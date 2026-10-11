
# DocumentVisualAssertion

Persistent masked-render assertion. Protocol engines contact Browser Engine only when excludedRegions is non-empty and the local attachment hash or fingerprint failed.

## Properties

Name | Type
------------ | -------------
`version` | number
`algorithm` | string
`renderProfile` | string
`pages` | [Array&lt;DocumentVisualAssertionPage&gt;](DocumentVisualAssertionPage.md)
`excludedRegions` | [Array&lt;DocumentVisualExcludedRegion&gt;](DocumentVisualExcludedRegion.md)

## Example

```typescript
import type { DocumentVisualAssertion } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "version": null,
  "algorithm": null,
  "renderProfile": null,
  "pages": null,
  "excludedRegions": null,
} satisfies DocumentVisualAssertion

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentVisualAssertion
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
