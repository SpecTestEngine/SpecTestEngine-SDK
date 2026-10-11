# StreamingSpecification

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
**StableKey** | **string** |  |
**Format** | **string** |  |
**RawSpec** | **string** |  |
**Spec** | **map[string]interface{}** |  |
**DefinitionHash** | **string** |  |

## Methods

### NewStreamingSpecification

`func NewStreamingSpecification(id string, name string, specType string, transport StreamingTransport, endpoint string, codec string, createdAt time.Time, updatedAt time.Time, stableKey string, format string, rawSpec string, spec map[string]interface{}, definitionHash string, ) *StreamingSpecification`

NewStreamingSpecification instantiates a new StreamingSpecification object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreamingSpecificationWithDefaults

`func NewStreamingSpecificationWithDefaults() *StreamingSpecification`

NewStreamingSpecificationWithDefaults instantiates a new StreamingSpecification object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *StreamingSpecification) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *StreamingSpecification) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *StreamingSpecification) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *StreamingSpecification) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *StreamingSpecification) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *StreamingSpecification) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *StreamingSpecification) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *StreamingSpecification) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *StreamingSpecification) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *StreamingSpecification) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *StreamingSpecification) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *StreamingSpecification) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSpecType

`func (o *StreamingSpecification) GetSpecType() string`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *StreamingSpecification) GetSpecTypeOk() (*string, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *StreamingSpecification) SetSpecType(v string)`

SetSpecType sets SpecType field to given value.


### GetTransport

`func (o *StreamingSpecification) GetTransport() StreamingTransport`

GetTransport returns the Transport field if non-nil, zero value otherwise.

### GetTransportOk

`func (o *StreamingSpecification) GetTransportOk() (*StreamingTransport, bool)`

GetTransportOk returns a tuple with the Transport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransport

`func (o *StreamingSpecification) SetTransport(v StreamingTransport)`

SetTransport sets Transport field to given value.


### GetEndpoint

`func (o *StreamingSpecification) GetEndpoint() string`

GetEndpoint returns the Endpoint field if non-nil, zero value otherwise.

### GetEndpointOk

`func (o *StreamingSpecification) GetEndpointOk() (*string, bool)`

GetEndpointOk returns a tuple with the Endpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndpoint

`func (o *StreamingSpecification) SetEndpoint(v string)`

SetEndpoint sets Endpoint field to given value.


### GetCodec

`func (o *StreamingSpecification) GetCodec() string`

GetCodec returns the Codec field if non-nil, zero value otherwise.

### GetCodecOk

`func (o *StreamingSpecification) GetCodecOk() (*string, bool)`

GetCodecOk returns a tuple with the Codec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodec

`func (o *StreamingSpecification) SetCodec(v string)`

SetCodec sets Codec field to given value.


### GetCreatedAt

`func (o *StreamingSpecification) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *StreamingSpecification) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *StreamingSpecification) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetUpdatedAt

`func (o *StreamingSpecification) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *StreamingSpecification) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *StreamingSpecification) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetLastRunAt

`func (o *StreamingSpecification) GetLastRunAt() time.Time`

GetLastRunAt returns the LastRunAt field if non-nil, zero value otherwise.

### GetLastRunAtOk

`func (o *StreamingSpecification) GetLastRunAtOk() (*time.Time, bool)`

GetLastRunAtOk returns a tuple with the LastRunAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunAt

`func (o *StreamingSpecification) SetLastRunAt(v time.Time)`

SetLastRunAt sets LastRunAt field to given value.

### HasLastRunAt

`func (o *StreamingSpecification) HasLastRunAt() bool`

HasLastRunAt returns a boolean if a field has been set.

### SetLastRunAtNil

`func (o *StreamingSpecification) SetLastRunAtNil(b bool)`

 SetLastRunAtNil sets the value for LastRunAt to be an explicit nil

### UnsetLastRunAt
`func (o *StreamingSpecification) UnsetLastRunAt()`

UnsetLastRunAt ensures that no value is present for LastRunAt, not even an explicit nil
### GetLastRunStatus

`func (o *StreamingSpecification) GetLastRunStatus() string`

GetLastRunStatus returns the LastRunStatus field if non-nil, zero value otherwise.

### GetLastRunStatusOk

`func (o *StreamingSpecification) GetLastRunStatusOk() (*string, bool)`

GetLastRunStatusOk returns a tuple with the LastRunStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunStatus

`func (o *StreamingSpecification) SetLastRunStatus(v string)`

SetLastRunStatus sets LastRunStatus field to given value.

### HasLastRunStatus

`func (o *StreamingSpecification) HasLastRunStatus() bool`

HasLastRunStatus returns a boolean if a field has been set.

### SetLastRunStatusNil

`func (o *StreamingSpecification) SetLastRunStatusNil(b bool)`

 SetLastRunStatusNil sets the value for LastRunStatus to be an explicit nil

### UnsetLastRunStatus
`func (o *StreamingSpecification) UnsetLastRunStatus()`

UnsetLastRunStatus ensures that no value is present for LastRunStatus, not even an explicit nil
### GetStableKey

`func (o *StreamingSpecification) GetStableKey() string`

GetStableKey returns the StableKey field if non-nil, zero value otherwise.

### GetStableKeyOk

`func (o *StreamingSpecification) GetStableKeyOk() (*string, bool)`

GetStableKeyOk returns a tuple with the StableKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStableKey

`func (o *StreamingSpecification) SetStableKey(v string)`

SetStableKey sets StableKey field to given value.


### GetFormat

`func (o *StreamingSpecification) GetFormat() string`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *StreamingSpecification) GetFormatOk() (*string, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *StreamingSpecification) SetFormat(v string)`

SetFormat sets Format field to given value.


### GetRawSpec

`func (o *StreamingSpecification) GetRawSpec() string`

GetRawSpec returns the RawSpec field if non-nil, zero value otherwise.

### GetRawSpecOk

`func (o *StreamingSpecification) GetRawSpecOk() (*string, bool)`

GetRawSpecOk returns a tuple with the RawSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawSpec

`func (o *StreamingSpecification) SetRawSpec(v string)`

SetRawSpec sets RawSpec field to given value.


### GetSpec

`func (o *StreamingSpecification) GetSpec() map[string]interface{}`

GetSpec returns the Spec field if non-nil, zero value otherwise.

### GetSpecOk

`func (o *StreamingSpecification) GetSpecOk() (*map[string]interface{}, bool)`

GetSpecOk returns a tuple with the Spec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpec

`func (o *StreamingSpecification) SetSpec(v map[string]interface{})`

SetSpec sets Spec field to given value.


### GetDefinitionHash

`func (o *StreamingSpecification) GetDefinitionHash() string`

GetDefinitionHash returns the DefinitionHash field if non-nil, zero value otherwise.

### GetDefinitionHashOk

`func (o *StreamingSpecification) GetDefinitionHashOk() (*string, bool)`

GetDefinitionHashOk returns a tuple with the DefinitionHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefinitionHash

`func (o *StreamingSpecification) SetDefinitionHash(v string)`

SetDefinitionHash sets DefinitionHash field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
