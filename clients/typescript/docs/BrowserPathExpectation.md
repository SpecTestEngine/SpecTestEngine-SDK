
# BrowserPathExpectation

Exactly one of value or pattern is required. Values retain JSON types, including explicit null. Pattern is a whole-string glob with at most 32 stars; only a star or backslash can be escaped. Runtime templates are not accepted in patterns.

## Properties

Name | Type
------------ | -------------
`path` | string
`value` | any
`pattern` | string

## Example

```typescript
import type { BrowserPathExpectation } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "path": null,
  "value": null,
  "pattern": null,
} satisfies BrowserPathExpectation

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserPathExpectation
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
