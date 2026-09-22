# Specification

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
**StableKey** | Pointer to **NullableString** |  | [optional]
**Format** | [**ContentFormat**](ContentFormat.md) |  | [default to CONTENTFORMAT_JSON]
**RawSpec** | **string** |  |
**Spec** | **map[string]interface{}** |  |

## Methods

### NewSpecification

`func NewSpecification(id string, name string, specType SpecType, createdAt time.Time, format ContentFormat, rawSpec string, spec map[string]interface{}, ) *Specification`

NewSpecification instantiates a new Specification object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpecificationWithDefaults

`func NewSpecificationWithDefaults() *Specification`

NewSpecificationWithDefaults instantiates a new Specification object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Specification) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Specification) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Specification) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *Specification) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Specification) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Specification) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *Specification) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Specification) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Specification) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Specification) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Specification) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Specification) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetSpecType

`func (o *Specification) GetSpecType() SpecType`

GetSpecType returns the SpecType field if non-nil, zero value otherwise.

### GetSpecTypeOk

`func (o *Specification) GetSpecTypeOk() (*SpecType, bool)`

GetSpecTypeOk returns a tuple with the SpecType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecType

`func (o *Specification) SetSpecType(v SpecType)`

SetSpecType sets SpecType field to given value.


### GetMethod

`func (o *Specification) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *Specification) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *Specification) SetMethod(v string)`

SetMethod sets Method field to given value.

### HasMethod

`func (o *Specification) HasMethod() bool`

HasMethod returns a boolean if a field has been set.

### SetMethodNil

`func (o *Specification) SetMethodNil(b bool)`

 SetMethodNil sets the value for Method to be an explicit nil

### UnsetMethod
`func (o *Specification) UnsetMethod()`

UnsetMethod ensures that no value is present for Method, not even an explicit nil
### GetUrl

`func (o *Specification) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *Specification) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *Specification) SetUrl(v string)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *Specification) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### SetUrlNil

`func (o *Specification) SetUrlNil(b bool)`

 SetUrlNil sets the value for Url to be an explicit nil

### UnsetUrl
`func (o *Specification) UnsetUrl()`

UnsetUrl ensures that no value is present for Url, not even an explicit nil
### GetUpdatedAt

`func (o *Specification) GetUpdatedAt() time.Time`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *Specification) GetUpdatedAtOk() (*time.Time, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *Specification) SetUpdatedAt(v time.Time)`

SetUpdatedAt sets UpdatedAt field to given value.

### HasUpdatedAt

`func (o *Specification) HasUpdatedAt() bool`

HasUpdatedAt returns a boolean if a field has been set.

### SetUpdatedAtNil

`func (o *Specification) SetUpdatedAtNil(b bool)`

 SetUpdatedAtNil sets the value for UpdatedAt to be an explicit nil

### UnsetUpdatedAt
`func (o *Specification) UnsetUpdatedAt()`

UnsetUpdatedAt ensures that no value is present for UpdatedAt, not even an explicit nil
### GetCreatedAt

`func (o *Specification) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Specification) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Specification) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetLastRunAt

`func (o *Specification) GetLastRunAt() time.Time`

GetLastRunAt returns the LastRunAt field if non-nil, zero value otherwise.

### GetLastRunAtOk

`func (o *Specification) GetLastRunAtOk() (*time.Time, bool)`

GetLastRunAtOk returns a tuple with the LastRunAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunAt

`func (o *Specification) SetLastRunAt(v time.Time)`

SetLastRunAt sets LastRunAt field to given value.

### HasLastRunAt

`func (o *Specification) HasLastRunAt() bool`

HasLastRunAt returns a boolean if a field has been set.

### SetLastRunAtNil

`func (o *Specification) SetLastRunAtNil(b bool)`

 SetLastRunAtNil sets the value for LastRunAt to be an explicit nil

### UnsetLastRunAt
`func (o *Specification) UnsetLastRunAt()`

UnsetLastRunAt ensures that no value is present for LastRunAt, not even an explicit nil
### GetLastRunStatus

`func (o *Specification) GetLastRunStatus() string`

GetLastRunStatus returns the LastRunStatus field if non-nil, zero value otherwise.

### GetLastRunStatusOk

`func (o *Specification) GetLastRunStatusOk() (*string, bool)`

GetLastRunStatusOk returns a tuple with the LastRunStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRunStatus

`func (o *Specification) SetLastRunStatus(v string)`

SetLastRunStatus sets LastRunStatus field to given value.

### HasLastRunStatus

`func (o *Specification) HasLastRunStatus() bool`

HasLastRunStatus returns a boolean if a field has been set.

### SetLastRunStatusNil

`func (o *Specification) SetLastRunStatusNil(b bool)`

 SetLastRunStatusNil sets the value for LastRunStatus to be an explicit nil

### UnsetLastRunStatus
`func (o *Specification) UnsetLastRunStatus()`

UnsetLastRunStatus ensures that no value is present for LastRunStatus, not even an explicit nil
### GetStableKey

`func (o *Specification) GetStableKey() string`

GetStableKey returns the StableKey field if non-nil, zero value otherwise.

### GetStableKeyOk

`func (o *Specification) GetStableKeyOk() (*string, bool)`

GetStableKeyOk returns a tuple with the StableKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStableKey

`func (o *Specification) SetStableKey(v string)`

SetStableKey sets StableKey field to given value.

### HasStableKey

`func (o *Specification) HasStableKey() bool`

HasStableKey returns a boolean if a field has been set.

### SetStableKeyNil

`func (o *Specification) SetStableKeyNil(b bool)`

 SetStableKeyNil sets the value for StableKey to be an explicit nil

### UnsetStableKey
`func (o *Specification) UnsetStableKey()`

UnsetStableKey ensures that no value is present for StableKey, not even an explicit nil
### GetFormat

`func (o *Specification) GetFormat() ContentFormat`

GetFormat returns the Format field if non-nil, zero value otherwise.

### GetFormatOk

`func (o *Specification) GetFormatOk() (*ContentFormat, bool)`

GetFormatOk returns a tuple with the Format field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFormat

`func (o *Specification) SetFormat(v ContentFormat)`

SetFormat sets Format field to given value.


### GetRawSpec

`func (o *Specification) GetRawSpec() string`

GetRawSpec returns the RawSpec field if non-nil, zero value otherwise.

### GetRawSpecOk

`func (o *Specification) GetRawSpecOk() (*string, bool)`

GetRawSpecOk returns a tuple with the RawSpec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRawSpec

`func (o *Specification) SetRawSpec(v string)`

SetRawSpec sets RawSpec field to given value.


### GetSpec

`func (o *Specification) GetSpec() map[string]interface{}`

GetSpec returns the Spec field if non-nil, zero value otherwise.

### GetSpecOk

`func (o *Specification) GetSpecOk() (*map[string]interface{}, bool)`

GetSpecOk returns a tuple with the Spec field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpec

`func (o *Specification) SetSpec(v map[string]interface{})`

SetSpec sets Spec field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


