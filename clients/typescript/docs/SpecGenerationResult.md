
# SpecGenerationResult


## Properties

Name | Type
------------ | -------------
`specGenerationType` | string
`generatedSpec` | { [key: string]: any; }

## Example

```typescript
import type { SpecGenerationResult } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "specGenerationType": null,
  "generatedSpec": null,
} satisfies SpecGenerationResult

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SpecGenerationResult
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
