
# BrowserVisualComparisonSummary

Immutable visual evidence embedded in a Flow run or Snapshot behavior payload. Empty diagnostic/exclusion lists may be omitted. Fetch the comparison detail lazily for review capabilities.

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
`assertionRevision` | number
`baselineRevisionId` | string
`generationNumber` | number
`sourceComparisonId` | string
`rootComparisonId` | string
`excludedRegions` | [Array&lt;BrowserVisualExcludedRegion&gt;](BrowserVisualExcludedRegion.md)
`changedExcludedRegionIndexes` | Array&lt;number&gt;

## Example

```typescript
import type { BrowserVisualComparisonSummary } from '@spectestengine/sdk'

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
  "assertionRevision": null,
  "baselineRevisionId": null,
  "generationNumber": null,
  "sourceComparisonId": null,
  "rootComparisonId": null,
  "excludedRegions": null,
  "changedExcludedRegionIndexes": null,
} satisfies BrowserVisualComparisonSummary

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserVisualComparisonSummary
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


