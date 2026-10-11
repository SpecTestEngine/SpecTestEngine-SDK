
# DocumentAssetReference


## Properties

Name | Type
------------ | -------------
`assetId` | string
`fileName` | string
`contentType` | string
`sizeBytes` | number
`sha256` | string
`objectKey` | string
`fieldName` | string
`contentId` | string

## Example

```typescript
import type { DocumentAssetReference } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "assetId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "fileName": null,
  "contentType": null,
  "sizeBytes": null,
  "sha256": null,
  "objectKey": null,
  "fieldName": null,
  "contentId": null,
} satisfies DocumentAssetReference

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentAssetReference
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
