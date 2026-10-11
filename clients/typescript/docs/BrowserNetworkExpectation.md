
# BrowserNetworkExpectation

Approved expectations and recorded candidates are separate. Body/path values remain typed JSON; exclusions affect network validation only.

## Properties

Name | Type
------------ | -------------
`enabled` | boolean
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
`expectedBodyPaths` | Array&lt;{ [key: string]: any; }&gt;
`candidateBodyPaths` | { [key: string]: any; }
`excludedBodyFields` | Array&lt;string&gt;

## Example

```typescript
import type { BrowserNetworkExpectation } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "enabled": null,
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
  "candidateBodyPaths": null,
  "excludedBodyFields": null,
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
