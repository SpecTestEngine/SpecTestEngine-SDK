
# PreparationPage


## Properties

Name | Type
------------ | -------------
`items` | [Array&lt;PreparationSummary&gt;](PreparationSummary.md)
`page` | number
`size` | number
`totalElements` | number
`totalPages` | number
`first` | boolean
`last` | boolean

## Example

```typescript
import type { PreparationPage } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "items": null,
  "page": null,
  "size": null,
  "totalElements": null,
  "totalPages": null,
  "first": null,
  "last": null,
} satisfies PreparationPage

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PreparationPage
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)
