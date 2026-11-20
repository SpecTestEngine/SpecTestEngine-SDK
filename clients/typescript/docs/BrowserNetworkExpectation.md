
# BrowserNetworkExpectation

Local checks over observed browser traffic, never a second HTTP send. Candidates are not executable checks. Recorded credentials are rejected; current-run bindings are private and optional. Body and headers constrain the request; expectedBody and expectedHeaders constrain the response. Explicit empty response-header objects are checks. Unsupported OpenAPI/schema/attachment assertions are rejected, not processed by Browser.

## Properties

Name | Type
------------ | -------------
`enabled` | boolean
`policy` | string
`recordedCallId` | number
`recordedUrl` | string
`method` | string
`url` | string
`expectedStatusCode` | number
`candidateStatusCode` | number
`expectedContentType` | string
`candidateContentType` | string
`expectedHeaders` | { [key: string]: string; }
`candidateHeaders` | { [key: string]: string; }
`excludedHeaderFields` | Array&lt;string&gt;
`excludeAllOtherHeaderFields` | boolean
`body` | any
`candidateBody` | any
`expectedBodyPaths` | [Array&lt;BrowserPathExpectation&gt;](BrowserPathExpectation.md)
`expectedHeaderPaths` | [Array&lt;BrowserPathExpectation&gt;](BrowserPathExpectation.md)
`stream` | [BrowserStreamMessage](BrowserStreamMessage.md)
`candidateBodyPaths` | { [key: string]: any; }
`excludedBodyFields` | Array&lt;string&gt;
`headers` | { [key: string]: string; }
`expectedBody` | any
`skipExactBodyCheck` | boolean
`excludeAllOtherBodyFields` | boolean
`occurrence` | number
`requestBodyPaths` | [Array&lt;BrowserPathExpectation&gt;](BrowserPathExpectation.md)
`candidateFields` | [BrowserNetworkFieldInventory](BrowserNetworkFieldInventory.md)
`authTransfer` | [BrowserAuthTransfer](BrowserAuthTransfer.md)
`runtimeBindings` | [Array&lt;BrowserNetworkRuntimeBinding&gt;](BrowserNetworkRuntimeBinding.md)

## Example

```typescript
import type { BrowserNetworkExpectation } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "enabled": null,
  "policy": null,
  "recordedCallId": null,
  "recordedUrl": null,
  "method": null,
  "url": null,
  "expectedStatusCode": null,
  "candidateStatusCode": null,
  "expectedContentType": null,
  "candidateContentType": null,
  "expectedHeaders": null,
  "candidateHeaders": null,
  "excludedHeaderFields": null,
  "excludeAllOtherHeaderFields": null,
  "body": null,
  "candidateBody": null,
  "expectedBodyPaths": null,
  "expectedHeaderPaths": null,
  "stream": null,
  "candidateBodyPaths": null,
  "excludedBodyFields": null,
  "headers": null,
  "expectedBody": null,
  "skipExactBodyCheck": null,
  "excludeAllOtherBodyFields": null,
  "occurrence": null,
  "requestBodyPaths": null,
  "candidateFields": null,
  "authTransfer": null,
  "runtimeBindings": null,
} satisfies BrowserNetworkExpectation

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserNetworkExpectation
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
