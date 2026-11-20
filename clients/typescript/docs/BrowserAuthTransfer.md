
# BrowserAuthTransfer

Metadata only. Initial sources are Action-bound; renewal sources are run-bound and require an exact current-run private input. No token values or public initial-variable seeds are accepted. Resolve Recorder ambiguity before saving.

## Properties

Name | Type
------------ | -------------
`sources` | [Array&lt;BrowserAuthSource&gt;](BrowserAuthSource.md)
`authorizationVariable` | string
`candidates` | Array&lt;any&gt;
`optionalRefresh` | boolean
`choiceId` | string

## Example

```typescript
import type { BrowserAuthTransfer } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "sources": null,
  "authorizationVariable": null,
  "candidates": null,
  "optionalRefresh": null,
  "choiceId": null,
} satisfies BrowserAuthTransfer

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BrowserAuthTransfer
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
