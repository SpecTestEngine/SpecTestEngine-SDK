
# SnapshotStepDiffInput


## Properties

Name | Type
------------ | -------------
`stepType` | [SnapshotStepType](SnapshotStepType.md)
`leftDefinitionPayload` | any
`rightDefinitionPayload` | any
`leftBehaviorPayload` | any
`rightBehaviorPayload` | any

## Example

```typescript
import type { SnapshotStepDiffInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "stepType": null,
  "leftDefinitionPayload": null,
  "rightDefinitionPayload": null,
  "leftBehaviorPayload": null,
  "rightBehaviorPayload": null,
} satisfies SnapshotStepDiffInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SnapshotStepDiffInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
