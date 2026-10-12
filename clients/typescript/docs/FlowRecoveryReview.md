
# FlowRecoveryReview


## Properties

Name | Type
------------ | -------------
`historical` | [FlowRecoveryPreview](FlowRecoveryPreview.md)
`targetRevision` | number
`targetName` | string
`targetDescription` | string
`dependencyRevisions` | { [key: string]: number; }
`occurrences` | [Array&lt;FlowRecoveryOccurrence&gt;](FlowRecoveryOccurrence.md)
`restoreAvailable` | boolean
`restoreReason` | string

## Example

```typescript
import type { FlowRecoveryReview } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "historical": null,
  "targetRevision": null,
  "targetName": null,
  "targetDescription": null,
  "dependencyRevisions": null,
  "occurrences": null,
  "restoreAvailable": null,
  "restoreReason": null,
} satisfies FlowRecoveryReview

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryReview
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
