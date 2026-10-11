
# FragmentDraftAssembly


## Properties

Name | Type
------------ | -------------
`specType` | [SpecType](SpecType.md)
`streamingTransport` | [StreamingTransport](StreamingTransport.md)
`fragments` | [Array&lt;FragmentDraftInput&gt;](FragmentDraftInput.md)

## Example

```typescript
import type { FragmentDraftAssembly } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "specType": null,
  "streamingTransport": null,
  "fragments": null,
} satisfies FragmentDraftAssembly

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FragmentDraftAssembly
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
