
# RequestNode


## Properties

Name | Type
------------ | -------------
`name` | string
`type` | string
`parentNodeId` | string
`orderIndex` | number
`request` | [SavedRequestInput](SavedRequestInput.md)
`id` | string
`createdAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { RequestNode } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "type": null,
  "parentNodeId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "orderIndex": null,
  "request": null,
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "createdAt": null,
  "updatedAt": null,
} satisfies RequestNode

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RequestNode
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


