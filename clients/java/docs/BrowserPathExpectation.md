

# BrowserPathExpectation

Exactly one of value or pattern is required. Values retain JSON types, including explicit null. Pattern is a whole-string glob with at most 32 stars; only a star or backslash can be escaped. Runtime templates are not accepted in patterns.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**path** | **String** |  |  |
|**value** | **Object** | Exact JSON value, including null. Absence selects pattern matching instead. |  [optional] |
|**pattern** | **String** |  |  [optional] |
