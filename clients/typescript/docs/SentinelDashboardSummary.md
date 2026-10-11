
# SentinelDashboardSummary


## Properties

Name | Type
------------ | -------------
`totalChecks` | number
`activeChecks` | number
`activeIncidents` | number
`runs24h` | number
`failedRuns24h` | number
`uptime24h` | number
`averageLatency24h` | number

## Example

```typescript
import type { SentinelDashboardSummary } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "totalChecks": null,
  "activeChecks": null,
  "activeIncidents": null,
  "runs24h": null,
  "failedRuns24h": null,
  "uptime24h": null,
  "averageLatency24h": null,
} satisfies SentinelDashboardSummary

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SentinelDashboardSummary
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
