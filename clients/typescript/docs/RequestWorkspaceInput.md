
# RequestWorkspaceInput


## Properties

Name | Type
------------ | -------------
`name` | string
`description` | string
`variables` | { [key: string]: string; }
`globalVariableFallbacks` | { [key: string]: string; }

## Example

```typescript
import type { RequestWorkspaceInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "description": null,
  "variables": null,
  "globalVariableFallbacks": null,
} satisfies RequestWorkspaceInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as RequestWorkspaceInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


