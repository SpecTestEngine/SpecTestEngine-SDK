
# BrowserAuthSource


## Properties

Name | Type
------------ | -------------
`name` | string
`source` | string
`path` | string
`scopeOrigin` | string
`updateFrom` | [BrowserAuthGuard](BrowserAuthGuard.md)

## Example

```typescript
import type { BrowserAuthSource } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "source": null,
  "path": null,
  "scopeOrigin": null,
  "updateFrom": null,
} satisfies BrowserAuthSource

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserAuthSource
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
