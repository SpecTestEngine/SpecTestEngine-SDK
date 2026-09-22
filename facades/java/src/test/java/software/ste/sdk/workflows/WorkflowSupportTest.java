package software.ste.sdk.workflows;

import java.time.Duration;
import java.util.concurrent.atomic.AtomicInteger;

public final class WorkflowSupportTest {
    public static void main(String[] args) throws Exception {
        AtomicInteger attempts = new AtomicInteger();
        int result = WorkflowSupport.poll(
                attempts::incrementAndGet,
                value -> value == 3,
                new WorkflowSupport.PollOptions(
                        Duration.ofMillis(1), Duration.ofMillis(2), Duration.ofSeconds(1), 1.0),
                null);
        if (result != 3) {
            throw new AssertionError("poll did not return the terminal value");
        }

        WorkflowSupport.SseParser parser = new WorkflowSupport.SseParser();
        parser.accept("event: progress");
        parser.accept("data: first");
        parser.accept("data: second");
        WorkflowSupport.SseEvent event = parser.accept("").orElseThrow();
        if (!"first\nsecond".equals(event.data())) {
            throw new AssertionError("SSE multiline data was not preserved");
        }
    }
}
