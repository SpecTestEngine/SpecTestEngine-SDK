package software.ste.sdk.workflows;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import java.util.function.Consumer;
import java.util.function.LongConsumer;
import java.util.function.Predicate;

/** Transport-neutral helpers for long-running SpecTestEngine workflows. */
public final class WorkflowSupport {
    private WorkflowSupport() {
    }

    @FunctionalInterface
    public interface CheckedSupplier<T> {
        T get() throws Exception;
    }

    public record PollOptions(Duration interval, Duration maxInterval, Duration timeout, double backoff) {
        public PollOptions {
            Objects.requireNonNull(interval, "interval");
            Objects.requireNonNull(maxInterval, "maxInterval");
            Objects.requireNonNull(timeout, "timeout");
            if (interval.isZero() || interval.isNegative()) {
                throw new IllegalArgumentException("interval must be positive");
            }
            if (maxInterval.compareTo(interval) < 0 || timeout.isZero() || timeout.isNegative()) {
                throw new IllegalArgumentException("maxInterval and timeout must be valid");
            }
            if (backoff < 1.0) {
                throw new IllegalArgumentException("backoff must be at least 1.0");
            }
        }

        public static PollOptions defaults() {
            return new PollOptions(Duration.ofMillis(500), Duration.ofSeconds(5), Duration.ofMinutes(2), 1.5);
        }
    }

    public static <T> T poll(
            CheckedSupplier<T> fetch,
            Predicate<T> terminal,
            PollOptions options,
            Consumer<T> onUpdate) throws Exception {
        Objects.requireNonNull(fetch, "fetch");
        Objects.requireNonNull(terminal, "terminal");
        Objects.requireNonNull(options, "options");
        long deadline = System.nanoTime() + options.timeout().toNanos();
        Duration delay = options.interval();

        while (true) {
            if (Thread.currentThread().isInterrupted()) {
                throw new InterruptedException("workflow polling was cancelled");
            }
            T value = fetch.get();
            if (onUpdate != null) {
                onUpdate.accept(value);
            }
            if (terminal.test(value)) {
                return value;
            }
            if (System.nanoTime() >= deadline) {
                throw new WorkflowTimeoutException("workflow did not reach a terminal state before the timeout");
            }
            Thread.sleep(delay.toMillis());
            long nextMillis = Math.min(
                    options.maxInterval().toMillis(),
                    Math.max(delay.toMillis(), Math.round(delay.toMillis() * options.backoff())));
            delay = Duration.ofMillis(nextMillis);
        }
    }

    public static long copy(
            InputStream source,
            OutputStream target,
            long maxBytes,
            LongConsumer onProgress) throws IOException {
        if (maxBytes <= 0) {
            throw new IllegalArgumentException("maxBytes must be positive");
        }
        byte[] buffer = new byte[64 * 1024];
        long total = 0;
        int read;
        while ((read = source.read(buffer)) != -1) {
            total += read;
            if (total > maxBytes) {
                throw new IOException("stream exceeded the configured byte limit");
            }
            target.write(buffer, 0, read);
            if (onProgress != null) {
                onProgress.accept(total);
            }
        }
        return total;
    }

    public record SseEvent(String event, String data, String id, Long retryMillis) {
    }

    public static final class SseParser {
        private final List<String> data = new ArrayList<>();
        private String event;
        private String id;
        private Long retryMillis;

        public Optional<SseEvent> accept(String line) {
            Objects.requireNonNull(line, "line");
            if (line.isEmpty()) {
                return dispatch();
            }
            if (line.startsWith(":")) {
                return Optional.empty();
            }
            int separator = line.indexOf(':');
            String field = separator < 0 ? line : line.substring(0, separator);
            String value = separator < 0 ? "" : line.substring(separator + 1);
            if (value.startsWith(" ")) {
                value = value.substring(1);
            }
            switch (field) {
                case "event" -> event = value;
                case "data" -> data.add(value);
                case "id" -> id = value;
                case "retry" -> retryMillis = parseRetry(value);
                default -> {
                    // Unknown SSE fields are ignored by the protocol.
                }
            }
            return Optional.empty();
        }

        public Optional<SseEvent> finish() {
            return dispatch();
        }

        private Optional<SseEvent> dispatch() {
            if (data.isEmpty() && event == null && id == null && retryMillis == null) {
                return Optional.empty();
            }
            SseEvent value = new SseEvent(event == null ? "message" : event, String.join("\n", data), id, retryMillis);
            data.clear();
            event = null;
            retryMillis = null;
            return Optional.of(value);
        }

        private static Long parseRetry(String value) {
            try {
                long parsed = Long.parseLong(value);
                return parsed >= 0 ? parsed : null;
            } catch (NumberFormatException ignored) {
                return null;
            }
        }
    }

    public static final class WorkflowTimeoutException extends RuntimeException {
        public WorkflowTimeoutException(String message) {
            super(message);
        }
    }
}
