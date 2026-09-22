
# Specification


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`specType` | [SpecType](SpecType.md)
`method` | string
`url` | string
`updatedAt` | Date
`createdAt` | Date
`lastRunAt` | Date
`lastRunStatus` | string
`stableKey` | string
`format` | [ContentFormat](ContentFormat.md)
`rawSpec` | string
`spec` | { [key: string]: any; }

## Example

```typescript
import type { Specification } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "name": null,
  "description": null,
  "specType": null,
  "method": null,
  "url": null,
  "updatedAt": null,
  "createdAt": null,
  "lastRunAt": null,
  "lastRunStatus": null,
  "stableKey": null,
  "format": null,
  "rawSpec": null,
  "spec": null,
} satisfies Specification

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Specification
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


