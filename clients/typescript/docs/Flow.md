
# Flow

Saved Flow read model. Browser action fields are flattened on each step; create/update use FlowInput with nested browserAction instead.

## Properties

Name | Type
------------ | -------------
`flowId` | string
`name` | string
`description` | string
`globalVariableFallbacks` | { [key: string]: string; }
`browserStartUrl` | string
`browserViewportWidth` | number
`browserViewportHeight` | number
`browserViewportPreset` | string
`steps` | [Array&lt;FlowStep&gt;](FlowStep.md)
`createdAt` | Date

## Example

```typescript
import type { Flow } from '@spectestengine/sdk'

// TODO: Update the object below with actual values
const example = {
  "flowId": 0197f0ab-42e7-7a31-8a9c-591a8ee54c12,
  "name": null,
  "description": null,
  "globalVariableFallbacks": null,
  "browserStartUrl": null,
  "browserViewportWidth": null,
  "browserViewportHeight": null,
  "browserViewportPreset": null,
  "steps": null,
  "createdAt": null,
} satisfies Flow

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Flow
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


