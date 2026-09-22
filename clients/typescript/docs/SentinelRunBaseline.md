
# SentinelRunBaseline


## Properties

Name | Type
------------ | -------------
`id` | string
`status` | [RunStatus](RunStatus.md)
`label` | string
`definitionHash` | string
`behaviorHash` | string
`responseHeadersJson` | string
`responseBodyPreview` | string
`resultLog` | string
`errorMessage` | string
`finishedAt` | Date

## Example

```typescript
import type { SentinelRunBaseline } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "status": null,
  "label": null,
  "definitionHash": null,
  "behaviorHash": null,
  "responseHeadersJson": null,
  "responseBodyPreview": null,
  "resultLog": null,
  "errorMessage": null,
  "finishedAt": null,
} satisfies SentinelRunBaseline

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SentinelRunBaseline
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


