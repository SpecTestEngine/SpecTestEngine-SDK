
# DocumentVisualDiff


## Properties

Name | Type
------------ | -------------
`visualDiffId` | string
`viewerUrl` | string
`sourceType` | string
`sourceRunId` | string
`sourceStepId` | string
`attachmentId` | string
`actualContentType` | string
`actualSha256` | string
`expectedSha256` | string
`status` | [DocumentVisualDiffStatus](DocumentVisualDiffStatus.md)
`decision` | [DocumentVisualDiffDecision](DocumentVisualDiffDecision.md)
`actualPageCount` | number
`createdAt` | Date
`expiresAt` | Date
`actualAvailable` | boolean
`expectedUploadRequired` | boolean
`regenerateAvailable` | boolean
`generations` | [Array&lt;DocumentVisualDiffGeneration&gt;](DocumentVisualDiffGeneration.md)
`currentGeneration` | [DocumentVisualDiffGeneration](DocumentVisualDiffGeneration.md)

## Example

```typescript
import type { DocumentVisualDiff } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "visualDiffId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "viewerUrl": null,
  "sourceType": null,
  "sourceRunId": null,
  "sourceStepId": null,
  "attachmentId": null,
  "actualContentType": null,
  "actualSha256": null,
  "expectedSha256": null,
  "status": null,
  "decision": null,
  "actualPageCount": null,
  "createdAt": null,
  "expiresAt": null,
  "actualAvailable": null,
  "expectedUploadRequired": null,
  "regenerateAvailable": null,
  "generations": null,
  "currentGeneration": null,
} satisfies DocumentVisualDiff

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentVisualDiff
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
