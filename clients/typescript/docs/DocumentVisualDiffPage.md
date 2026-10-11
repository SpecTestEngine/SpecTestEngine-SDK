
# DocumentVisualDiffPage


## Properties

Name | Type
------------ | -------------
`pageNumber` | number
`actualArtifactId` | string
`expectedArtifactId` | string
`diffArtifactId` | string
`width` | number
`height` | number

## Example

```typescript
import type { DocumentVisualDiffPage } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "pageNumber": null,
  "actualArtifactId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "expectedArtifactId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "diffArtifactId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "width": null,
  "height": null,
} satisfies DocumentVisualDiffPage

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentVisualDiffPage
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
