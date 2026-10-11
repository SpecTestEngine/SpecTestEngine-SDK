
# FlowRecoveryProjection


## Properties

Name | Type
------------ | -------------
`definitionJson` | string
`bindings` | [Array&lt;FlowRecoveryBinding&gt;](FlowRecoveryBinding.md)
`unavailableReason` | string

## Example

```typescript
import type { FlowRecoveryProjection } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "definitionJson": null,
  "bindings": null,
  "unavailableReason": null,
} satisfies FlowRecoveryProjection

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryProjection
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
