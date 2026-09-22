
# SnapshotStepDiffSection


## Properties

Name | Type
------------ | -------------
`added` | [Array&lt;SnapshotStepDiffGroup&gt;](SnapshotStepDiffGroup.md)
`removed` | [Array&lt;SnapshotStepDiffGroup&gt;](SnapshotStepDiffGroup.md)
`changed` | [Array&lt;SnapshotStepDiffGroup&gt;](SnapshotStepDiffGroup.md)

## Example

```typescript
import type { SnapshotStepDiffSection } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "added": null,
  "removed": null,
  "changed": null,
} satisfies SnapshotStepDiffSection

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SnapshotStepDiffSection
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


