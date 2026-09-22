
# DocumentVisualDiffBaselinePreview


## Properties

Name | Type
------------ | -------------
`visualDiffId` | string
`sourceType` | string
`sourceRunId` | string
`sourceStepId` | string
`attachmentId` | string
`expectedAttachmentHash` | string
`expectedAttachmentFingerprint` | string
`mode` | string
`proposedAssertion` | [DocumentAttachmentAssertionBaseline](DocumentAttachmentAssertionBaseline.md)
`confirmed` | boolean
`status` | string
`message` | string

## Example

```typescript
import type { DocumentVisualDiffBaselinePreview } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "visualDiffId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "sourceType": null,
  "sourceRunId": null,
  "sourceStepId": null,
  "attachmentId": null,
  "expectedAttachmentHash": null,
  "expectedAttachmentFingerprint": null,
  "mode": null,
  "proposedAssertion": null,
  "confirmed": null,
  "status": null,
  "message": null,
} satisfies DocumentVisualDiffBaselinePreview

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentVisualDiffBaselinePreview
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


