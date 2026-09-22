
# StreamingLimits


## Properties

Name | Type
------------ | -------------
`maxDuration` | string
`maxIdleTimeout` | string
`maxEvents` | number
`maxBytes` | number
`maxEventBytes` | number
`maxConcurrentRunsPerCompany` | number

## Example

```typescript
import type { StreamingLimits } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "maxDuration": PT5M,
  "maxIdleTimeout": PT1M,
  "maxEvents": null,
  "maxBytes": null,
  "maxEventBytes": null,
  "maxConcurrentRunsPerCompany": null,
} satisfies StreamingLimits

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as StreamingLimits
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


