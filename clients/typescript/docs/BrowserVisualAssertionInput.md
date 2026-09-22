
# BrowserVisualAssertionInput

Saved visual assertion. The existing Java comparator and thresholds are unchanged. Baseline images are raw captures, never WebRTC video frames. Omitted exclusions mean an empty list.

## Properties

Name | Type
------------ | -------------
`enabled` | boolean
`name` | string
`scopeType` | [BrowserVisualScopeType](BrowserVisualScopeType.md)
`compareMode` | [BrowserVisualCompareMode](BrowserVisualCompareMode.md)
`stopPolicy` | [BrowserVisualStopPolicy](BrowserVisualStopPolicy.md)
`maxDiffPixels` | number
`maxDiffPixelRatio` | number
`colorThreshold` | number
`moveTolerancePx` | number
`bounds` | [BrowserVisualBounds](BrowserVisualBounds.md)
`excludedRegions` | [Array&lt;BrowserVisualExcludedRegion&gt;](BrowserVisualExcludedRegion.md)
`baselineScreenshotBase64` | string
`baselineSemanticJson` | string

## Example

```typescript
import type { BrowserVisualAssertionInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "enabled": null,
  "name": null,
  "scopeType": null,
  "compareMode": null,
  "stopPolicy": null,
  "maxDiffPixels": null,
  "maxDiffPixelRatio": null,
  "colorThreshold": null,
  "moveTolerancePx": null,
  "bounds": null,
  "excludedRegions": null,
  "baselineScreenshotBase64": null,
  "baselineSemanticJson": null,
} satisfies BrowserVisualAssertionInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserVisualAssertionInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


