
# RequestWorkspace


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`variables` | { [key: string]: string; }
`globalVariableFallbacks` | { [key: string]: string; }
`id` | string
`nodes` | [Array&lt;RequestNode&gt;](RequestNode.md)
`createdAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { RequestWorkspace } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "variables": null,
  "globalVariableFallbacks": null,
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "nodes": null,
  "createdAt": null,
  "updatedAt": null,
} satisfies RequestWorkspace

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RequestWorkspace
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
