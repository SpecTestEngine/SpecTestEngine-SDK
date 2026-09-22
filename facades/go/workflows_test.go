package workflows

import (
	"context"
	"strings"
	"testing"
	"time"
)

func TestPollReturnsTerminalValue(t *testing.T) {
	attempts := 0
	value, err := Poll(context.Background(), func(context.Context) (int, error) {
		attempts++
		return attempts, nil
	}, func(value int) bool { return value == 3 }, PollOptions{
		Interval: time.Millisecond, MaximumInterval: time.Millisecond, Timeout: time.Second, Backoff: 1,
	}, nil)
	if err != nil || value != 3 {
		t.Fatalf("unexpected poll result: value=%d error=%v", value, err)
	}
}

func TestReadSsePreservesMultilineData(t *testing.T) {
	var data string
	err := ReadSse(strings.NewReader("event: progress\ndata: first\ndata: second\n\n"), func(event SseEvent) error {
		data = event.Data
		return nil
	})
	if err != nil || data != "first\nsecond" {
		t.Fatalf("unexpected SSE result: data=%q error=%v", data, err)
	}
}
