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
  const step = { stepId: '019f9100-0000-7000-8000-000000000002', orderIndex: 0, stepType: 'BROWSER_ACTION', stepStatus: '----------------FAIL-------------------',
    visualComparison: {
      comparisonId: '019f9100-0000-7000-8000-000000000003', status: '----------------FAIL-------------------',
      baselineArtifactId: '019f9000-2222-7000-8000-000000000222', actualArtifactId: '019f9000-1111-7000-8000-000000000111',
      baselineRevisionId, assertionRevision: 4, generationNumber: 2,
      rootComparisonId: '019f9100-0000-7000-8000-000000000001', sourceComparisonId: '019f9100-0000-7000-8000-000000000001',
      excludedRegions: [exclusion], changedExcludedRegionIndexes: [0], diffPixels: 10, diffPixelRatio: 0.01,
    } };
  assert.deepEqual(wire(sdk.FlowRunStepToJSON(sdk.FlowRunStepFromJSON(step))), step);
});


test('Value transfer, selected occurrences and typed request paths survive generated SDK serialization', () => {
  const call = { method: 'POST', url: 'https://example.test/orders', occurrence: 2,
    headers: { authorization: 'Bearer ${runtime.current}' },
    requestBodyPaths: [
      { path: 'id', value: '${runtime.id}' },
      { path: 'optional', value: null },
      { path: 'active', value: false },
      { path: 'count', value: 7 },
      { path: 'opaque', value: '123' },
    ],
    runtimeBindings: [{ name: 'current', source: 'RESPONSE_BODY', path: 'access_token', scopeOrigin: 'https://example.test' }],
    candidateFields: { requestHeaders: ['authorization'], requestBody: [{ path: '$.id', type: 'NUMBER' }],
      responseBody: [{ path: '$.access_token', type: 'STRING' }], requestHeadersComplete: true, requestBodyComplete: false, responseBodyComplete: true },
  };
  assert.deepEqual(wire(sdk.BrowserNetworkExpectationToJSON(sdk.BrowserNetworkExpectationFromJSON(call))), call);
});

test('Automatic authorization retains metadata and cookie guards without runtime credential values', () => {
  const call = { method: 'POST', url: 'https://identity.test/refresh', policy: 'IGNORE',
    authTransfer: { sources: [{ name: 'auth', source: 'RESPONSE_BODY', path: '/accessToken', scopeOrigin: 'https://api.test',
      updateFrom: { variable: 'auth_input_1', source: 'REQUEST_COOKIE', path: 'refresh_token', prefix: '' } }],
      candidates: [], optionalRefresh: true },
  };
  assert.deepEqual(wire(sdk.BrowserNetworkExpectationToJSON(sdk.BrowserNetworkExpectationFromJSON(call))), call);
  const page = { items: [{ id: '019f9300-0000-7000-8000-000000000001', stableKey: 'customer-authentication', name: 'Login', protocol: 'REST',
    outputs: { accessToken: { path: '/accessToken', type: 'string', required: true } } }], page: 0, size: 20, totalElements: 1, totalPages: 1, first: true, last: true };
  assert.deepEqual(wire(sdk.PreparationPageToJSON(sdk.PreparationPageFromJSON(page))), page);
});


test('Preparation catalogs preserve every native protocol and typed outputs; engine statuses retain exact wire strings',()=>{
 for(const protocol of ['REST','SOAP','GRAPHQL','STREAMING']){
  const page={items:[{id:'019f9400-0000-7000-8000-000000000001',stableKey:'customer-authentication',name:'Login',protocol,
   outputs:{accessToken:{path:'/accessToken',type:'string',required:true},count:{path:'/count',type:'number',required:false}}}],
   page:0,size:20,totalElements:1,totalPages:1,first:true,last:true};
  assert.deepEqual(wire(sdk.PreparationPageToJSON(sdk.PreparationPageFromJSON(page))),page);
 }
 for(const status of ['----------------PASS-------------------','----------------FAIL-------------------','---------------ERROR-------------------']){
  assert.equal(sdk.RunStatusToJSON(sdk.RunStatusFromJSON(status)),status);
 }
});


test('Current Browser authoring fields and focused patterns survive all transport projections', () => {
  const action = { actionType: 'PASTE_ADDRESS_BAR', textSource: 'LINK_URL', expectedPageUrlPolicy: 'MATCH',
    expectedPageTitlePolicy: 'MATCH', targetMatch: { role: 'button', name: 'Continue', destination: { role: 'group', name: 'Cart' } },
    expectedNetworkCalls: [{ expectedHeaderPaths: [{path: 'content-type', pattern: 'application/*'}],
      expectedBodyPaths: [{path: '/count', value: 3}], stream: {transport: 'SSE', direction: 'INBOUND', eventName: 'update', binary: false, failed: false} }] };
  assert.deepEqual(wire(sdk.BrowserActionInputToJSON(sdk.BrowserActionInputFromJSON(action))), action);
});


test('Whole Browser body operands preserve null and never introduce absent checks', () => {
  for (const wire of [{headers:{accept:'application/json'}}, {body:null}, {candidateBody:null}, {expectedBody:null}, {expectedBody:false}, {expectedBody:7}, {expectedBody:'123'}])
    assert.deepEqual(JSON.parse(JSON.stringify(sdk.BrowserNetworkExpectationToJSON(sdk.BrowserNetworkExpectationFromJSON(wire)))),wire);
});
