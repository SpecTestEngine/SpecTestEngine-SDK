
# BrowserVisualAssertion

Persisted visual definition. Revisions are server-owned; baseline bytes are fetched separately through retained artifact references.

## Properties

Name | Type
------------ | -------------
`enabled` | boolean
`name` | string
`scopeType` | [BrowserVisualScopeType](BrowserVisualScopeType.md)
`compareMode` | [BrowserVisualCompareMode](BrowserVisualCompareMode.md)
`stopPolicy` | [BrowserVisualStopPolicy](BrowserVisualStopPolicy.md)
`baselineArtifactId` | string
`baselineRevisionId` | string
`assertionRevision` | number
`maxDiffPixels` | number
`maxDiffPixelRatio` | number
`colorThreshold` | number
`moveTolerancePx` | number
`bounds` | [BrowserVisualBounds](BrowserVisualBounds.md)
`excludedRegions` | [Array&lt;BrowserVisualExcludedRegion&gt;](BrowserVisualExcludedRegion.md)

## Example

```typescript
import type { BrowserVisualAssertion } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "enabled": null,
  "name": null,
  "scopeType": null,
  "compareMode": null,
  "stopPolicy": null,
  "baselineArtifactId": null,
  "baselineRevisionId": null,
  "assertionRevision": null,
  "maxDiffPixels": null,
  "maxDiffPixelRatio": null,
  "colorThreshold": null,
  "moveTolerancePx": null,
  "bounds": null,
  "excludedRegions": null,
} satisfies BrowserVisualAssertion

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserVisualAssertion
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
