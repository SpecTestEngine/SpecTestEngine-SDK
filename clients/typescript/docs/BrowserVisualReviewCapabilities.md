
# BrowserVisualReviewCapabilities


## Properties

Name | Type
------------ | -------------
`useCurrentAsNewBaseline` | [BrowserVisualReviewCapability](BrowserVisualReviewCapability.md)
`excludeAreaAndRecompare` | [BrowserVisualReviewCapability](BrowserVisualReviewCapability.md)
`keepAsRegression` | [BrowserVisualReviewCapability](BrowserVisualReviewCapability.md)

## Example

```typescript
import type { BrowserVisualReviewCapabilities } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "useCurrentAsNewBaseline": null,
  "excludeAreaAndRecompare": null,
  "keepAsRegression": null,
} satisfies BrowserVisualReviewCapabilities

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserVisualReviewCapabilities
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
