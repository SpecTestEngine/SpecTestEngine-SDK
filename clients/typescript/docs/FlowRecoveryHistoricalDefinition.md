
# FlowRecoveryHistoricalDefinition

Read-only historical Flow, not the live Flow. Creation timestamps are not evidence of the original authoring time.

## Properties

Name | Type
------------ | -------------
`flowId` | string
`name` | string
`description` | string
`globalVariableFallbacks` | { [key: string]: string; }
`browserStartUrl` | string
`browserViewportWidth` | number
`browserViewportHeight` | number
`browserViewportPreset` | string
`steps` | [Array&lt;FlowStep&gt;](FlowStep.md)

## Example

```typescript
import type { FlowRecoveryHistoricalDefinition } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "flowId": null,
  "name": null,
  "description": null,
  "globalVariableFallbacks": null,
  "browserStartUrl": null,
  "browserViewportWidth": null,
  "browserViewportHeight": null,
  "browserViewportPreset": null,
  "steps": null,
} satisfies FlowRecoveryHistoricalDefinition

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryHistoricalDefinition
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
