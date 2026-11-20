
# BrowserTargetMatch

Explicit selector-first role/name policy. Only DRAG accepts a destination identity. Sensitive actions cannot use this policy.

## Properties

Name | Type
------------ | -------------
`role` | string
`name` | string
`destination` | [BrowserTargetIdentity](BrowserTargetIdentity.md)

## Example

```typescript
import type { BrowserTargetMatch } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "role": null,
  "name": null,
  "destination": null,
} satisfies BrowserTargetMatch

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserTargetMatch
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
