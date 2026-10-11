
# SnapshotStepDiff


## Properties

Name | Type
------------ | -------------
`stepType` | [SnapshotStepType](SnapshotStepType.md)
`overview` | Array&lt;string&gt;
`definition` | [SnapshotStepDiffSection](SnapshotStepDiffSection.md)
`behavior` | [SnapshotStepDiffSection](SnapshotStepDiffSection.md)

## Example

```typescript
import type { SnapshotStepDiff } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "stepType": null,
  "overview": null,
  "definition": null,
  "behavior": null,
} satisfies SnapshotStepDiff

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SnapshotStepDiff
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
