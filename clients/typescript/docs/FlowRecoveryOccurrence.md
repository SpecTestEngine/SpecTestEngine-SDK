
# FlowRecoveryOccurrence


## Properties

Name | Type
------------ | -------------
`sourceStepId` | string
`orderIndex` | number
`dependencyKey` | string
`role` | string

## Example

```typescript
import type { FlowRecoveryOccurrence } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "sourceStepId": null,
  "orderIndex": null,
  "dependencyKey": null,
  "role": null,
} satisfies FlowRecoveryOccurrence

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryOccurrence
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
