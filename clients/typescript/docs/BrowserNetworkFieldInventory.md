
# BrowserNetworkFieldInventory


## Properties

Name | Type
------------ | -------------
`requestHeaders` | Array&lt;string&gt;
`requestBody` | [Array&lt;BrowserNetworkField&gt;](BrowserNetworkField.md)
`responseBody` | [Array&lt;BrowserNetworkField&gt;](BrowserNetworkField.md)
`requestHeadersComplete` | boolean
`requestBodyComplete` | boolean
`responseBodyComplete` | boolean

## Example

```typescript
import type { BrowserNetworkFieldInventory } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "requestHeaders": null,
  "requestBody": null,
  "responseBody": null,
  "requestHeadersComplete": null,
  "requestBodyComplete": null,
  "responseBodyComplete": null,
} satisfies BrowserNetworkFieldInventory

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserNetworkFieldInventory
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
