
# FlowStepInput


## Properties

Name | Type
------------ | -------------
`stepType` | string
`orderIndex` | number
`specId` | string
`specType` | [SpecType](SpecType.md)
`specName` | string
`uiMacroId` | string
`uiMacro` | [BrowserMacroInput](BrowserMacroInput.md)
`browserAction` | [BrowserActionInput](BrowserActionInput.md)
`storeValues` | { [key: string]: string; }
`overrideValues` | { [key: string]: any; }

## Example

```typescript
import type { FlowStepInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "stepType": null,
  "orderIndex": null,
  "specId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "specType": null,
  "specName": null,
  "uiMacroId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "uiMacro": null,
  "browserAction": null,
  "storeValues": null,
  "overrideValues": null,
} satisfies FlowStepInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowStepInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
