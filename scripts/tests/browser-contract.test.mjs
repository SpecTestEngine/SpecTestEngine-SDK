import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import test from 'node:test';

const require = createRequire(import.meta.url);
const sdk = require('../../clients/typescript/dist/index.js');
const wire = (value) => JSON.parse(JSON.stringify(value));
const exclusion = { xRatio: 0.8, yRatio: 0.1, widthRatio: 0.1, heightRatio: 0.2, reason: 'User-selected clock' };
const baselineRevisionId = '019f9000-7777-7000-8000-000000000777';
const assertion = {
  enabled: true, scopeType: 'REGION', compareMode: 'TEXT_AND_LAYOUT', stopPolicy: 'CONTINUE_AND_REVIEW',
  bounds: { leftRatio: 0.1, topRatio: 0.2, widthRatio: 0.8, heightRatio: 0.6 }, excludedRegions: [exclusion],
};

test('Flow input preserves browser session URL, selector chain, explicit sensitivity and typed network values', () => {
  const action = {
    actionType: 'EXTRACT_TEXT', selector: '#otp', selectorCandidates: ['[data-testid=otp]'],
    sensitive: true, textSource: 'ELEMENT_TEXT', variableName: 'otp', tabAlias: 'mail',
    timeoutMs: 12000, expectedNetworkPolicy: 'STRICT', visualAssertion: assertion,
    expectedNetworkCalls: [{ method: 'GET', url: '/mail', body: { unread: true, count: 2 },
      expectedBodyPaths: [{ path: '$.unread', value: true }, { path: '$.count', value: 2 }], excludedBodyFields: ['receivedAt'] }],
  };
  const input = { name: 'Fresh OTP', browserSession: { url: 'https://example.test', viewportWidth: 1280, viewportHeight: 720 },
    steps: [{ stepType: 'BROWSER_ACTION', browserAction: action }] };
  assert.deepEqual(wire(sdk.FlowInputToJSON(input)), input);
});

test('Inline macros preserve page identity and visual exclusion geometry', () => {
  const input = { name: 'Inline', steps: [{ stepType: 'UI_MACRO',
    uiMacro: { name: 'Macro', startUrl: 'https://example.test', steps: [
      { actionType: 'CLICK', pageId: 'page-2', tabAlias: 'mail', selector: '#open', visualAssertion: assertion },
    ] } }] };
  assert.deepEqual(wire(sdk.FlowInputToJSON(input)), input);
});

test('Saved Flow read models retain flattened browser fields and typed visual assertions', () => {
  const saved = { flowId: '019f9100-0000-7000-8000-000000000001', name: 'Saved', createdAt: '2026-08-28T10:00:00.000Z',
    browserStartUrl: 'https://example.test', steps: [{
      stepId: '019f9100-0000-7000-8000-000000000002', orderIndex: 0, stepType: 'BROWSER_ACTION',
      browserActionType: 'EXTRACT_TEXT', selector: '#otp', selectorCandidates: ['[data-testid=otp]'],
      variableName: 'otp', tabAlias: 'mail', visualAssertion: { ...assertion, assertionRevision: 4, baselineRevisionId },
    }] };
  assert.deepEqual(wire(sdk.FlowToJSON(sdk.FlowFromJSON(saved))), saved);
});

test('Run evidence retains immutable comparison lineage, artifact references and exclusion diagnostics', () => {
  const step = { stepId: '019f9100-0000-7000-8000-000000000002', orderIndex: 0, stepType: 'BROWSER_ACTION', stepStatus: 'FAIL',
    visualComparison: {
      comparisonId: '019f9100-0000-7000-8000-000000000003', status: 'FAILED',
      baselineArtifactId: '019f9000-2222-7000-8000-000000000222', actualArtifactId: '019f9000-1111-7000-8000-000000000111',
      baselineRevisionId, assertionRevision: 4, generationNumber: 2,
      rootComparisonId: '019f9100-0000-7000-8000-000000000001', sourceComparisonId: '019f9100-0000-7000-8000-000000000001',
      excludedRegions: [exclusion], changedExcludedRegionIndexes: [0], diffPixels: 10, diffPixelRatio: 0.01,
    } };
  assert.deepEqual(wire(sdk.FlowRunStepToJSON(sdk.FlowRunStepFromJSON(step))), step);
});
