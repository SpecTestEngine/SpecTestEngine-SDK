package workflows

import (
	"bufio"
	"context"
	"errors"
	"fmt"
	"io"
	"strconv"
	"strings"
	"time"
)

var ErrWorkflowTimeout = errors.New("workflow did not reach a terminal state before the timeout")

type PollOptions struct {
	Interval        time.Duration
	MaximumInterval time.Duration
	Timeout         time.Duration
	Backoff         float64
}

func DefaultPollOptions() PollOptions {
	return PollOptions{Interval: 500 * time.Millisecond, MaximumInterval: 5 * time.Second, Timeout: 2 * time.Minute, Backoff: 1.5}
}

func Poll[T any](
	ctx context.Context,
	fetch func(context.Context) (T, error),
	terminal func(T) bool,
	options PollOptions,
	onUpdate func(T),
) (T, error) {
	var zero T
	if options.Interval <= 0 || options.MaximumInterval < options.Interval || options.Timeout <= 0 || options.Backoff < 1 {
		return zero, fmt.Errorf("invalid polling options")
	}
	deadline := time.Now().Add(options.Timeout)
	delay := options.Interval
	for {
		if err := ctx.Err(); err != nil {
			return zero, err
		}
		value, err := fetch(ctx)
		if err != nil {
			return zero, err
		}
		if onUpdate != nil {
			onUpdate(value)
		}
		if terminal(value) {
			return value, nil
		}
		if !time.Now().Before(deadline) {
			return zero, ErrWorkflowTimeout
		}
		timer := time.NewTimer(delay)
		select {
		case <-ctx.Done():
			if !timer.Stop() {
				select {
				case <-timer.C:
				default:
				}
			}
			return zero, ctx.Err()
		case <-timer.C:
		}
		next := time.Duration(float64(delay) * options.Backoff)
		if next < delay {
			next = delay
		}
		if next > options.MaximumInterval {
			next = options.MaximumInterval
		}
		delay = next
	}
}

func Copy(source io.Reader, target io.Writer, maximumBytes int64, onProgress func(int64)) (int64, error) {
	if maximumBytes <= 0 {
		return 0, fmt.Errorf("maximumBytes must be positive")
	}
	buffer := make([]byte, 64*1024)
	var total int64
	for {
		read, readErr := source.Read(buffer)
		if read > 0 {
			total += int64(read)
			if total > maximumBytes {
				return total, fmt.Errorf("stream exceeded the configured byte limit")
			}
			if _, err := target.Write(buffer[:read]); err != nil {
				return total, err
			}
			if onProgress != nil {
				onProgress(total)
			}
		}
		if errors.Is(readErr, io.EOF) {
			return total, nil
		}
		if readErr != nil {
			return total, readErr
		}
	}
}

type SseEvent struct {
	Event             string
	Data              string
	ID                string
	RetryMilliseconds *int64
}

type SseParser struct {
	data              []string
	event             string
	id                string
	retryMilliseconds *int64
}

func (parser *SseParser) Accept(line string) *SseEvent {
	line = strings.TrimSuffix(strings.TrimSuffix(line, "\n"), "\r")
	if line == "" {
		return parser.dispatch()
	}
	if strings.HasPrefix(line, ":") {
		return nil
	}
	field, value, found := strings.Cut(line, ":")
	if !found {
		value = ""
	}
	value = strings.TrimPrefix(value, " ")
	switch field {
	case "event":
		parser.event = value
	case "data":
		parser.data = append(parser.data, value)
	case "id":
		parser.id = value
	case "retry":
		if retry, err := strconv.ParseInt(value, 10, 64); err == nil && retry >= 0 {
			parser.retryMilliseconds = &retry
		}
	}
	return nil
}

func (parser *SseParser) Finish() *SseEvent {
	return parser.dispatch()
}

func (parser *SseParser) dispatch() *SseEvent {
	if len(parser.data) == 0 && parser.event == "" && parser.id == "" && parser.retryMilliseconds == nil {
		return nil
	}
	event := parser.event
	if event == "" {
		event = "message"
	}
	result := &SseEvent{Event: event, Data: strings.Join(parser.data, "\n"), ID: parser.id, RetryMilliseconds: parser.retryMilliseconds}
	parser.data = nil
	parser.event = ""
	parser.retryMilliseconds = nil
	return result
}

func ReadSse(source io.Reader, onEvent func(SseEvent) error) error {
	if onEvent == nil {
		return fmt.Errorf("onEvent is required")
	}
	parser := &SseParser{}
	scanner := bufio.NewScanner(source)
	scanner.Buffer(make([]byte, 64*1024), 1024*1024)
	for scanner.Scan() {
		if event := parser.Accept(scanner.Text()); event != nil {
			if err := onEvent(*event); err != nil {
				return err
			}
		}
	}
	if err := scanner.Err(); err != nil {
		return err
	}
	if event := parser.Finish(); event != nil {
		return onEvent(*event)
	}
	return nil
}
