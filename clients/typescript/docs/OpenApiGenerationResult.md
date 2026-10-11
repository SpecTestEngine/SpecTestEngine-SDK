
# OpenApiGenerationResult


## Properties

Name | Type
------------ | -------------
`openApiUrl` | string
`generatedSpecsCount` | number
`generatedSpecs` | Array&lt;{ [key: string]: any; }&gt;
`includeNegativeTests` | boolean
`generateFlowScenarios` | boolean
`generatedFlowScenariosCount` | number
`generatedFlowScenarios` | [Array&lt;FlowInput&gt;](FlowInput.md)
`coverage` | { [key: string]: any; }

## Example

```typescript
import type { OpenApiGenerationResult } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "openApiUrl": null,
  "generatedSpecsCount": null,
  "generatedSpecs": null,
  "includeNegativeTests": null,
  "generateFlowScenarios": null,
  "generatedFlowScenariosCount": null,
  "generatedFlowScenarios": null,
  "coverage": null,
} satisfies OpenApiGenerationResult

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OpenApiGenerationResult
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
