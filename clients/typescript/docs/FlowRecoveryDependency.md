
# FlowRecoveryDependency


## Properties

Name | Type
------------ | -------------
`key` | string
`kind` | string
`sourceName` | string
`format` | string
`definitionHash` | string
`roles` | Array&lt;string&gt;
`bindingCount` | number

## Example

```typescript
import type { FlowRecoveryDependency } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "key": null,
  "kind": null,
  "sourceName": null,
  "format": null,
  "definitionHash": null,
  "roles": null,
  "bindingCount": null,
} satisfies FlowRecoveryDependency

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FlowRecoveryDependency
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
