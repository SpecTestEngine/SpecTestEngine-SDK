
# AtfGenerationResult


## Properties

Name | Type
------------ | -------------
`projectName` | string
`targetFramework` | string
`exportMode` | string
`buildTool` | string
`manifest` | { [key: string]: any; }
`files` | [Array&lt;AtfGenerationResultFilesInner&gt;](AtfGenerationResultFilesInner.md)
`notes` | Array&lt;{ [key: string]: any; }&gt;

## Example

```typescript
import type { AtfGenerationResult } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "projectName": null,
  "targetFramework": null,
  "exportMode": null,
  "buildTool": null,
  "manifest": null,
  "files": null,
  "notes": null,
} satisfies AtfGenerationResult

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AtfGenerationResult
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


