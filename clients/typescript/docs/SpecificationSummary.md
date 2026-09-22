
# SpecificationSummary


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

## Example

```typescript
import type { SpecificationSummary } from '@spectestengine/sdk'

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
} satisfies SpecificationSummary

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SpecificationSummary
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


