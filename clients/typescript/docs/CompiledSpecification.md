
# CompiledSpecification


## Properties

Name | Type
------------ | -------------
`format` | [ContentFormat](ContentFormat.md)
`rawSpec` | string
`compiledSpec` | { [key: string]: any; }

## Example

```typescript
import type { CompiledSpecification } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "format": null,
  "rawSpec": null,
  "compiledSpec": null,
} satisfies CompiledSpecification

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CompiledSpecification
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
