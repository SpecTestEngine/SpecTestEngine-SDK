
# BrowserVisualExcludedRegion

Normalized rectangle relative to the active PAGE, ELEMENT, or REGION comparison canvas. Exclusions apply before pixel, SSIM, changed-region and scoped semantic comparison; URL, title, and network checks remain active. Overlaps are valid. Right/bottom overflow is clipped without moving the origin; a rectangle without in-canvas area is rejected.

## Properties

Name | Type
------------ | -------------
`xRatio` | number
`yRatio` | number
`widthRatio` | number
`heightRatio` | number
`reason` | string

## Example

```typescript
import type { BrowserVisualExcludedRegion } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "xRatio": null,
  "yRatio": null,
  "widthRatio": null,
  "heightRatio": null,
  "reason": null,
} satisfies BrowserVisualExcludedRegion

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserVisualExcludedRegion
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


