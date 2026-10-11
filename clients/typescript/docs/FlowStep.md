
# FlowStep


## Properties

Name | Type
------------ | -------------
`stepId` | string
`orderIndex` | number
`flowName` | string
`stepType` | string
`specId` | string
`specType` | [SpecType](SpecType.md)
`specName` | string
`uiMacroId` | string
`uiMacroName` | string
`browserActionType` | [BrowserActionType](BrowserActionType.md)
`selector` | string
`selectorCandidates` | Array&lt;string&gt;
`value` | string
`variableName` | string
`tabAlias` | string
`frameSelector` | string
`pattern` | string
`extractionHint` | string
`textSource` | string
`expectedPageUrl` | string
`expectedPageUrlPolicy` | string
`expectedPageTitle` | string
`expectedPageTitlePolicy` | string
`expectedNetworkPolicy` | string
`visualAssertion` | [BrowserVisualAssertion](BrowserVisualAssertion.md)
`expectedNetworkCalls` | [Array&lt;BrowserNetworkExpectation&gt;](BrowserNetworkExpectation.md)
`storeValues` | { [key: string]: string; }
`overrideValues` | { [key: string]: any; }

## Example

```typescript
import type { FlowStep } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "stepId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "orderIndex": null,
  "flowName": null,
  "stepType": null,
  "specId": null,
  "specType": null,
  "specName": null,
  "uiMacroId": null,
  "uiMacroName": null,
  "browserActionType": null,
  "selector": null,
  "selectorCandidates": null,
  "value": null,
  "variableName": null,
  "tabAlias": null,
  "frameSelector": null,
  "pattern": null,
  "extractionHint": null,
  "textSource": null,
  "expectedPageUrl": null,
  "expectedPageUrlPolicy": null,
  "expectedPageTitle": null,
  "expectedPageTitlePolicy": null,
  "expectedNetworkPolicy": null,
  "visualAssertion": null,
  "expectedNetworkCalls": null,
  "storeValues": null,
  "overrideValues": null,
} satisfies FlowStep

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowStep
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
