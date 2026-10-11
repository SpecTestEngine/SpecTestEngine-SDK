
# StreamingDefinitionStream


## Properties

Name | Type
------------ | -------------
`transport` | [StreamingTransport](StreamingTransport.md)
`endpoint` | string
`connection` | { [key: string]: any; }
`steps` | Array&lt;{ [key: string]: any; }&gt;

## Example

```typescript
import type { StreamingDefinitionStream } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "transport": null,
  "endpoint": null,
  "connection": null,
  "steps": null,
} satisfies StreamingDefinitionStream

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StreamingDefinitionStream
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
