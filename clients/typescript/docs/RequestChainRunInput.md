
# RequestChainRunInput


## Properties

Name | Type
------------ | -------------
`overrideValues` | { [key: string]: any; }
`globalVariables` | { [key: string]: string; }
`globalVariableFallbacks` | { [key: string]: string; }
`draftRequest` | [SavedRequestInput](SavedRequestInput.md)

## Example

```typescript
import type { RequestChainRunInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "overrideValues": null,
  "globalVariables": null,
  "globalVariableFallbacks": null,
  "draftRequest": null,
} satisfies RequestChainRunInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RequestChainRunInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
