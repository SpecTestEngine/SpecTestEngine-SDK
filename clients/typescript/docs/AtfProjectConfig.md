
# AtfProjectConfig


## Properties

Name | Type
------------ | -------------
`projectName` | string
`packageName` | string
`targetFramework` | string
`exportMode` | string
`buildTool` | string
`javaVersion` | number
`baseUrlMode` | [AtfBaseUrlMode](AtfBaseUrlMode.md)
`baseUrlVariableName` | string
`includeSupportFiles` | boolean
`includeCoverage` | boolean
`ciProvider` | string
`unsupportedFeatureMode` | string

## Example

```typescript
import type { AtfProjectConfig } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "projectName": null,
  "packageName": null,
  "targetFramework": null,
  "exportMode": null,
  "buildTool": null,
  "javaVersion": null,
  "baseUrlMode": null,
  "baseUrlVariableName": null,
  "includeSupportFiles": null,
  "includeCoverage": null,
  "ciProvider": null,
  "unsupportedFeatureMode": null,
} satisfies AtfProjectConfig

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AtfProjectConfig
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


