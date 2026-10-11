
# StreamingSpecification


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`specType` | string
`transport` | [StreamingTransport](StreamingTransport.md)
`endpoint` | string
`codec` | string
`createdAt` | Date
`updatedAt` | Date
`lastRunAt` | Date
`lastRunStatus` | string
`stableKey` | string
`format` | string
`rawSpec` | string
`spec` | { [key: string]: any; }
`definitionHash` | string

## Example

```typescript
import type { StreamingSpecification } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "name": null,
  "description": null,
  "specType": null,
  "transport": null,
  "endpoint": wss://stream.example.test/events,
  "codec": null,
  "createdAt": null,
  "updatedAt": null,
  "lastRunAt": null,
  "lastRunStatus": null,
  "stableKey": null,
  "format": null,
  "rawSpec": null,
  "spec": null,
  "definitionHash": null,
} satisfies StreamingSpecification

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StreamingSpecification
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
