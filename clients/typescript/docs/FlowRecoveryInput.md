
# FlowRecoveryInput


## Properties

Name | Type
------------ | -------------
`manifestHash` | string
`name` | string
`description` | string
`bindings` | { [key: string]: any; }

## Example

```typescript
import type { FlowRecoveryInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "manifestHash": null,
  "name": null,
  "description": null,
  "bindings": null,
} satisfies FlowRecoveryInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
