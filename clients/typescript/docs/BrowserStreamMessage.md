
# BrowserStreamMessage

Observed stream message metadata. SSE only supports INBOUND. This never sends another request.

## Properties

Name | Type
------------ | -------------
`transport` | string
`direction` | string
`eventName` | string
`binary` | boolean
`failed` | boolean

## Example

```typescript
import type { BrowserStreamMessage } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "transport": null,
  "direction": null,
  "eventName": null,
  "binary": null,
  "failed": null,
} satisfies BrowserStreamMessage

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserStreamMessage
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
