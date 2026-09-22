

# DocumentVisualDiffGeneration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**generationId** | **UUID** | A UUIDv7 identifier. Treat identifiers as opaque values. |  |
|**generationNumber** | **Integer** |  |  |
|**expectedSha256** | **String** |  |  |
|**colorThreshold** | **Double** |  |  |
|**totalPages** | **Integer** |  |  |
|**changedPages** | **Integer** |  |  |
|**diffPixels** | **Long** |  |  |
|**diffPixelRatio** | **Double** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**expiresAt** | **OffsetDateTime** |  |  |
|**excludedRegions** | [**List&lt;DocumentVisualExcludedRegion&gt;**](DocumentVisualExcludedRegion.md) | Immutable normalized masks used by this generation. |  |
|**changedExcludedRegionIndexes** | **Set&lt;Integer&gt;** | Indexes into excludedRegions whose masked area contained a real change in this immutable generation. |  |
|**pages** | [**List&lt;DocumentVisualDiffPage&gt;**](DocumentVisualDiffPage.md) |  |  |



