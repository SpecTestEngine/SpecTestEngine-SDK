
# StreamingDefinition

Executable SpecTestEngine-like bounded Streaming DSL.

## Properties

Name | Type
------------ | -------------
`stream` | [StreamingDefinitionStream](StreamingDefinitionStream.md)
`expectedConnection` | { [key: string]: any; }
`expectedStream` | { [key: string]: any; }
`expectedTermination` | { [key: string]: any; }
`exclusions` | Array&lt;string&gt;
`redactions` | Array&lt;string&gt;
`observationOnly` | boolean

## Example

```typescript
import type { StreamingDefinition } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "stream": null,
  "expectedConnection": null,
  "expectedStream": null,
  "expectedTermination": null,
  "exclusions": null,
  "redactions": null,
  "observationOnly": null,
} satisfies StreamingDefinition

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StreamingDefinition
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


