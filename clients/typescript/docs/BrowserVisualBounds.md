
# BrowserVisualBounds

Normalized capture rectangle in page coordinates for REGION scope. Excluded regions are relative to the resulting cropped canvas, not to these page coordinates.

## Properties

Name | Type
------------ | -------------
`leftRatio` | number
`topRatio` | number
`widthRatio` | number
`heightRatio` | number

## Example

```typescript
import type { BrowserVisualBounds } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "leftRatio": null,
  "topRatio": null,
  "widthRatio": null,
  "heightRatio": null,
} satisfies BrowserVisualBounds

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserVisualBounds
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


