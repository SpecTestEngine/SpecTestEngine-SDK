
# Fragment


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`specType` | [SpecType](SpecType.md)
`streamingTransport` | [StreamingTransport](StreamingTransport.md)
`type` | [FragmentType](FragmentType.md)
`content` | { [key: string]: any; }
`fragmentId` | string
`createdAt` | Date

## Example

```typescript
import type { Fragment } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "specType": null,
  "streamingTransport": null,
  "type": null,
  "content": null,
  "fragmentId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "createdAt": null,
} satisfies Fragment

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Fragment
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
