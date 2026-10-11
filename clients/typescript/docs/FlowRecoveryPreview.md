
# FlowRecoveryPreview


## Properties

Name | Type
------------ | -------------
`runId` | string
`available` | boolean
`reason` | string
`manifestVersion` | number
`manifestHash` | string
`suggestedName` | string
`flow` | [FlowRecoveryHistoricalDefinition](FlowRecoveryHistoricalDefinition.md)
`stepCount` | number
`copyCount` | number
`bindings` | [Array&lt;FlowRecoveryBinding&gt;](FlowRecoveryBinding.md)
`dependencies` | [FlowRecoveryDependencyPage](FlowRecoveryDependencyPage.md)
`activeOperation` | [FlowRecoveryOperation](FlowRecoveryOperation.md)

## Example

```typescript
import type { FlowRecoveryPreview } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "runId": null,
  "available": null,
  "reason": null,
  "manifestVersion": null,
  "manifestHash": null,
  "suggestedName": null,
  "flow": null,
  "stepCount": null,
  "copyCount": null,
  "bindings": null,
  "dependencies": null,
  "activeOperation": null,
} satisfies FlowRecoveryPreview

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryPreview
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
