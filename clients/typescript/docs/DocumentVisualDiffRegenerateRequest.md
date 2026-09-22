
# DocumentVisualDiffRegenerateRequest


## Properties

Name | Type
------------ | -------------
`colorThreshold` | number
`excludedRegions` | [Array&lt;DocumentVisualExcludedRegion&gt;](DocumentVisualExcludedRegion.md)

## Example

```typescript
import type { DocumentVisualDiffRegenerateRequest } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "colorThreshold": null,
  "excludedRegions": null,
} satisfies DocumentVisualDiffRegenerateRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentVisualDiffRegenerateRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


