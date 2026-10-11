
# BrowserMacroInput


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`startUrl` | string
`viewportWidth` | number
`viewportHeight` | number
`steps` | [Array&lt;BrowserMacroStepInput&gt;](BrowserMacroStepInput.md)

## Example

```typescript
import type { BrowserMacroInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "startUrl": null,
  "viewportWidth": null,
  "viewportHeight": null,
  "steps": null,
} satisfies BrowserMacroInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserMacroInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
