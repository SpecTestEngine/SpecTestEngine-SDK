
# DocumentAttachmentAssertionBaseline


## Properties

Name | Type
------------ | -------------
`id` | string
`expectedAttachmentHash` | string
`visualAssertion` | [DocumentVisualAssertion](DocumentVisualAssertion.md)

## Example

```typescript
import type { DocumentAttachmentAssertionBaseline } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "expectedAttachmentHash": null,
  "visualAssertion": null,
} satisfies DocumentAttachmentAssertionBaseline

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DocumentAttachmentAssertionBaseline
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
