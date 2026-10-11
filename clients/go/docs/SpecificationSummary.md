# SpecificationSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A UUIDv7 identifier. Treat identifiers as opaque values. |
**Name** | **string** |  |
**Description** | Pointer to **NullableString** |  | [optional]
**SpecType** | [**SpecType**](SpecType.md) |  |
**Method** | Pointer to **NullableString** | HTTP method from a REST specification request. | [optional]
**Url** | Pointer to **NullableString** | Request URL from a REST specification. | [optional]
**UpdatedAt** | Pointer to **NullableTime** |  | [optional]
**CreatedAt** | **time.Time** |  |
**LastRunAt** | Pointer to **NullableTime** |  | [optional]
**LastRunStatus** | Pointer to **NullableString** |  | [optional]

## Methods

### NewSpecificationSummary

`func NewSpecificationSummary(id string, name string, specType SpecType, createdAt time.Time, ) *SpecificationSummary`

NewSpecificationSummary instantiates a new SpecificationSummary object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpecificationSummaryWithDefaults

`func NewSpecificationSummaryWithDefaults() *SpecificationSummary`

NewSpecificationSummaryWithDefaults instantiates a new SpecificationSummary object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SpecificationSummary) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SpecificationSummary) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SpecificationSummary) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *SpecificationSummary) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SpecificationSummary) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SpecificationSummary) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *SpecificationSummary) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SpecificationSummary) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SpecificationSummary) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SpecificationSummary) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *SpecificationSummary) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *SpecificationSummary) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSpecType

`func (o *SpecificationSummary) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *SpecificationSummary) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *SpecificationSummary) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetMethod

`func (o *SpecificationSummary) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *SpecificationSummary) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *SpecificationSummary) SetMethod(v string)`

SetMethod sets Method field to given value.

### HasMethod

`func (o *SpecificationSummary) HasMethod() bool`

HasMethod returns a boolean if a field has been set.

### SetMethodNil

`func (o *SpecificationSummary) SetMethodNil(b bool)`

 SetMethodNil sets the value for Method to be an explicit nil

### UnsetMethod
`func (o *SpecificationSummary) UnsetMethod()`

UnsetMethod ensures that no value is present for Method, not even an explicit nil
### GetUrl

`func (o *SpecificationSummary) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *SpecificationSummary) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *SpecificationSummary) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *SpecificationSummary) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### SetUrlNil

`func (o *SpecificationSummary) SetUrlNil(b bool)`

 SetUrlNil sets the value for Url to be an explicit nil

### UnsetUrl
`func (o *SpecificationSummary) UnsetUrl()`

UnsetUrl ensures that no value is present for Url, not even an explicit nil
### GetUpdatedAt

`func (o *SpecificationSummary) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *SpecificationSummary) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *SpecificationSummary) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *SpecificationSummary) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### SetUpdatedAtNil

`func (o *SpecificationSummary) SetUpdatedAtNil(b bool)`

 SetUpdatedAtNil sets the value for UpdatedAt to be an explicit nil

### UnsetUpdatedAt
`func (o *SpecificationSummary) UnsetUpdatedAt()`

UnsetUpdatedAt ensures that no value is present for UpdatedAt, not even an explicit nil
### GetCreatedAt

`func (o *SpecificationSummary) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SpecificationSummary) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SpecificationSummary) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetLastRunAt

`func (o *SpecificationSummary) GetLastRunAt() time.Time`

GetLastRunAt returns the LastRunAt field if non-nil, zero value otherwise.

### GetLastRunAtOk

`func (o *SpecificationSummary) GetLastRunAtOk() (*time.Time, bool)`

GetLastRunAtOk returns a tuple with the LastRunAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunAt

`func (o *SpecificationSummary) SetLastRunAt(v time.Time)`

SetLastRunAt sets LastRunAt field to given value.

### HasLastRunAt

`func (o *SpecificationSummary) HasLastRunAt() bool`

HasLastRunAt returns a boolean if a field has been set.

### SetLastRunAtNil

`func (o *SpecificationSummary) SetLastRunAtNil(b bool)`

 SetLastRunAtNil sets the value for LastRunAt to be an explicit nil

### UnsetLastRunAt
`func (o *SpecificationSummary) UnsetLastRunAt()`

UnsetLastRunAt ensures that no value is present for LastRunAt, not even an explicit nil
### GetLastRunStatus

`func (o *SpecificationSummary) GetLastRunStatus() string`

GetLastRunStatus returns the LastRunStatus field if non-nil, zero value otherwise.

### GetLastRunStatusOk

`func (o *SpecificationSummary) GetLastRunStatusOk() (*string, bool)`

GetLastRunStatusOk returns a tuple with the LastRunStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunStatus

`func (o *SpecificationSummary) SetLastRunStatus(v string)`

SetLastRunStatus sets LastRunStatus field to given value.

### HasLastRunStatus

`func (o *SpecificationSummary) HasLastRunStatus() bool`

HasLastRunStatus returns a boolean if a field has been set.

### SetLastRunStatusNil

`func (o *SpecificationSummary) SetLastRunStatusNil(b bool)`

 SetLastRunStatusNil sets the value for LastRunStatus to be an explicit nil

### UnsetLastRunStatus
`func (o *SpecificationSummary) UnsetLastRunStatus()`

UnsetLastRunStatus ensures that no value is present for LastRunStatus, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
