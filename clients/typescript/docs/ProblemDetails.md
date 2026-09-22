
# ProblemDetails


## Properties

Name | Type
------------ | -------------
`timestamp` | Date
`status` | number
`error` | string
`message` | string
`path` | string
`errorCode` | string
`translationKey` | string
`requestId` | string
`violations` | Array&lt;{ [key: string]: any; }&gt;

## Example

```typescript
import type { ProblemDetails } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "timestamp": null,
  "status": null,
  "error": null,
  "message": null,
  "path": null,
  "errorCode": null,
  "translationKey": null,
  "requestId": null,
  "violations": null,
} satisfies ProblemDetails

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ProblemDetails
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


