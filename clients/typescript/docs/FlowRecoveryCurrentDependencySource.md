
# FlowRecoveryCurrentDependencySource


## Properties

Name | Type
------------ | -------------
`sourceId` | string
`revision` | number
`name` | string
`format` | string
`definition` | [FlowRecoveryProjection](FlowRecoveryProjection.md)

## Example

```typescript
import type { FlowRecoveryCurrentDependencySource } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "sourceId": null,
  "revision": null,
  "name": null,
  "format": null,
  "definition": null,
} satisfies FlowRecoveryCurrentDependencySource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryCurrentDependencySource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
