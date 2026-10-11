
# ArtifactGenerationProfileEnvironment


## Properties

Name | Type
------------ | -------------
`environmentKey` | string
`resolutionMode` | string
`baseUrlMode` | [AtfBaseUrlMode](AtfBaseUrlMode.md)
`baseUrlVariableName` | string
`snapshotBundleHash` | string
`snapshotAt` | Date
`cachedBundleHash` | string
`cachedAt` | Date

## Example

```typescript
import type { ArtifactGenerationProfileEnvironment } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "environmentKey": null,
  "resolutionMode": null,
  "baseUrlMode": null,
  "baseUrlVariableName": null,
  "snapshotBundleHash": null,
  "snapshotAt": null,
  "cachedBundleHash": null,
  "cachedAt": null,
} satisfies ArtifactGenerationProfileEnvironment

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactGenerationProfileEnvironment
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
