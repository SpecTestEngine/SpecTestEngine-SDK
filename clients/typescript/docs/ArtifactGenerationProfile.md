
# ArtifactGenerationProfile


## Properties

Name | Type
------------ | -------------
`id` | string
`revision` | number
`name` | string
`description` | string
`artifactType` | string
`selection` | [ArtifactSelection](ArtifactSelection.md)
`atf` | [AtfProjectConfig](AtfProjectConfig.md)
`environments` | [Array&lt;ArtifactGenerationProfileEnvironment&gt;](ArtifactGenerationProfileEnvironment.md)
`createdAt` | Date
`updatedAt` | Date

## Example

```typescript
import type { ArtifactGenerationProfile } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "revision": null,
  "name": null,
  "description": null,
  "artifactType": null,
  "selection": null,
  "atf": null,
  "environments": null,
  "createdAt": null,
  "updatedAt": null,
} satisfies ArtifactGenerationProfile

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ArtifactGenerationProfile
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


