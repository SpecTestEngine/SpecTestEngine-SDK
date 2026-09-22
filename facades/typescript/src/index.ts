export interface PollOptions {
  intervalMs?: number;
  maxIntervalMs?: number;
  timeoutMs?: number;
  backoff?: number;
  signal?: AbortSignal;
}

export async function pollWorkflow<T>(
  fetchValue: () => Promise<T>,
  isTerminal: (value: T) => boolean,
  options: PollOptions = {},
  onUpdate?: (value: T) => void,
): Promise<T> {
  const interval = positive(options.intervalMs ?? 500, "intervalMs");
  const maximum = positive(options.maxIntervalMs ?? 5000, "maxIntervalMs");
  const timeout = positive(options.timeoutMs ?? 120000, "timeoutMs");
  const backoff = options.backoff ?? 1.5;
  if (maximum < interval || backoff < 1) {
    throw new RangeError("maxIntervalMs and backoff must be valid");
  }
  const deadline = Date.now() + timeout;
  let delay = interval;

  while (true) {
    options.signal?.throwIfAborted();
    const value = await fetchValue();
    onUpdate?.(value);
    if (isTerminal(value)) return value;
    if (Date.now() >= deadline) throw new WorkflowTimeoutError();
    await sleep(delay, options.signal);
    delay = Math.min(maximum, Math.max(delay, Math.round(delay * backoff)));
  }
}

export interface SseEvent {
  event: string;
  data: string;
  id?: string;
  retryMs?: number;
}

export class SseParser {
  private data: string[] = [];
  private event?: string;
  private id?: string;
  private retryMs?: number;

  accept(line: string): SseEvent | undefined {
    if (line === "") return this.dispatch();
    if (line.startsWith(":")) return undefined;
    const separator = line.indexOf(":");
    const field = separator < 0 ? line : line.slice(0, separator);
    let value = separator < 0 ? "" : line.slice(separator + 1);
    if (value.startsWith(" ")) value = value.slice(1);
    if (field === "data") this.data.push(value);
    else if (field === "event") this.event = value;
    else if (field === "id") this.id = value;
    else if (field === "retry" && /^\d+$/.test(value)) this.retryMs = Number(value);
    return undefined;
  }

  finish(): SseEvent | undefined {
    return this.dispatch();
  }

  private dispatch(): SseEvent | undefined {
    if (!this.data.length && this.event === undefined && this.id === undefined && this.retryMs === undefined) {
      return undefined;
    }
    const result: SseEvent = {
      event: this.event ?? "message",
      data: this.data.join("\n"),
      ...(this.id === undefined ? {} : { id: this.id }),
      ...(this.retryMs === undefined ? {} : { retryMs: this.retryMs }),
    };
    this.data = [];
    this.event = undefined;
    this.retryMs = undefined;
    return result;
  }
}

export async function readSseStream(
  stream: ReadableStream<Uint8Array>,
  onEvent: (event: SseEvent) => void,
  signal?: AbortSignal,
): Promise<void> {
  const reader = stream.getReader();
  const decoder = new TextDecoder();
  const parser = new SseParser();
  let pending = "";
  try {
    while (true) {
      signal?.throwIfAborted();
      const { done, value } = await reader.read();
      if (done) break;
      pending += decoder.decode(value, { stream: true }).replace(/\r\n/g, "\n");
      const lines = pending.split("\n");
      pending = lines.pop() ?? "";
      for (const line of lines) {
        const event = parser.accept(line);
        if (event) onEvent(event);
      }
    }
    pending += decoder.decode();
    if (pending) {
      const event = parser.accept(pending);
      if (event) onEvent(event);
    }
    const finalEvent = parser.finish();
    if (finalEvent) onEvent(finalEvent);
  } finally {
    reader.releaseLock();
  }
}

export async function readBinaryStream(
  stream: ReadableStream<Uint8Array>,
  maxBytes: number,
  onProgress?: (bytesRead: number) => void,
): Promise<Uint8Array> {
  positive(maxBytes, "maxBytes");
  const reader = stream.getReader();
  const chunks: Uint8Array[] = [];
  let total = 0;
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      total += value.byteLength;
      if (total > maxBytes) throw new RangeError("stream exceeded the configured byte limit");
      chunks.push(value);
      onProgress?.(total);
    }
  } finally {
    reader.releaseLock();
  }
  const result = new Uint8Array(total);
  let offset = 0;
  for (const chunk of chunks) {
    result.set(chunk, offset);
    offset += chunk.byteLength;
  }
  return result;
}

export class WorkflowTimeoutError extends Error {
  constructor() {
    super("workflow did not reach a terminal state before the timeout");
    this.name = "WorkflowTimeoutError";
  }
}

function positive(value: number, name: string): number {
  if (!Number.isFinite(value) || value <= 0) throw new RangeError(`${name} must be positive`);
  return value;
}

function sleep(milliseconds: number, signal?: AbortSignal): Promise<void> {
  return new Promise((resolve, reject) => {
    const onAbort = () => {
      clearTimeout(timer);
      reject(signal?.reason ?? new DOMException("The operation was aborted", "AbortError"));
    };
    const timer = setTimeout(() => {
      signal?.removeEventListener("abort", onAbort);
      resolve();
    }, milliseconds);
    signal?.addEventListener("abort", onAbort, { once: true });
  });
}
