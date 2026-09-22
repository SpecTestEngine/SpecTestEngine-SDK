
# SpecificationRecoveryPreview


## Properties

Name | Type
------------ | -------------
`specId` | string
`specName` | string
`specType` | [SpecType](SpecType.md)
`currentSpec` | { [key: string]: any; }
`recoveredSpec` | { [key: string]: any; }
`currentRawSpec` | string
`recoveredRawSpec` | string
`sourceRunId` | string
`sourceRunStatus` | string
`changes` | [Array&lt;SpecificationRecoveryChange&gt;](SpecificationRecoveryChange.md)

## Example

```typescript
import type { SpecificationRecoveryPreview } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "specId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "specName": null,
  "specType": null,
  "currentSpec": null,
  "recoveredSpec": null,
  "currentRawSpec": null,
  "recoveredRawSpec": null,
  "sourceRunId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "sourceRunStatus": null,
  "changes": null,
} satisfies SpecificationRecoveryPreview

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SpecificationRecoveryPreview
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


