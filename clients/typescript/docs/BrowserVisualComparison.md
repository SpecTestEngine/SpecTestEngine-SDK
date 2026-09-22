
# BrowserVisualComparison

Immutable visual comparison generation. Baseline promotion creates a new baseline revision; it never deletes evidence referenced by older comparisons or snapshots.

## Properties

Name | Type
------------ | -------------
`comparisonId` | string
`status` | [BrowserVisualComparisonStatus](BrowserVisualComparisonStatus.md)
`decisionStatus` | [BrowserVisualDecisionStatus](BrowserVisualDecisionStatus.md)
`scopeType` | [BrowserVisualScopeType](BrowserVisualScopeType.md)
`compareMode` | [BrowserVisualCompareMode](BrowserVisualCompareMode.md)
`stopPolicy` | [BrowserVisualStopPolicy](BrowserVisualStopPolicy.md)
`baselineArtifactId` | string
`actualArtifactId` | string
`diffArtifactId` | string
`diffPixels` | number
`diffPixelRatio` | number
`message` | string
`changedDetails` | Array&lt;string&gt;
`changedRegions` | [Array&lt;BrowserVisualDiffRegion&gt;](BrowserVisualDiffRegion.md)
`createdAt` | Date
`reviewedAt` | Date
`assertionRevision` | number
`baselineRevisionId` | string
`appliedBaselineRevisionId` | string
`generationNumber` | number
`sourceComparisonId` | string
`rootComparisonId` | string
`excludedRegions` | [Array&lt;BrowserVisualExcludedRegion&gt;](BrowserVisualExcludedRegion.md)
`changedExcludedRegionIndexes` | Set&lt;number&gt;
`reviewCapabilities` | [BrowserVisualReviewCapabilities](BrowserVisualReviewCapabilities.md)

## Example

```typescript
import type { BrowserVisualComparison } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "comparisonId": null,
  "status": null,
  "decisionStatus": null,
  "scopeType": null,
  "compareMode": null,
  "stopPolicy": null,
  "baselineArtifactId": null,
  "actualArtifactId": null,
  "diffArtifactId": null,
  "diffPixels": null,
  "diffPixelRatio": null,
  "message": null,
  "changedDetails": null,
  "changedRegions": null,
  "createdAt": null,
  "reviewedAt": null,
  "assertionRevision": null,
  "baselineRevisionId": null,
  "appliedBaselineRevisionId": null,
  "generationNumber": null,
  "sourceComparisonId": null,
  "rootComparisonId": null,
  "excludedRegions": null,
  "changedExcludedRegionIndexes": null,
  "reviewCapabilities": null,
} satisfies BrowserVisualComparison

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserVisualComparison
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


