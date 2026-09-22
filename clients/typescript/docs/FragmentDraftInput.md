
# FragmentDraftInput


## Properties

Name | Type
------------ | -------------
`name` | string
`type` | [FragmentType](FragmentType.md)
`content` | { [key: string]: any; }

## Example

```typescript
import type { FragmentDraftInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "type": null,
  "content": null,
} satisfies FragmentDraftInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FragmentDraftInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


