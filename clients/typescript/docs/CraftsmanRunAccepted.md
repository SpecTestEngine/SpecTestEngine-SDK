
# CraftsmanRunAccepted


## Properties

Name | Type
------------ | -------------
`runId` | string
`state` | [CraftsmanRunState](CraftsmanRunState.md)

## Example

```typescript
import type { CraftsmanRunAccepted } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "runId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "state": null,
} satisfies CraftsmanRunAccepted

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CraftsmanRunAccepted
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


