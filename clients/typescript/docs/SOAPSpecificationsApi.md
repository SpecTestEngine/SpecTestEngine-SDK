# SOAPSpecificationsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureSoapSpecificationAttachmentVisualDiff**](SOAPSpecificationsApi.md#capturesoapspecificationattachmentvisualdiff) | **POST** /test/soap-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed SOAP attachment assertion |
| [**createSoapSpecification**](SOAPSpecificationsApi.md#createsoapspecification) | **POST** /test/soap-spec/create | Create a SOAP specification |
| [**deleteSoapSpecification**](SOAPSpecificationsApi.md#deletesoapspecification) | **DELETE** /test/soap-spec/by-id | Delete a SOAP specification |
| [**getSoapSpecification**](SOAPSpecificationsApi.md#getsoapspecification) | **GET** /test/soap-spec/by-id | Get a SOAP specification |
| [**getSoapSpecificationRun**](SOAPSpecificationsApi.md#getsoapspecificationrun) | **GET** /test/soap-spec/run/history/by-run-id/{runId} | Get saved SOAP run evidence |
| [**listSoapSpecificationRuns**](SOAPSpecificationsApi.md#listsoapspecificationruns) | **GET** /test/soap-spec/run/page/by-spec-id/{specId} | List saved SOAP runs |
| [**listSoapSpecifications**](SOAPSpecificationsApi.md#listsoapspecifications) | **GET** /test/soap-spec/page | List SOAP specifications |
| [**previewSoapSpecificationRecovery**](SOAPSpecificationsApi.md#previewsoapspecificationrecovery) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a SOAP specification version |
| [**restoreSoapSpecificationFromRun**](SOAPSpecificationsApi.md#restoresoapspecificationfromrun) | **PUT** /test/soap-spec/recovery/{specId}/from-run/{runId}/restore | Restore a SOAP specification version |
| [**runSoapSpecification**](SOAPSpecificationsApi.md#runsoapspecification) | **POST** /test/soap-spec/run/by-id | Run a saved SOAP specification |
| [**testSoapSpecificationRecoveryVersion**](SOAPSpecificationsApi.md#testsoapspecificationrecoveryversion) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous SOAP specification version |
| [**updateSoapSpecification**](SOAPSpecificationsApi.md#updatesoapspecification) | **PUT** /test/soap-spec/by-id | Replace a SOAP specification definition |



## captureSoapSpecificationAttachmentVisualDiff

> SpecificationRun captureSoapSpecificationAttachmentVisualDiff(specId, documentVisualDiffCaptureRunRequest)

Create a visual diff from a failed SOAP attachment assertion

Explicitly reruns the saved SOAP specification and temporarily captures one failed PDF or image response. The attachment assertion and run keep their real failed status.

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { CaptureSoapSpecificationAttachmentVisualDiffRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // DocumentVisualDiffCaptureRunRequest
    documentVisualDiffCaptureRunRequest: ...,
  } satisfies CaptureSoapSpecificationAttachmentVisualDiffRequest;

  try {
    const data = await api.captureSoapSpecificationAttachmentVisualDiff(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **documentVisualDiffCaptureRunRequest** | [DocumentVisualDiffCaptureRunRequest](DocumentVisualDiffCaptureRunRequest.md) |  | |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete failed run evidence containing the temporary visual diff link. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createSoapSpecification

> Specification createSoapSpecification(specName, body, description, idempotencyKey)

Create a SOAP specification

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { CreateSoapSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | User-facing specification name within the active project.
    specName: specName_example,
    // string
    body: body_example,
    // string | Optional user-facing description stored with the asset. (optional)
    description: description_example,
    // string | A caller-generated UUID retained for safe write retries where supported. (optional)
    idempotencyKey: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies CreateSoapSpecificationRequest;

  try {
    const data = await api.createSoapSpecification(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specName** | `string` | User-facing specification name within the active project. | [Defaults to `undefined`] |
| **body** | `string` |  | |
| **description** | `string` | Optional user-facing description stored with the asset. | [Optional] [Defaults to `undefined`] |
| **idempotencyKey** | `string` | A caller-generated UUID retained for safe write retries where supported. | [Optional] [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored SOAP specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteSoapSpecification

> Specification deleteSoapSpecification(specId)

Delete a SOAP specification

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { DeleteSoapSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteSoapSpecificationRequest;

  try {
    const data = await api.deleteSoapSpecification(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted SOAP specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSoapSpecification

> Specification getSoapSpecification(specId)

Get a SOAP specification

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetSoapSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetSoapSpecificationRequest;

  try {
    const data = await api.getSoapSpecification(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested SOAP specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSoapSpecificationRun

> SpecificationRun getSoapSpecificationRun(runId)

Get saved SOAP run evidence

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { GetSoapSpecificationRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetSoapSpecificationRunRequest;

  try {
    const data = await api.getSoapSpecificationRun(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **runId** | `string` | UUIDv7 identifier of the stored run evidence. | [Defaults to `undefined`] |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete saved run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSoapSpecificationRuns

> SpecificationRunPage listSoapSpecificationRuns(specId, page, size)

List saved SOAP runs

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListSoapSpecificationRunsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
  } satisfies ListSoapSpecificationRunsRequest;

  try {
    const data = await api.listSoapSpecificationRuns(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |

### Return type

[**SpecificationRunPage**](SpecificationRunPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of run summaries. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSoapSpecifications

> SpecificationPage listSoapSpecifications(page, size, search)

List SOAP specifications

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { ListSoapSpecificationsRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // number | Zero-based page index. (optional)
    page: 56,
    // number | Maximum number of results returned in one page. (optional)
    size: 56,
    // string | Case-insensitive server-side search within the active project. (optional)
    search: search_example,
  } satisfies ListSoapSpecificationsRequest;

  try {
    const data = await api.listSoapSpecifications(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | `number` | Zero-based page index. | [Optional] [Defaults to `0`] |
| **size** | `number` | Maximum number of results returned in one page. | [Optional] [Defaults to `20`] |
| **search** | `string` | Case-insensitive server-side search within the active project. | [Optional] [Defaults to `undefined`] |

### Return type

[**SpecificationPage**](SpecificationPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of SOAP specifications. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## previewSoapSpecificationRecovery

> SpecificationRecoveryPreview previewSoapSpecificationRecovery(specId, runId)

Preview restoring a SOAP specification version

Compares the current specification with the exact DSL snapshot retained by a completed PASS or FAIL run. No expectations are regenerated.

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { PreviewSoapSpecificationRecoveryRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies PreviewSoapSpecificationRecoveryRequest;

  try {
    const data = await api.previewSoapSpecificationRecovery(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **runId** | `string` | UUIDv7 identifier of the stored run evidence. | [Defaults to `undefined`] |

### Return type

[**SpecificationRecoveryPreview**](SpecificationRecoveryPreview.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Definition-only recovery preview. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## restoreSoapSpecificationFromRun

> Specification restoreSoapSpecificationFromRun(specId, runId)

Restore a SOAP specification version

Replaces only the current DSL content with the exact snapshot retained by a completed PASS or FAIL run. The specification id, name, description, and stable identity are preserved.

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { RestoreSoapSpecificationFromRunRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RestoreSoapSpecificationFromRunRequest;

  try {
    const data = await api.restoreSoapSpecificationFromRun(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **runId** | `string` | UUIDv7 identifier of the stored run evidence. | [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restored specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## runSoapSpecification

> SpecificationRun runSoapSpecification(specId)

Run a saved SOAP specification

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { RunSoapSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies RunSoapSpecificationRequest;

  try {
    const data = await api.runSoapSpecification(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete run evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## testSoapSpecificationRecoveryVersion

> SpecificationRun testSoapSpecificationRecoveryVersion(specId, runId)

Test a previous SOAP specification version

Executes the exact DSL snapshot retained by the selected completed PASS or FAIL run against the current API without changing the saved specification.

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { TestSoapSpecificationRecoveryVersionRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | UUIDv7 identifier of the stored run evidence.
    runId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies TestSoapSpecificationRecoveryVersionRequest;

  try {
    const data = await api.testSoapSpecificationRecoveryVersion(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **runId** | `string` | UUIDv7 identifier of the stored run evidence. | [Defaults to `undefined`] |

### Return type

[**SpecificationRun**](SpecificationRun.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Complete test-run evidence for the selected version. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateSoapSpecification

> Specification updateSoapSpecification(specId, body, description)

Replace a SOAP specification definition

### Example

```ts
import {
  Configuration,
  SOAPSpecificationsApi,
} from '@spectestengine/sdk';
import type { UpdateSoapSpecificationRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new SOAPSpecificationsApi(config);

  const body = {
    // string | UUIDv7 identifier of the saved specification.
    specId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string
    body: body_example,
    // string | Optional user-facing description stored with the asset. (optional)
    description: description_example,
  } satisfies UpdateSoapSpecificationRequest;

  try {
    const data = await api.updateSoapSpecification(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **specId** | `string` | UUIDv7 identifier of the saved specification. | [Defaults to `undefined`] |
| **body** | `string` |  | |
| **description** | `string` | Optional user-facing description stored with the asset. | [Optional] [Defaults to `undefined`] |

### Return type

[**Specification**](Specification.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated SOAP specification. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

