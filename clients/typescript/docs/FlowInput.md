
# FlowInput


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`steps` | [Array&lt;FlowStepInput&gt;](FlowStepInput.md)
`globalVariableFallbacks` | { [key: string]: string; }
`browserSession` | [BrowserSessionInput](BrowserSessionInput.md)

## Example

```typescript
import type { FlowInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "steps": null,
  "globalVariableFallbacks": null,
  "browserSession": null,
} satisfies FlowInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


