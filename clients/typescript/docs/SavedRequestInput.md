
# SavedRequestInput

HTTP-shaped fields are required for REST/SOAP/GraphQL; streamingSpec is required for STREAMING.

## Properties

Name | Type
------------ | -------------
`specType` | string
`method` | string
`url` | string
`streamingSpec` | [StreamingDefinition](StreamingDefinition.md)
`headers` | { [key: string]: string; }
`queryParams` | { [key: string]: string; }
`body` | string
`auth` | { [key: string]: any; }
`requestAuth` | { [key: string]: any; }
`requestAttachments` | [Array&lt;DocumentAssetReference&gt;](DocumentAssetReference.md)
`prerequisites` | Array&lt;{ [key: string]: any; }&gt;

## Example

```typescript
import type { SavedRequestInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "specType": null,
  "method": null,
  "url": null,
  "streamingSpec": null,
  "headers": null,
  "queryParams": null,
  "body": null,
  "auth": null,
  "requestAuth": null,
  "requestAttachments": null,
  "prerequisites": null,
} satisfies SavedRequestInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SavedRequestInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


