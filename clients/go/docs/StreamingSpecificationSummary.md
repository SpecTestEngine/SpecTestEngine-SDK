# StreamingSpecificationSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**SpecType** | **string** |  |
**Transport** | [**StreamingTransport**](StreamingTransport.md) |  |
**Endpoint** | **string** | Streaming endpoint URI |
**Codec** | **string** |  |
**CreatedAt** | **time.Time** |  |
**UpdatedAt** | **time.Time** |  |
**LastRunAt** | Pointer to **NullableTime** |  | [optional]
**LastRunStatus** | Pointer to **NullableString** |  | [optional]

## Methods

### NewStreamingSpecificationSummary

`func NewStreamingSpecificationSummary(id string, name string, specType string, transport StreamingTransport, endpoint string, codec string, createdAt time.Time, updatedAt time.Time, ) *StreamingSpecificationSummary`

NewStreamingSpecificationSummary instantiates a new StreamingSpecificationSummary object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingSpecificationSummaryWithDefaults

`func NewStreamingSpecificationSummaryWithDefaults() *StreamingSpecificationSummary`

NewStreamingSpecificationSummaryWithDefaults instantiates a new StreamingSpecificationSummary object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *StreamingSpecificationSummary) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *StreamingSpecificationSummary) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *StreamingSpecificationSummary) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *StreamingSpecificationSummary) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *StreamingSpecificationSummary) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *StreamingSpecificationSummary) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *StreamingSpecificationSummary) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *StreamingSpecificationSummary) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *StreamingSpecificationSummary) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *StreamingSpecificationSummary) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *StreamingSpecificationSummary) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *StreamingSpecificationSummary) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSpecType

`func (o *StreamingSpecificationSummary) GetSpecType() string`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *StreamingSpecificationSummary) GetSpecTypeOk() (*string, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *StreamingSpecificationSummary) SetSpecType(v string)`

SetSpecType sets SpecType field to given value.


### GetTransport

`func (o *StreamingSpecificationSummary) GetTransport() StreamingTransport`

GetTransport returns the Transport field if non-nil, zero value otherwise.

### GetTransportOk

`func (o *StreamingSpecificationSummary) GetTransportOk() (*StreamingTransport, bool)`

GetTransportOk returns a tuple with the Transport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransport

`func (o *StreamingSpecificationSummary) SetTransport(v StreamingTransport)`

SetTransport sets Transport field to given value.


### GetEndpoint

`func (o *StreamingSpecificationSummary) GetEndpoint() string`

GetEndpoint returns the Endpoint field if non-nil, zero value otherwise.

### GetEndpointOk

`func (o *StreamingSpecificationSummary) GetEndpointOk() (*string, bool)`

GetEndpointOk returns a tuple with the Endpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndpoint

`func (o *StreamingSpecificationSummary) SetEndpoint(v string)`

SetEndpoint sets Endpoint field to given value.


### GetCodec

`func (o *StreamingSpecificationSummary) GetCodec() string`

GetCodec returns the Codec field if non-nil, zero value otherwise.

### GetCodecOk

`func (o *StreamingSpecificationSummary) GetCodecOk() (*string, bool)`

GetCodecOk returns a tuple with the Codec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodec

`func (o *StreamingSpecificationSummary) SetCodec(v string)`

SetCodec sets Codec field to given value.


### GetCreatedAt

`func (o *StreamingSpecificationSummary) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *StreamingSpecificationSummary) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *StreamingSpecificationSummary) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *StreamingSpecificationSummary) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *StreamingSpecificationSummary) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *StreamingSpecificationSummary) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetLastRunAt

`func (o *StreamingSpecificationSummary) GetLastRunAt() time.Time`

GetLastRunAt returns the LastRunAt field if non-nil, zero value otherwise.

### GetLastRunAtOk

`func (o *StreamingSpecificationSummary) GetLastRunAtOk() (*time.Time, bool)`

GetLastRunAtOk returns a tuple with the LastRunAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunAt

`func (o *StreamingSpecificationSummary) SetLastRunAt(v time.Time)`

SetLastRunAt sets LastRunAt field to given value.

### HasLastRunAt

`func (o *StreamingSpecificationSummary) HasLastRunAt() bool`

HasLastRunAt returns a boolean if a field has been set.

### SetLastRunAtNil

`func (o *StreamingSpecificationSummary) SetLastRunAtNil(b bool)`

 SetLastRunAtNil sets the value for LastRunAt to be an explicit nil

### UnsetLastRunAt
`func (o *StreamingSpecificationSummary) UnsetLastRunAt()`

UnsetLastRunAt ensures that no value is present for LastRunAt, not even an explicit nil
### GetLastRunStatus

`func (o *StreamingSpecificationSummary) GetLastRunStatus() string`

GetLastRunStatus returns the LastRunStatus field if non-nil, zero value otherwise.

### GetLastRunStatusOk

`func (o *StreamingSpecificationSummary) GetLastRunStatusOk() (*string, bool)`

GetLastRunStatusOk returns a tuple with the LastRunStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunStatus

`func (o *StreamingSpecificationSummary) SetLastRunStatus(v string)`

SetLastRunStatus sets LastRunStatus field to given value.

### HasLastRunStatus

`func (o *StreamingSpecificationSummary) HasLastRunStatus() bool`

HasLastRunStatus returns a boolean if a field has been set.

### SetLastRunStatusNil

`func (o *StreamingSpecificationSummary) SetLastRunStatusNil(b bool)`

 SetLastRunStatusNil sets the value for LastRunStatus to be an explicit nil

### UnsetLastRunStatus
`func (o *StreamingSpecificationSummary) UnsetLastRunStatus()`

UnsetLastRunStatus ensures that no value is present for LastRunStatus, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


