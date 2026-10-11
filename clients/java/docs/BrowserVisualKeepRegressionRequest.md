

# BrowserVisualKeepRegressionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionId** | **UUID** | Client-generated idempotency key for this review command. |  |
|**expectedAssertionRevision** | **Long** | Current assertion revision. A stale value is rejected with HTTP 409. |  |
