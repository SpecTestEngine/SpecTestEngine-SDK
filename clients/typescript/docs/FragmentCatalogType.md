
# FragmentCatalogType


## Properties

Name | Type
------------ | -------------
`type` | [FragmentType](FragmentType.md)
`allowedFields` | Array&lt;string&gt;
`singleton` | boolean
`editorMode` | string
`compatibleStreamingTransports` | [Set&lt;StreamingTransport&gt;](StreamingTransport.md)
`starterTemplate` | { [key: string]: any; }

## Example

```typescript
import type { FragmentCatalogType } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "type": null,
  "allowedFields": null,
  "singleton": null,
  "editorMode": null,
  "compatibleStreamingTransports": null,
  "starterTemplate": null,
} satisfies FragmentCatalogType

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FragmentCatalogType
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
