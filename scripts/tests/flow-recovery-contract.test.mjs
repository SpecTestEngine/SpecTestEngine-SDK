import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import test from 'node:test';

const require = createRequire(import.meta.url);
const sdk = require('../../clients/typescript/dist/index.js');
const runId = '019f9100-0000-7000-8000-000000000001';
const operationId = '019f9100-0000-7000-8000-000000000002';
const key = '019f9100-0000-7000-8000-000000000003';
const input = { manifestHash: 'a'.repeat(64), name: 'Recovered checkout', description: null,
  bindings: { count: 7, enabled: false, token: '${fresh.token}' } };
const operation = { operationId, state: 'OUTCOME_UNKNOWN', flowId: null, failureCode: null,
  idempotencyKey: key, name: input.name, description: null, manifestHash: input.manifestHash,
  copiedDependencies: 1, totalDependencies: 2 };

test('generated recovery transport keeps typed bindings, exact retries, pagination and GET-only readback', async () => {
  const calls = [];
  const api = new sdk.FlowsApi(new sdk.Configuration({ basePath: 'https://example.test',
    accessToken: 'fixture-authority', fetchApi: async (url, init) => {
      calls.push({ url, init });
      const body = url.endsWith('/preview') ? { runId, available: false, reason: 'LEGACY_NO_MANIFEST',
        manifestVersion: 1, stepCount: 0, copyCount: 0, bindings: [], dependencies: { items: [], page: 0,
          size: 20, totalElements: 0, totalPages: 0, first: true, last: true } }
        : url.includes('/dependencies?') ? { items: [], page: 2, size: 20, totalElements: 0, totalPages: 0, first: false, last: true }
        : url.includes('/dependencies/') ? { summary: { key: 'version/key', kind: 'REST', sourceName: 'Catalog',
          format: 'JSON', definitionHash: 'b'.repeat(64), roles: ['PLANNED_NOT_EXECUTED'], bindingCount: 0 },
          definition: { definitionJson: '{}', bindings: [], unavailableReason: null } } : operation;
      return new Response(JSON.stringify(body), { status: init.method === 'POST' ? 202 : 200,
        headers: { 'Content-Type': 'application/json', Location: `/test/flow/run/recovery-operations/${operationId}` } });
    } }));
  assert.equal((await api.previewFlowRecovery({ runId })).reason, 'LEGACY_NO_MANIFEST');
  await api.listFlowRecoveryDependencies({ runId, page: 2, size: 20 });
  const detail = await api.getFlowRecoveryDependency({ runId, dependencyKey: 'version/key' });
  assert.deepEqual(detail.summary.roles, ['PLANNED_NOT_EXECUTED']);
  const request = { runId, idempotencyKey: key, flowRecoveryInput: input };
  assert.equal((await api.createFlowRecovery(request)).state, 'OUTCOME_UNKNOWN');
  await api.getFlowRecoveryOperation({ operationId });
  await api.createFlowRecovery(request);
  assert.deepEqual(calls.map(({ init }) => init.method), ['GET', 'GET', 'GET', 'POST', 'GET', 'POST']);
  assert.match(calls[1].url, /page=2&size=20$/);
  assert.match(calls[2].url, /dependencies\/version%2Fkey$/);
  assert.equal(calls[3].init.headers['Idempotency-Key'], key);
  assert.deepEqual(JSON.parse(calls[3].init.body), input);
  assert.equal(calls[3].init.body, calls[5].init.body);
  assert.equal(calls[4].url, `https://example.test/test/flow/run/recovery-operations/${operationId}`);
  for (const { init } of calls) assert.equal(init.headers.Authorization, 'Bearer fixture-authority');
});
