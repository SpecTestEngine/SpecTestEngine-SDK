
# ArtifactGenerationProfileInput


## Properties

Name | Type
------------ | -------------
`revision` | number
`name` | string
`description` | string
`artifactType` | string
`selection` | [ArtifactSelection](ArtifactSelection.md)
`atf` | [AtfProjectConfig](AtfProjectConfig.md)
`environments` | [Array&lt;ArtifactGenerationProfileEnvironmentInput&gt;](ArtifactGenerationProfileEnvironmentInput.md)

## Example

```typescript
import type { ArtifactGenerationProfileInput } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "revision": null,
  "name": null,
  "description": null,
  "artifactType": null,
  "selection": null,
  "atf": null,
  "environments": null,
} satisfies ArtifactGenerationProfileInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactGenerationProfileInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


