
# FlowRunStep


## Properties

Name | Type
------------ | -------------
`stepId` | string
`orderIndex` | number
`stepType` | string
`specName` | string
`uiMacroId` | string
`uiMacroName` | string
`uiMacroRunId` | string
`browserActionType` | [BrowserActionType](BrowserActionType.md)
`selector` | string
`value` | string
`variableName` | string
`browserPageUrl` | string
`browserPageTitle` | string
`browserFailureCode` | string
`browserFailureMessage` | string
`visualComparison` | [BrowserVisualComparisonSummary](BrowserVisualComparisonSummary.md)
`stepStatus` | string
`uiMacroFailureCode` | string
`uiMacroFailureMessage` | string
`testStepRun` | { [key: string]: any; }

## Example

```typescript
import type { FlowRunStep } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "stepId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "orderIndex": null,
  "stepType": null,
  "specName": null,
  "uiMacroId": null,
  "uiMacroName": null,
  "uiMacroRunId": null,
  "browserActionType": null,
  "selector": null,
  "value": null,
  "variableName": null,
  "browserPageUrl": null,
  "browserPageTitle": null,
  "browserFailureCode": null,
  "browserFailureMessage": null,
  "visualComparison": null,
  "stepStatus": null,
  "uiMacroFailureCode": null,
  "uiMacroFailureMessage": null,
  "testStepRun": null,
} satisfies FlowRunStep

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRunStep
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


