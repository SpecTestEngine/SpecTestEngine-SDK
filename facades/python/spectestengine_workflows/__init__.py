"""Transport-neutral helpers for long-running SpecTestEngine workflows."""

from __future__ import annotations

from dataclasses import dataclass
import threading
import time
from typing import BinaryIO, Callable, Iterable, Iterator, TypeVar

T = TypeVar("T")


class WorkflowTimeoutError(TimeoutError):
    """Raised when a workflow does not reach a terminal state in time."""


def poll_workflow(
    fetch_value: Callable[[], T],
    is_terminal: Callable[[T], bool],
    *,
    interval_seconds: float = 0.5,
    max_interval_seconds: float = 5.0,
    timeout_seconds: float = 120.0,
    backoff: float = 1.5,
    cancelled: threading.Event | None = None,
    on_update: Callable[[T], None] | None = None,
) -> T:
    if interval_seconds <= 0 or max_interval_seconds < interval_seconds or timeout_seconds <= 0 or backoff < 1:
        raise ValueError("polling intervals, timeout, and backoff must be valid")
    deadline = time.monotonic() + timeout_seconds
    delay = interval_seconds
    while True:
        if cancelled is not None and cancelled.is_set():
            raise InterruptedError("workflow polling was cancelled")
        value = fetch_value()
        if on_update is not None:
            on_update(value)
        if is_terminal(value):
            return value
        if time.monotonic() >= deadline:
            raise WorkflowTimeoutError("workflow did not reach a terminal state before the timeout")
        if cancelled is None:
            time.sleep(delay)
        elif cancelled.wait(delay):
            raise InterruptedError("workflow polling was cancelled")
        delay = min(max_interval_seconds, max(delay, delay * backoff))


@dataclass(frozen=True)
class SseEvent:
    event: str
    data: str
    id: str | None = None
    retry_ms: int | None = None


def iter_sse(lines: Iterable[str]) -> Iterator[SseEvent]:
    data: list[str] = []
    event: str | None = None
    event_id: str | None = None
    retry_ms: int | None = None

    def dispatch() -> SseEvent | None:
        nonlocal data, event, retry_ms
        if not data and event is None and event_id is None and retry_ms is None:
            return None
        value = SseEvent(event or "message", "\n".join(data), event_id, retry_ms)
        data = []
        event = None
        retry_ms = None
        return value

    for raw_line in lines:
        line = raw_line.rstrip("\r\n")
        if not line:
            value = dispatch()
            if value is not None:
                yield value
            continue
        if line.startswith(":"):
            continue
        field, separator, raw_value = line.partition(":")
        value = raw_value[1:] if separator and raw_value.startswith(" ") else raw_value
        if field == "data":
            data.append(value)
        elif field == "event":
            event = value
        elif field == "id":
            event_id = value
        elif field == "retry" and value.isdigit():
            retry_ms = int(value)
    value = dispatch()
    if value is not None:
        yield value


def copy_stream(
    source: BinaryIO,
    target: BinaryIO,
    *,
    max_bytes: int,
    on_progress: Callable[[int], None] | None = None,
) -> int:
    if max_bytes <= 0:
        raise ValueError("max_bytes must be positive")
    total = 0
    while chunk := source.read(64 * 1024):
        total += len(chunk)
        if total > max_bytes:
            raise ValueError("stream exceeded the configured byte limit")
        target.write(chunk)
        if on_progress is not None:
            on_progress(total)
    return total


__all__ = ["SseEvent", "WorkflowTimeoutError", "copy_stream", "iter_sse", "poll_workflow"]
