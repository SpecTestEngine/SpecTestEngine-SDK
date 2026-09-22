import assert from "node:assert/strict";
import test from "node:test";

import { pollWorkflow, SseParser } from "../dist/index.js";

test("pollWorkflow returns the terminal value", async () => {
  let attempts = 0;
  const value = await pollWorkflow(
    async () => ++attempts,
    (candidate) => candidate === 3,
    { intervalMs: 1, maxIntervalMs: 1, timeoutMs: 1000, backoff: 1 },
  );
  assert.equal(value, 3);
});

test("SseParser preserves multiline data", () => {
  const parser = new SseParser();
  parser.accept("event: progress");
  parser.accept("data: first");
  parser.accept("data: second");
  assert.deepEqual(parser.accept(""), {
    event: "progress",
    data: "first\nsecond",
  });
});
