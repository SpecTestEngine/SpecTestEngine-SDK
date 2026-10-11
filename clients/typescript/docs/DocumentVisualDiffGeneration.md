
# DocumentVisualDiffGeneration


## Properties

Name | Type
------------ | -------------
`generationId` | string
`generationNumber` | number
`expectedSha256` | string
`colorThreshold` | number
`totalPages` | number
`changedPages` | number
`diffPixels` | number
`diffPixelRatio` | number
`createdAt` | Date
`expiresAt` | Date
`excludedRegions` | [Array&lt;DocumentVisualExcludedRegion&gt;](DocumentVisualExcludedRegion.md)
`changedExcludedRegionIndexes` | Set&lt;number&gt;
`pages` | [Array&lt;DocumentVisualDiffPage&gt;](DocumentVisualDiffPage.md)

## Example

```typescript
import type { DocumentVisualDiffGeneration } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "generationId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "generationNumber": null,
  "expectedSha256": null,
  "colorThreshold": null,
  "totalPages": null,
  "changedPages": null,
  "diffPixels": null,
  "diffPixelRatio": null,
  "createdAt": null,
  "expiresAt": null,
  "excludedRegions": null,
  "changedExcludedRegionIndexes": null,
  "pages": null,
} satisfies DocumentVisualDiffGeneration

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentVisualDiffGeneration
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
