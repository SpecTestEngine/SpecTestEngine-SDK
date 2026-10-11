
# BrowserMacroStepInput


## Properties

Name | Type
------------ | -------------
`orderIndex` | number
`actionType` | [BrowserActionType](BrowserActionType.md)
`selector` | string
`selectorCandidates` | Array&lt;string&gt;
`value` | string
`sensitive` | boolean
`timeoutMs` | number
`tabAlias` | string
`frameSelector` | string
`variableName` | string
`pattern` | string
`extractionHint` | string
`textSource` | string
`expectedPageUrl` | string
`expectedPageUrlPolicy` | string
`expectedPageTitle` | string
`expectedPageTitlePolicy` | string
`expectedNetworkPolicy` | string
`expectedNetworkCalls` | [Array&lt;BrowserNetworkExpectation&gt;](BrowserNetworkExpectation.md)
`visualAssertion` | [BrowserVisualAssertionInput](BrowserVisualAssertionInput.md)
`pageId` | string

## Example

```typescript
import type { BrowserMacroStepInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "orderIndex": null,
  "actionType": null,
  "selector": null,
  "selectorCandidates": null,
  "value": null,
  "sensitive": null,
  "timeoutMs": null,
  "tabAlias": null,
  "frameSelector": null,
  "variableName": null,
  "pattern": null,
  "extractionHint": null,
  "textSource": null,
  "expectedPageUrl": null,
  "expectedPageUrlPolicy": null,
  "expectedPageTitle": null,
  "expectedPageTitlePolicy": null,
  "expectedNetworkPolicy": null,
  "expectedNetworkCalls": null,
  "visualAssertion": null,
  "pageId": null,
} satisfies BrowserMacroStepInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserMacroStepInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
