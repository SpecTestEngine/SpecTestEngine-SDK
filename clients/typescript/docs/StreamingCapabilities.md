
# StreamingCapabilities


## Properties

Name | Type
------------ | -------------
`engine` | string
`storage` | string
`formats` | Array&lt;string&gt;
`transports` | [Array&lt;StreamingTransport&gt;](StreamingTransport.md)
`schemes` | { [key: string]: Array&lt;string&gt;; }
`codecs` | Array&lt;string&gt;
`actions` | Array&lt;string&gt;
`eventAssertionFields` | Array&lt;string&gt;
`limits` | [StreamingLimits](StreamingLimits.md)

## Example

```typescript
import type { StreamingCapabilities } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "engine": null,
  "storage": null,
  "formats": null,
  "transports": null,
  "schemes": null,
  "codecs": null,
  "actions": null,
  "eventAssertionFields": null,
  "limits": null,
} satisfies StreamingCapabilities

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StreamingCapabilities
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


