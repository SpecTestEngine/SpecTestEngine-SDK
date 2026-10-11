
# AtfValidationResult


## Properties

Name | Type
------------ | -------------
`projectName` | string
`exportMode` | string
`buildTool` | string
`validationPassed` | boolean
`suggestedCommand` | string
`steps` | [Array&lt;AtfValidationStep&gt;](AtfValidationStep.md)

## Example

```typescript
import type { AtfValidationResult } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "projectName": null,
  "exportMode": null,
  "buildTool": null,
  "validationPassed": null,
  "suggestedCommand": null,
  "steps": null,
} satisfies AtfValidationResult

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AtfValidationResult
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
