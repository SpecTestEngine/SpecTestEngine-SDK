# SpecTestEngine.Sdk.Api.SnapshotsApi

All URIs are relative to *https://app.ste.software*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CompareSnapshotStep**](SnapshotsApi.md#comparesnapshotstep) | **POST** /test/snapshot/diff/step | Compare snapshot step payloads |
| [**CompareSnapshotToRunBatch**](SnapshotsApi.md#comparesnapshottorunbatch) | **GET** /test/snapshot/diff/snapshot/{snapshotId}/batch/{batchId} | Compare a snapshot with a run batch |
| [**CompareSnapshots**](SnapshotsApi.md#comparesnapshots) | **GET** /test/snapshot/diff/snapshot/{leftSnapshotId}/snapshot/{rightSnapshotId} | Compare two snapshots |
| [**CreateSnapshot**](SnapshotsApi.md#createsnapshot) | **POST** /test/snapshot/create | Create a snapshot baseline |
| [**GetSnapshot**](SnapshotsApi.md#getsnapshot) | **GET** /test/snapshot/by-id/{snapshotId} | Get a snapshot |
| [**ListSnapshots**](SnapshotsApi.md#listsnapshots) | **GET** /test/snapshot/page | List snapshots |

<a id="comparesnapshotstep"></a>
# **CompareSnapshotStep**
> SnapshotStepDiff CompareSnapshotStep (SnapshotStepDiffInput snapshotStepDiffInput)

Compare snapshot step payloads

Produce a field-level definition and behavior diff for one API, UI macro, or browser-action step.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **snapshotStepDiffInput** | [**SnapshotStepDiffInput**](SnapshotStepDiffInput.md) |  |  |

### Return type

[**SnapshotStepDiff**](SnapshotStepDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A grouped, field-level step comparison suitable for a review UI. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="comparesnapshottorunbatch"></a>
# **CompareSnapshotToRunBatch**
> SnapshotDiff CompareSnapshotToRunBatch (Guid snapshotId, Guid batchId)

Compare a snapshot with a run batch

Compare a saved baseline with fresh run-batch evidence before promoting a new snapshot.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **snapshotId** | **Guid** | UUIDv7 identifier of the saved snapshot baseline. |  |
| **batchId** | **Guid** | UUIDv7 identifier of the saved run batch. |  |

### Return type

[**SnapshotDiff**](SnapshotDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The classified baseline-to-batch comparison. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="comparesnapshots"></a>
# **CompareSnapshots**
> SnapshotDiff CompareSnapshots (Guid leftSnapshotId, Guid rightSnapshotId)

Compare two snapshots

Compare two saved baselines and classify new, removed, regressed, improved, and stable subjects.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **leftSnapshotId** | **Guid** | UUIDv7 identifier of the baseline side of the comparison. |  |
| **rightSnapshotId** | **Guid** | UUIDv7 identifier of the candidate side of the comparison. |  |

### Return type

[**SnapshotDiff**](SnapshotDiff.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The classified snapshot comparison. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="createsnapshot"></a>
# **CreateSnapshot**
> Snapshot CreateSnapshot (SnapshotInput snapshotInput, Guid idempotencyKey = null)

Create a snapshot baseline

Promote all or a selected subset of one run batch into a versioned baseline for later regression comparison.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **snapshotInput** | [**SnapshotInput**](SnapshotInput.md) |  |  |
| **idempotencyKey** | **Guid** | A caller-generated UUID retained for safe write retries where supported. | [optional]  |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created snapshot baseline. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getsnapshot"></a>
# **GetSnapshot**
> Snapshot GetSnapshot (Guid snapshotId)

Get a snapshot


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **snapshotId** | **Guid** | UUIDv7 identifier of the saved snapshot baseline. |  |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested snapshot and its baseline evidence. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listsnapshots"></a>
# **ListSnapshots**
> SnapshotPage ListSnapshots (int page = null, int size = null, string search = null)

List snapshots


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **page** | **int** | Zero-based page index. | [optional] [default to 0] |
| **size** | **int** | Maximum number of results returned in one page. | [optional] [default to 20] |
| **search** | **string** | Case-insensitive server-side search within the active project. | [optional]  |

### Return type

[**SnapshotPage**](SnapshotPage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of snapshot baselines in the active project. |  -  |
| **0** | The request failed. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

