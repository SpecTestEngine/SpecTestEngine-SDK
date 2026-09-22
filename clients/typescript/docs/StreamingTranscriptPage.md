
# StreamingTranscriptPage


## Properties

Name | Type
------------ | -------------
`runId` | string
`events` | Array&lt;{ [key: string]: any; }&gt;
`page` | number
`size` | number
`totalElements` | number
`totalPages` | number
`complete` | boolean

## Example

```typescript
import type { StreamingTranscriptPage } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "runId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "events": null,
  "page": null,
  "size": null,
  "totalElements": null,
  "totalPages": null,
  "complete": null,
} satisfies StreamingTranscriptPage

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StreamingTranscriptPage
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


