
# BrowserSessionInput


## Properties

Name | Type
------------ | -------------
`url` | string
`viewportWidth` | number
`viewportHeight` | number
`viewportPreset` | string

## Example

```typescript
import type { BrowserSessionInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "url": null,
  "viewportWidth": null,
  "viewportHeight": null,
  "viewportPreset": null,
} satisfies BrowserSessionInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserSessionInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
