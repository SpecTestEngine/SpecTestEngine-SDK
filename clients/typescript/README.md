# @spectestengine/sdk@0.1.0

A TypeScript SDK client for the app.ste.software API.

## Usage

First, install the SDK from npm.

```bash
npm install @spectestengine/sdk --save
```

Next, try it out.


```ts
import {
  Configuration,
  BrowserVisualReviewsApi,
} from '@spectestengine/sdk';
import type { ExcludeBrowserVisualAreaAndRecompareRequest } from '@spectestengine/sdk';

async function example() {
  console.log("🚀 Testing @spectestengine/sdk SDK...");
  const config = new Configuration({
    // Configure HTTP bearer authorization: BearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new BrowserVisualReviewsApi(config);

  const body = {
    // string | Identifier of an immutable Browser visual comparison generation.
    comparisonId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // BrowserVisualExcludeAndRecompareRequest
    browserVisualExcludeAndRecompareRequest: ...,
  } satisfies ExcludeBrowserVisualAreaAndRecompareRequest;

  try {
    const data = await api.excludeBrowserVisualAreaAndRecompare(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```


## Documentation

### API Endpoints

All URIs are relative to *https://app.ste.software*

| Class | Method | HTTP request | Description
| ----- | ------ | ------------ | -------------
*BrowserVisualReviewsApi* | [**excludeBrowserVisualAreaAndRecompare**](docs/BrowserVisualReviewsApi.md#excludebrowservisualareaandrecompare) | **POST** /browser/visual/comparisons/{comparisonId}/exclude-and-recompare | Exclude area and recompare
*BrowserVisualReviewsApi* | [**getBrowserVisualArtifactContent**](docs/BrowserVisualReviewsApi.md#getbrowservisualartifactcontent) | **GET** /browser/visual/artifacts/{artifactId}/content | Download Browser visual evidence
*BrowserVisualReviewsApi* | [**getBrowserVisualComparison**](docs/BrowserVisualReviewsApi.md#getbrowservisualcomparison) | **GET** /browser/visual/comparisons/{comparisonId} | Get a Browser visual comparison
*BrowserVisualReviewsApi* | [**keepBrowserVisualAsRegression**](docs/BrowserVisualReviewsApi.md#keepbrowservisualasregression) | **POST** /browser/visual/comparisons/{comparisonId}/keep-as-regression | Keep as regression
*BrowserVisualReviewsApi* | [**useCurrentBrowserVisualAsNewBaseline**](docs/BrowserVisualReviewsApi.md#usecurrentbrowservisualasnewbaseline) | **POST** /browser/visual/comparisons/{comparisonId}/use-current-as-new-baseline | Use current as new baseline
*CraftsmanApi* | [**cancelCraftsmanRun**](docs/CraftsmanApi.md#cancelcraftsmanrun) | **POST** /sentinel/request-workspaces/runs/{runId}/cancel | Cancel a queued or active Craftsman run
*CraftsmanApi* | [**createRequestNode**](docs/CraftsmanApi.md#createrequestnode) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes | Add a folder or saved request
*CraftsmanApi* | [**createRequestWorkspace**](docs/CraftsmanApi.md#createrequestworkspace) | **POST** /sentinel/request-workspaces | Create a request workspace
*CraftsmanApi* | [**deleteRequestNode**](docs/CraftsmanApi.md#deleterequestnode) | **DELETE** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Delete a folder or saved request
*CraftsmanApi* | [**deleteRequestWorkspace**](docs/CraftsmanApi.md#deleterequestworkspace) | **DELETE** /sentinel/request-workspaces/{workspaceId} | Delete a request workspace
*CraftsmanApi* | [**getCraftsmanRun**](docs/CraftsmanApi.md#getcraftsmanrun) | **GET** /sentinel/request-workspaces/runs/{runId} | Get Craftsman run lifecycle and evidence
*CraftsmanApi* | [**getCraftsmanRunTranscript**](docs/CraftsmanApi.md#getcraftsmanruntranscript) | **GET** /sentinel/request-workspaces/runs/{runId}/transcript | Get a Craftsman Streaming semantic transcript
*CraftsmanApi* | [**getDocumentAsset**](docs/CraftsmanApi.md#getdocumentasset) | **GET** /sentinel/document-assets/{assetId} | Resolve request attachment metadata
*CraftsmanApi* | [**getRequestWorkspace**](docs/CraftsmanApi.md#getrequestworkspace) | **GET** /sentinel/request-workspaces/{workspaceId} | Get a request workspace
*CraftsmanApi* | [**listRequestWorkspaces**](docs/CraftsmanApi.md#listrequestworkspaces) | **GET** /sentinel/request-workspaces/page | List request workspaces
*CraftsmanApi* | [**queueCraftsmanStreamingRun**](docs/CraftsmanApi.md#queuecraftsmanstreamingrun) | **POST** /sentinel/request-workspaces/runs/streaming | Queue a standalone bounded Streaming session
*CraftsmanApi* | [**queueCraftsmanWorkflowRun**](docs/CraftsmanApi.md#queuecraftsmanworkflowrun) | **POST** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId}/runs | Queue a saved request or mixed-protocol Workflow run
*CraftsmanApi* | [**updateRequestNode**](docs/CraftsmanApi.md#updaterequestnode) | **PUT** /sentinel/request-workspaces/{workspaceId}/nodes/{nodeId} | Update a folder or saved request
*CraftsmanApi* | [**updateRequestWorkspace**](docs/CraftsmanApi.md#updaterequestworkspace) | **PUT** /sentinel/request-workspaces/{workspaceId} | Replace request workspace metadata and variables
*CraftsmanApi* | [**uploadDocumentAsset**](docs/CraftsmanApi.md#uploaddocumentasset) | **POST** /sentinel/document-assets | Upload a reusable request attachment
*DocumentVisualDiffsApi* | [**getDocumentVisualDiff**](docs/DocumentVisualDiffsApi.md#getdocumentvisualdiff) | **GET** /browser/visual/document-diffs/{visualDiffId} | Get a visual document diff
*DocumentVisualDiffsApi* | [**getDocumentVisualDiffArtifact**](docs/DocumentVisualDiffsApi.md#getdocumentvisualdiffartifact) | **GET** /browser/visual/document-diffs/{visualDiffId}/artifacts/{artifactId} | Download a rendered visual diff page
*DocumentVisualDiffsApi* | [**prepareDocumentVisualDiffBaseline**](docs/DocumentVisualDiffsApi.md#preparedocumentvisualdiffbaseline) | **POST** /browser/visual/document-diffs/{visualDiffId}/baseline | Preview or create an attachment baseline update draft
*DocumentVisualDiffsApi* | [**regenerateDocumentVisualDiff**](docs/DocumentVisualDiffsApi.md#regeneratedocumentvisualdiff) | **POST** /browser/visual/document-diffs/{visualDiffId}/regenerate | Regenerate a visual document diff
*DocumentVisualDiffsApi* | [**uploadDocumentVisualDiffExpected**](docs/DocumentVisualDiffsApi.md#uploaddocumentvisualdiffexpected) | **POST** /browser/visual/document-diffs/{visualDiffId}/expected | Upload a reference document and create a diff generation
*FlowsApi* | [**captureFlowStepAttachmentVisualDiff**](docs/FlowsApi.md#captureflowstepattachmentvisualdiff) | **POST** /test/flow/run/by-id/{flowId}/visual-diff-captures | Create a visual diff from a failed flow-step attachment assertion
*FlowsApi* | [**copyFlowRecoveryDraft**](docs/FlowsApi.md#copyflowrecoverydraft) | **POST** /test/flow/run/saved/{runId}/recovery/copy | Recover an edited draft as an independent new Flow
*FlowsApi* | [**createFlow**](docs/FlowsApi.md#createflow) | **POST** /test/flow/create | Create a test flow
*FlowsApi* | [**createFlowRecovery**](docs/FlowsApi.md#createflowrecovery) | **POST** /test/flow/run/saved/{runId}/recovery | Recover a saved run as a new Flow and new dependency copies
*FlowsApi* | [**deleteFlow**](docs/FlowsApi.md#deleteflow) | **DELETE** /test/flow/by-id | Delete a test flow
*FlowsApi* | [**getFlow**](docs/FlowsApi.md#getflow) | **GET** /test/flow/by-id/{flowId} | Get a test flow
*FlowsApi* | [**getFlowRecoveryCurrentDependency**](docs/FlowsApi.md#getflowrecoverycurrentdependency) | **GET** /test/flow/run/saved/{runId}/recovery/current-dependency | Read one current safe Recovery dependency
*FlowsApi* | [**getFlowRecoveryDependency**](docs/FlowsApi.md#getflowrecoverydependency) | **GET** /test/flow/run/saved/{runId}/recovery/dependencies/{dependencyKey} | Inspect one retained safe dependency definition
*FlowsApi* | [**getFlowRecoveryOperation**](docs/FlowsApi.md#getflowrecoveryoperation) | **GET** /test/flow/run/recovery-operations/{operationId} | Read a Flow recovery outcome without performing writes
*FlowsApi* | [**getFlowRun**](docs/FlowsApi.md#getflowrun) | **GET** /test/flow/run/saved/{runId} | Get a saved flow run
*FlowsApi* | [**listFlowRecoveryDependencies**](docs/FlowsApi.md#listflowrecoverydependencies) | **GET** /test/flow/run/saved/{runId}/recovery/dependencies | List historical dependency versions for Flow recovery
*FlowsApi* | [**listFlowRuns**](docs/FlowsApi.md#listflowruns) | **GET** /test/flow/run/by-flow-id/{flowId}/page | List saved runs for a flow
*FlowsApi* | [**listFlows**](docs/FlowsApi.md#listflows) | **GET** /test/flow/page | List test flows
*FlowsApi* | [**previewFlowRecovery**](docs/FlowsApi.md#previewflowrecovery) | **GET** /test/flow/run/saved/{runId}/recovery/preview | Preview an independent Flow recovery from a saved run
*FlowsApi* | [**restoreFlowRecoveryDraft**](docs/FlowsApi.md#restoreflowrecoverydraft) | **POST** /test/flow/run/saved/{runId}/recovery/restore | Restore an edited historical Flow into the current Flow
*FlowsApi* | [**reviewFlowRecovery**](docs/FlowsApi.md#reviewflowrecovery) | **GET** /test/flow/run/saved/{runId}/recovery/review | Review Flow Recovery for restore or independent copy
*FlowsApi* | [**runFlow**](docs/FlowsApi.md#runflow) | **POST** /test/flow/run/by-id/{flowId} | Run a saved flow
*FlowsApi* | [**runFlowBatch**](docs/FlowsApi.md#runflowbatchoperation) | **POST** /test/flow/run/batch | Run multiple saved flows
*FlowsApi* | [**updateFlow**](docs/FlowsApi.md#updateflow) | **PUT** /test/flow/by-id | Replace a test flow
*FragmentsApi* | [**compileDraftFragments**](docs/FragmentsApi.md#compiledraftfragments) | **POST** /test/spec/fragment/compile-draft | Compile inline fragment DSL into a specification draft
*FragmentsApi* | [**compileFragments**](docs/FragmentsApi.md#compilefragments) | **POST** /test/spec/fragment/compile | Compile fragments into a specification draft
*FragmentsApi* | [**createFragment**](docs/FragmentsApi.md#createfragment) | **POST** /test/spec/fragment/create | Create a specification fragment
*FragmentsApi* | [**deleteFragment**](docs/FragmentsApi.md#deletefragment) | **DELETE** /test/spec/fragment/by-id | Delete a fragment
*FragmentsApi* | [**getFragment**](docs/FragmentsApi.md#getfragment) | **GET** /test/spec/fragment/by-id/{fragmentId} | Get a fragment
*FragmentsApi* | [**getFragmentCatalog**](docs/FragmentsApi.md#getfragmentcatalog) | **GET** /test/spec/fragment/catalog | Get the fragment DSL catalog for an API type
*FragmentsApi* | [**getFragmentSummary**](docs/FragmentsApi.md#getfragmentsummary) | **GET** /test/spec/fragment/summary | Count fragments by API type
*FragmentsApi* | [**listFragments**](docs/FragmentsApi.md#listfragments) | **GET** /test/spec/fragment/page | List specification fragments
*FragmentsApi* | [**saveFragmentsAsSpecification**](docs/FragmentsApi.md#savefragmentsasspecification) | **POST** /test/spec/fragment/save-as-spec | Compile saved fragments and persist the result in the matching protocol engine
*FragmentsApi* | [**updateFragment**](docs/FragmentsApi.md#updatefragment) | **PUT** /test/spec/fragment/by-id | Replace a fragment
*GenerationApi* | [**createArtifactGenerationProfile**](docs/GenerationApi.md#createartifactgenerationprofile) | **POST** /artifact-profiles | Create a CI export profile
*GenerationApi* | [**deleteArtifactGenerationProfile**](docs/GenerationApi.md#deleteartifactgenerationprofile) | **DELETE** /artifact-profiles/{profileId} | Delete a CI export profile
*GenerationApi* | [**downloadArtifactGenerationProfileArchive**](docs/GenerationApi.md#downloadartifactgenerationprofilearchive) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/atf/archive | Validate and download a CI profile archive
*GenerationApi* | [**downloadAtfProject**](docs/GenerationApi.md#downloadatfproject) | **POST** /atf/generate/download | Download a generated ATF project
*GenerationApi* | [**generateFromOpenApiContent**](docs/GenerationApi.md#generatefromopenapicontent) | **POST** /openapi/generate-from-content | Generate specifications and flows from OpenAPI content
*GenerationApi* | [**generateSpecification**](docs/GenerationApi.md#generatespecification) | **POST** /spec/generate | Generate an executable specification from concrete request evidence
*GenerationApi* | [**getArtifactGenerationProfile**](docs/GenerationApi.md#getartifactgenerationprofile) | **GET** /artifact-profiles/{profileId} | Get a CI export profile
*GenerationApi* | [**getAtfProjectValidationResult**](docs/GenerationApi.md#getatfprojectvalidationresult) | **GET** /atf/generate/validate/result/{validationId} | Get ATF validation status or result
*GenerationApi* | [**listArtifactGenerationProfiles**](docs/GenerationApi.md#listartifactgenerationprofiles) | **GET** /artifact-profiles | List CI export profiles
*GenerationApi* | [**observeAtfProjectValidation**](docs/GenerationApi.md#observeatfprojectvalidation) | **GET** /atf/generate/validate/events/{validationId} | Observe ATF validation progress
*GenerationApi* | [**previewAtfProject**](docs/GenerationApi.md#previewatfproject) | **POST** /atf/generate/preview | Generate an ATF project preview
*GenerationApi* | [**refreshArtifactGenerationProfileBundle**](docs/GenerationApi.md#refreshartifactgenerationprofilebundle) | **POST** /artifact-profiles/{profileId}/environments/{environmentKey}/bundle/refresh | Capture or refresh an environment baseline
*GenerationApi* | [**startAtfProjectValidation**](docs/GenerationApi.md#startatfprojectvalidation) | **POST** /atf/generate/validate/start | Start asynchronous ATF compile validation
*GenerationApi* | [**updateArtifactGenerationProfile**](docs/GenerationApi.md#updateartifactgenerationprofile) | **PUT** /artifact-profiles/{profileId} | Update a CI export profile
*GenerationApi* | [**validateAtfProject**](docs/GenerationApi.md#validateatfproject) | **POST** /atf/generate/validate | Validate that an ATF project compiles
*GraphQLSpecificationsApi* | [**captureGraphqlSpecificationAttachmentVisualDiff**](docs/GraphQLSpecificationsApi.md#capturegraphqlspecificationattachmentvisualdiff) | **POST** /test/graphql-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed GraphQL attachment assertion
*GraphQLSpecificationsApi* | [**createGraphqlSpecification**](docs/GraphQLSpecificationsApi.md#creategraphqlspecification) | **POST** /test/graphql-spec/create | Create a GraphQL specification
*GraphQLSpecificationsApi* | [**deleteGraphqlSpecification**](docs/GraphQLSpecificationsApi.md#deletegraphqlspecification) | **DELETE** /test/graphql-spec/by-id | Delete a GraphQL specification
*GraphQLSpecificationsApi* | [**getGraphqlSpecification**](docs/GraphQLSpecificationsApi.md#getgraphqlspecification) | **GET** /test/graphql-spec/by-id | Get a GraphQL specification
*GraphQLSpecificationsApi* | [**getGraphqlSpecificationRun**](docs/GraphQLSpecificationsApi.md#getgraphqlspecificationrun) | **GET** /test/graphql-spec/run/history/by-run-id/{runId} | Get saved GraphQL run evidence
*GraphQLSpecificationsApi* | [**listGraphqlSpecificationRuns**](docs/GraphQLSpecificationsApi.md#listgraphqlspecificationruns) | **GET** /test/graphql-spec/run/page/by-spec-id/{specId} | List saved GraphQL runs
*GraphQLSpecificationsApi* | [**listGraphqlSpecifications**](docs/GraphQLSpecificationsApi.md#listgraphqlspecifications) | **GET** /test/graphql-spec/page | List GraphQL specifications
*GraphQLSpecificationsApi* | [**previewGraphqlSpecificationRecovery**](docs/GraphQLSpecificationsApi.md#previewgraphqlspecificationrecovery) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a GraphQL specification version
*GraphQLSpecificationsApi* | [**restoreGraphqlSpecificationFromRun**](docs/GraphQLSpecificationsApi.md#restoregraphqlspecificationfromrun) | **PUT** /test/graphql-spec/recovery/{specId}/from-run/{runId}/restore | Restore a GraphQL specification version
*GraphQLSpecificationsApi* | [**runGraphqlSpecification**](docs/GraphQLSpecificationsApi.md#rungraphqlspecification) | **POST** /test/graphql-spec/run/by-id | Run a saved GraphQL specification
*GraphQLSpecificationsApi* | [**testGraphqlSpecificationRecoveryVersion**](docs/GraphQLSpecificationsApi.md#testgraphqlspecificationrecoveryversion) | **POST** /test/graphql-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous GraphQL specification version
*GraphQLSpecificationsApi* | [**updateGraphqlSpecification**](docs/GraphQLSpecificationsApi.md#updategraphqlspecification) | **PUT** /test/graphql-spec/by-id | Replace a GraphQL specification definition
*RESTSpecificationsApi* | [**captureRestSpecificationAttachmentVisualDiff**](docs/RESTSpecificationsApi.md#capturerestspecificationattachmentvisualdiff) | **POST** /test/rest-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed REST attachment assertion
*RESTSpecificationsApi* | [**createRestSpecification**](docs/RESTSpecificationsApi.md#createrestspecification) | **POST** /test/rest-spec/create | Create a REST specification
*RESTSpecificationsApi* | [**deleteRestSpecification**](docs/RESTSpecificationsApi.md#deleterestspecification) | **DELETE** /test/rest-spec/by-id | Delete a REST specification
*RESTSpecificationsApi* | [**getRestSpecification**](docs/RESTSpecificationsApi.md#getrestspecification) | **GET** /test/rest-spec/by-id | Get a REST specification
*RESTSpecificationsApi* | [**getRestSpecificationRun**](docs/RESTSpecificationsApi.md#getrestspecificationrun) | **GET** /test/rest-spec/run/history/by-run-id/{runId} | Get saved REST run evidence
*RESTSpecificationsApi* | [**listRestSpecificationRuns**](docs/RESTSpecificationsApi.md#listrestspecificationruns) | **GET** /test/rest-spec/run/page/by-spec-id/{specId} | List saved REST runs
*RESTSpecificationsApi* | [**listRestSpecifications**](docs/RESTSpecificationsApi.md#listrestspecifications) | **GET** /test/rest-spec/page | List REST specifications
*RESTSpecificationsApi* | [**previewRestSpecificationRecovery**](docs/RESTSpecificationsApi.md#previewrestspecificationrecovery) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a REST specification version
*RESTSpecificationsApi* | [**restoreRestSpecificationFromRun**](docs/RESTSpecificationsApi.md#restorerestspecificationfromrun) | **PUT** /test/rest-spec/recovery/{specId}/from-run/{runId}/restore | Restore a REST specification version
*RESTSpecificationsApi* | [**runRestSpecification**](docs/RESTSpecificationsApi.md#runrestspecification) | **POST** /test/rest-spec/run/by-id | Run a saved REST specification
*RESTSpecificationsApi* | [**testRestSpecificationRecoveryVersion**](docs/RESTSpecificationsApi.md#testrestspecificationrecoveryversion) | **POST** /test/rest-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous REST specification version
*RESTSpecificationsApi* | [**updateRestSpecification**](docs/RESTSpecificationsApi.md#updaterestspecification) | **PUT** /test/rest-spec/by-id | Replace a REST specification definition
*RunBatchesApi* | [**createRunBatch**](docs/RunBatchesApi.md#createrunbatch) | **POST** /test/run-batch/create | Create a run batch
*RunBatchesApi* | [**getRunBatch**](docs/RunBatchesApi.md#getrunbatch) | **GET** /test/run-batch/by-id/{batchId} | Get a run batch
*RunBatchesApi* | [**listRunBatches**](docs/RunBatchesApi.md#listrunbatches) | **GET** /test/run-batch/page | List run batches
*SOAPSpecificationsApi* | [**captureSoapSpecificationAttachmentVisualDiff**](docs/SOAPSpecificationsApi.md#capturesoapspecificationattachmentvisualdiff) | **POST** /test/soap-spec/run/by-id/{specId}/visual-diff-captures | Create a visual diff from a failed SOAP attachment assertion
*SOAPSpecificationsApi* | [**createSoapSpecification**](docs/SOAPSpecificationsApi.md#createsoapspecification) | **POST** /test/soap-spec/create | Create a SOAP specification
*SOAPSpecificationsApi* | [**deleteSoapSpecification**](docs/SOAPSpecificationsApi.md#deletesoapspecification) | **DELETE** /test/soap-spec/by-id | Delete a SOAP specification
*SOAPSpecificationsApi* | [**getSoapSpecification**](docs/SOAPSpecificationsApi.md#getsoapspecification) | **GET** /test/soap-spec/by-id | Get a SOAP specification
*SOAPSpecificationsApi* | [**getSoapSpecificationRun**](docs/SOAPSpecificationsApi.md#getsoapspecificationrun) | **GET** /test/soap-spec/run/history/by-run-id/{runId} | Get saved SOAP run evidence
*SOAPSpecificationsApi* | [**listSoapSpecificationRuns**](docs/SOAPSpecificationsApi.md#listsoapspecificationruns) | **GET** /test/soap-spec/run/page/by-spec-id/{specId} | List saved SOAP runs
*SOAPSpecificationsApi* | [**listSoapSpecifications**](docs/SOAPSpecificationsApi.md#listsoapspecifications) | **GET** /test/soap-spec/page | List SOAP specifications
*SOAPSpecificationsApi* | [**previewSoapSpecificationRecovery**](docs/SOAPSpecificationsApi.md#previewsoapspecificationrecovery) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a SOAP specification version
*SOAPSpecificationsApi* | [**restoreSoapSpecificationFromRun**](docs/SOAPSpecificationsApi.md#restoresoapspecificationfromrun) | **PUT** /test/soap-spec/recovery/{specId}/from-run/{runId}/restore | Restore a SOAP specification version
*SOAPSpecificationsApi* | [**runSoapSpecification**](docs/SOAPSpecificationsApi.md#runsoapspecification) | **POST** /test/soap-spec/run/by-id | Run a saved SOAP specification
*SOAPSpecificationsApi* | [**testSoapSpecificationRecoveryVersion**](docs/SOAPSpecificationsApi.md#testsoapspecificationrecoveryversion) | **POST** /test/soap-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous SOAP specification version
*SOAPSpecificationsApi* | [**updateSoapSpecification**](docs/SOAPSpecificationsApi.md#updatesoapspecification) | **PUT** /test/soap-spec/by-id | Replace a SOAP specification definition
*SentinelApi* | [**createSentinelCheck**](docs/SentinelApi.md#createsentinelcheck) | **POST** /sentinel/checks | Create a Sentinel check
*SentinelApi* | [**deleteSentinelCheck**](docs/SentinelApi.md#deletesentinelcheck) | **DELETE** /sentinel/checks/{checkId} | Delete a Sentinel check
*SentinelApi* | [**enqueueSentinelRun**](docs/SentinelApi.md#enqueuesentinelrun) | **POST** /sentinel/checks/{checkId}/run | Queue a Sentinel run
*SentinelApi* | [**getSentinelCheck**](docs/SentinelApi.md#getsentinelcheck) | **GET** /sentinel/checks/{checkId} | Get a Sentinel check
*SentinelApi* | [**getSentinelDashboardSummary**](docs/SentinelApi.md#getsentineldashboardsummary) | **GET** /sentinel/dashboard/summary | Get Sentinel dashboard summary
*SentinelApi* | [**getSentinelRun**](docs/SentinelApi.md#getsentinelrun) | **GET** /sentinel/runs/{runId} | Get Sentinel run evidence
*SentinelApi* | [**listLatestSentinelRuns**](docs/SentinelApi.md#listlatestsentinelruns) | **GET** /sentinel/runs | List latest Sentinel runs
*SentinelApi* | [**listSentinelChecks**](docs/SentinelApi.md#listsentinelchecks) | **GET** /sentinel/checks/page | List Sentinel checks
*SentinelApi* | [**listSentinelDashboardIncidents**](docs/SentinelApi.md#listsentineldashboardincidents) | **GET** /sentinel/dashboard/incidents | List recent Sentinel incidents
*SentinelApi* | [**listSentinelLinkedAssets**](docs/SentinelApi.md#listsentinellinkedassets) | **GET** /sentinel/checks/spec-links/page | List compact Sentinel links for one Automation asset type
*SentinelApi* | [**listSentinelRuns**](docs/SentinelApi.md#listsentinelruns) | **GET** /sentinel/runs/page | List Sentinel runs
*SentinelApi* | [**sampleSentinelRuns**](docs/SentinelApi.md#samplesentinelruns) | **GET** /sentinel/runs/sample | Sample Sentinel runs
*SentinelApi* | [**updateSentinelCheck**](docs/SentinelApi.md#updatesentinelcheck) | **PUT** /sentinel/checks/{checkId} | Replace a Sentinel check configuration
*SnapshotsApi* | [**compareSnapshotStep**](docs/SnapshotsApi.md#comparesnapshotstep) | **POST** /test/snapshot/diff/step | Compare snapshot step payloads
*SnapshotsApi* | [**compareSnapshotToRunBatch**](docs/SnapshotsApi.md#comparesnapshottorunbatch) | **GET** /test/snapshot/diff/snapshot/{snapshotId}/batch/{batchId} | Compare a snapshot with a run batch
*SnapshotsApi* | [**compareSnapshots**](docs/SnapshotsApi.md#comparesnapshots) | **GET** /test/snapshot/diff/snapshot/{leftSnapshotId}/snapshot/{rightSnapshotId} | Compare two snapshots
*SnapshotsApi* | [**createSnapshot**](docs/SnapshotsApi.md#createsnapshot) | **POST** /test/snapshot/create | Create a snapshot baseline
*SnapshotsApi* | [**getSnapshot**](docs/SnapshotsApi.md#getsnapshot) | **GET** /test/snapshot/by-id/{snapshotId} | Get a snapshot
*SnapshotsApi* | [**listSnapshots**](docs/SnapshotsApi.md#listsnapshots) | **GET** /test/snapshot/page | List snapshots
*StreamingSpecificationsApi* | [**cancelStreamingSpecificationRun**](docs/StreamingSpecificationsApi.md#cancelstreamingspecificationrun) | **POST** /test/streaming-spec/run/history/by-run-id/{runId}/cancel | Cancel an active streaming run
*StreamingSpecificationsApi* | [**createStreamingSpecification**](docs/StreamingSpecificationsApi.md#createstreamingspecification) | **POST** /test/streaming-spec/create | Create a streaming specification
*StreamingSpecificationsApi* | [**deleteStreamingSpecification**](docs/StreamingSpecificationsApi.md#deletestreamingspecification) | **DELETE** /test/streaming-spec/by-id | Delete a streaming specification
*StreamingSpecificationsApi* | [**getStreamingCapabilities**](docs/StreamingSpecificationsApi.md#getstreamingcapabilities) | **GET** /engine/streaming/capabilities | Get streaming engine capabilities and enforced limits
*StreamingSpecificationsApi* | [**getStreamingSpecification**](docs/StreamingSpecificationsApi.md#getstreamingspecification) | **GET** /test/streaming-spec/by-id | Get a streaming specification
*StreamingSpecificationsApi* | [**getStreamingSpecificationRun**](docs/StreamingSpecificationsApi.md#getstreamingspecificationrun) | **GET** /test/streaming-spec/run/history/by-run-id/{runId} | Get streaming run state and bounded semantic evidence
*StreamingSpecificationsApi* | [**getStreamingSpecificationRunTranscript**](docs/StreamingSpecificationsApi.md#getstreamingspecificationruntranscript) | **GET** /test/streaming-spec/run/history/by-run-id/{runId}/transcript | Page a bounded streaming run transcript
*StreamingSpecificationsApi* | [**listStreamingSpecificationRuns**](docs/StreamingSpecificationsApi.md#liststreamingspecificationruns) | **GET** /test/streaming-spec/run/page/by-spec-id/{specId} | List runs for a saved streaming specification
*StreamingSpecificationsApi* | [**listStreamingSpecifications**](docs/StreamingSpecificationsApi.md#liststreamingspecifications) | **GET** /test/streaming-spec/page | List streaming specifications
*StreamingSpecificationsApi* | [**previewStreamingSpecificationRecovery**](docs/StreamingSpecificationsApi.md#previewstreamingspecificationrecovery) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/preview | Preview restoring a Streaming specification version
*StreamingSpecificationsApi* | [**restoreStreamingSpecificationFromRun**](docs/StreamingSpecificationsApi.md#restorestreamingspecificationfromrun) | **PUT** /test/streaming-spec/recovery/{specId}/from-run/{runId}/restore | Restore a Streaming specification version
*StreamingSpecificationsApi* | [**runStreamingSpecification**](docs/StreamingSpecificationsApi.md#runstreamingspecification) | **POST** /test/streaming-spec/run/by-id/{specId} | Queue a saved streaming specification run
*StreamingSpecificationsApi* | [**runStreamingSpecificationDraft**](docs/StreamingSpecificationsApi.md#runstreamingspecificationdraft) | **POST** /test/streaming-spec/run/draft | Queue a bounded streaming specification draft run
*StreamingSpecificationsApi* | [**testStreamingSpecificationRecoveryVersion**](docs/StreamingSpecificationsApi.md#teststreamingspecificationrecoveryversion) | **POST** /test/streaming-spec/recovery/{specId}/from-run/{runId}/test-run | Test a previous Streaming specification version
*StreamingSpecificationsApi* | [**updateStreamingSpecification**](docs/StreamingSpecificationsApi.md#updatestreamingspecification) | **PUT** /test/streaming-spec/by-id | Replace a streaming specification definition
*StreamingSpecificationsApi* | [**validateStreamingSpecificationDraft**](docs/StreamingSpecificationsApi.md#validatestreamingspecificationdraft) | **POST** /test/streaming-spec/validate-draft | Validate and detect the transport of a streaming specification draft


### Models

- [ArtifactGenerationProfile](docs/ArtifactGenerationProfile.md)
- [ArtifactGenerationProfileEnvironment](docs/ArtifactGenerationProfileEnvironment.md)
- [ArtifactGenerationProfileEnvironmentInput](docs/ArtifactGenerationProfileEnvironmentInput.md)
- [ArtifactGenerationProfileInput](docs/ArtifactGenerationProfileInput.md)
- [ArtifactSelection](docs/ArtifactSelection.md)
- [ArtifactSpecRef](docs/ArtifactSpecRef.md)
- [AtfBaseUrlMode](docs/AtfBaseUrlMode.md)
- [AtfGenerationInput](docs/AtfGenerationInput.md)
- [AtfGenerationResult](docs/AtfGenerationResult.md)
- [AtfGenerationResultFilesInner](docs/AtfGenerationResultFilesInner.md)
- [AtfProjectConfig](docs/AtfProjectConfig.md)
- [AtfValidationResult](docs/AtfValidationResult.md)
- [AtfValidationStart](docs/AtfValidationStart.md)
- [AtfValidationStep](docs/AtfValidationStep.md)
- [BrowserActionInput](docs/BrowserActionInput.md)
- [BrowserActionType](docs/BrowserActionType.md)
- [BrowserMacroInput](docs/BrowserMacroInput.md)
- [BrowserMacroStepInput](docs/BrowserMacroStepInput.md)
- [BrowserNetworkExpectation](docs/BrowserNetworkExpectation.md)
- [BrowserSessionInput](docs/BrowserSessionInput.md)
- [BrowserVisualAssertion](docs/BrowserVisualAssertion.md)
- [BrowserVisualAssertionInput](docs/BrowserVisualAssertionInput.md)
- [BrowserVisualBounds](docs/BrowserVisualBounds.md)
- [BrowserVisualCompareMode](docs/BrowserVisualCompareMode.md)
- [BrowserVisualComparison](docs/BrowserVisualComparison.md)
- [BrowserVisualComparisonStatus](docs/BrowserVisualComparisonStatus.md)
- [BrowserVisualComparisonSummary](docs/BrowserVisualComparisonSummary.md)
- [BrowserVisualDecisionStatus](docs/BrowserVisualDecisionStatus.md)
- [BrowserVisualDiffRegion](docs/BrowserVisualDiffRegion.md)
- [BrowserVisualExcludeAndRecompareRequest](docs/BrowserVisualExcludeAndRecompareRequest.md)
- [BrowserVisualExcludedRegion](docs/BrowserVisualExcludedRegion.md)
- [BrowserVisualKeepRegressionRequest](docs/BrowserVisualKeepRegressionRequest.md)
- [BrowserVisualPromoteBaselineRequest](docs/BrowserVisualPromoteBaselineRequest.md)
- [BrowserVisualReviewCapabilities](docs/BrowserVisualReviewCapabilities.md)
- [BrowserVisualReviewCapability](docs/BrowserVisualReviewCapability.md)
- [BrowserVisualScopeType](docs/BrowserVisualScopeType.md)
- [BrowserVisualStopPolicy](docs/BrowserVisualStopPolicy.md)
- [CompiledSpecification](docs/CompiledSpecification.md)
- [ContentFormat](docs/ContentFormat.md)
- [CraftsmanRun](docs/CraftsmanRun.md)
- [CraftsmanRunAccepted](docs/CraftsmanRunAccepted.md)
- [CraftsmanRunState](docs/CraftsmanRunState.md)
- [CraftsmanStreamingRunInput](docs/CraftsmanStreamingRunInput.md)
- [DocumentAssetReference](docs/DocumentAssetReference.md)
- [DocumentAttachmentAssertionBaseline](docs/DocumentAttachmentAssertionBaseline.md)
- [DocumentVisualAssertion](docs/DocumentVisualAssertion.md)
- [DocumentVisualAssertionPage](docs/DocumentVisualAssertionPage.md)
- [DocumentVisualDiff](docs/DocumentVisualDiff.md)
- [DocumentVisualDiffBaselinePreview](docs/DocumentVisualDiffBaselinePreview.md)
- [DocumentVisualDiffBaselineRequest](docs/DocumentVisualDiffBaselineRequest.md)
- [DocumentVisualDiffCaptureRunRequest](docs/DocumentVisualDiffCaptureRunRequest.md)
- [DocumentVisualDiffDecision](docs/DocumentVisualDiffDecision.md)
- [DocumentVisualDiffGeneration](docs/DocumentVisualDiffGeneration.md)
- [DocumentVisualDiffPage](docs/DocumentVisualDiffPage.md)
- [DocumentVisualDiffRegenerateRequest](docs/DocumentVisualDiffRegenerateRequest.md)
- [DocumentVisualDiffStatus](docs/DocumentVisualDiffStatus.md)
- [DocumentVisualExcludedRegion](docs/DocumentVisualExcludedRegion.md)
- [Flow](docs/Flow.md)
- [FlowDocumentVisualDiffCaptureRunRequest](docs/FlowDocumentVisualDiffCaptureRunRequest.md)
- [FlowInput](docs/FlowInput.md)
- [FlowPage](docs/FlowPage.md)
- [FlowRecoveryBinding](docs/FlowRecoveryBinding.md)
- [FlowRecoveryCurrentDependency](docs/FlowRecoveryCurrentDependency.md)
- [FlowRecoveryCurrentDependencySource](docs/FlowRecoveryCurrentDependencySource.md)
- [FlowRecoveryDependency](docs/FlowRecoveryDependency.md)
- [FlowRecoveryDependencyDetail](docs/FlowRecoveryDependencyDetail.md)
- [FlowRecoveryDependencyPage](docs/FlowRecoveryDependencyPage.md)
- [FlowRecoveryDraftInput](docs/FlowRecoveryDraftInput.md)
- [FlowRecoveryHistoricalDefinition](docs/FlowRecoveryHistoricalDefinition.md)
- [FlowRecoveryInput](docs/FlowRecoveryInput.md)
- [FlowRecoveryOccurrence](docs/FlowRecoveryOccurrence.md)
- [FlowRecoveryOperation](docs/FlowRecoveryOperation.md)
- [FlowRecoveryPreview](docs/FlowRecoveryPreview.md)
- [FlowRecoveryProjection](docs/FlowRecoveryProjection.md)
- [FlowRecoveryReview](docs/FlowRecoveryReview.md)
- [FlowRun](docs/FlowRun.md)
- [FlowRunPage](docs/FlowRunPage.md)
- [FlowRunStep](docs/FlowRunStep.md)
- [FlowRunSummary](docs/FlowRunSummary.md)
- [FlowStep](docs/FlowStep.md)
- [FlowStepInput](docs/FlowStepInput.md)
- [FlowSummary](docs/FlowSummary.md)
- [Fragment](docs/Fragment.md)
- [FragmentAssembly](docs/FragmentAssembly.md)
- [FragmentCatalog](docs/FragmentCatalog.md)
- [FragmentCatalogType](docs/FragmentCatalogType.md)
- [FragmentDraftAssembly](docs/FragmentDraftAssembly.md)
- [FragmentDraftInput](docs/FragmentDraftInput.md)
- [FragmentInput](docs/FragmentInput.md)
- [FragmentPage](docs/FragmentPage.md)
- [FragmentSummary](docs/FragmentSummary.md)
- [FragmentSummaryCounts](docs/FragmentSummaryCounts.md)
- [FragmentType](docs/FragmentType.md)
- [OpenApiGenerationResult](docs/OpenApiGenerationResult.md)
- [PageMetadata](docs/PageMetadata.md)
- [ProblemDetails](docs/ProblemDetails.md)
- [RequestChainRun](docs/RequestChainRun.md)
- [RequestChainRunInput](docs/RequestChainRunInput.md)
- [RequestNode](docs/RequestNode.md)
- [RequestNodeInput](docs/RequestNodeInput.md)
- [RequestWorkspace](docs/RequestWorkspace.md)
- [RequestWorkspaceInput](docs/RequestWorkspaceInput.md)
- [RequestWorkspacePage](docs/RequestWorkspacePage.md)
- [RunBatch](docs/RunBatch.md)
- [RunBatchInput](docs/RunBatchInput.md)
- [RunBatchItem](docs/RunBatchItem.md)
- [RunBatchPage](docs/RunBatchPage.md)
- [RunEnqueueResponse](docs/RunEnqueueResponse.md)
- [RunFlowBatchRequest](docs/RunFlowBatchRequest.md)
- [RunStatus](docs/RunStatus.md)
- [SavedRequestInput](docs/SavedRequestInput.md)
- [SentinelCheck](docs/SentinelCheck.md)
- [SentinelCheckInput](docs/SentinelCheckInput.md)
- [SentinelCheckPage](docs/SentinelCheckPage.md)
- [SentinelDashboardSummary](docs/SentinelDashboardSummary.md)
- [SentinelIncident](docs/SentinelIncident.md)
- [SentinelLinkSummary](docs/SentinelLinkSummary.md)
- [SentinelLinkSummaryPage](docs/SentinelLinkSummaryPage.md)
- [SentinelLinkedAssetCheckType](docs/SentinelLinkedAssetCheckType.md)
- [SentinelRun](docs/SentinelRun.md)
- [SentinelRunBaseline](docs/SentinelRunBaseline.md)
- [SentinelRunPage](docs/SentinelRunPage.md)
- [Snapshot](docs/Snapshot.md)
- [SnapshotDiff](docs/SnapshotDiff.md)
- [SnapshotDiffChangeType](docs/SnapshotDiffChangeType.md)
- [SnapshotDiffEntry](docs/SnapshotDiffEntry.md)
- [SnapshotInput](docs/SnapshotInput.md)
- [SnapshotItem](docs/SnapshotItem.md)
- [SnapshotPage](docs/SnapshotPage.md)
- [SnapshotSelectionPolicy](docs/SnapshotSelectionPolicy.md)
- [SnapshotSourceRunType](docs/SnapshotSourceRunType.md)
- [SnapshotStatus](docs/SnapshotStatus.md)
- [SnapshotStepDiff](docs/SnapshotStepDiff.md)
- [SnapshotStepDiffGroup](docs/SnapshotStepDiffGroup.md)
- [SnapshotStepDiffInput](docs/SnapshotStepDiffInput.md)
- [SnapshotStepDiffItem](docs/SnapshotStepDiffItem.md)
- [SnapshotStepDiffSection](docs/SnapshotStepDiffSection.md)
- [SnapshotStepType](docs/SnapshotStepType.md)
- [SnapshotSubjectType](docs/SnapshotSubjectType.md)
- [SpecGenerationResult](docs/SpecGenerationResult.md)
- [SpecType](docs/SpecType.md)
- [Specification](docs/Specification.md)
- [SpecificationPage](docs/SpecificationPage.md)
- [SpecificationRecoveryChange](docs/SpecificationRecoveryChange.md)
- [SpecificationRecoveryPreview](docs/SpecificationRecoveryPreview.md)
- [SpecificationRun](docs/SpecificationRun.md)
- [SpecificationRunPage](docs/SpecificationRunPage.md)
- [SpecificationRunSummary](docs/SpecificationRunSummary.md)
- [SpecificationSummary](docs/SpecificationSummary.md)
- [StreamingCapabilities](docs/StreamingCapabilities.md)
- [StreamingDefinition](docs/StreamingDefinition.md)
- [StreamingDefinitionStream](docs/StreamingDefinitionStream.md)
- [StreamingDraftValidation](docs/StreamingDraftValidation.md)
- [StreamingLimits](docs/StreamingLimits.md)
- [StreamingRun](docs/StreamingRun.md)
- [StreamingRunAccepted](docs/StreamingRunAccepted.md)
- [StreamingRunOutcome](docs/StreamingRunOutcome.md)
- [StreamingRunPage](docs/StreamingRunPage.md)
- [StreamingRunState](docs/StreamingRunState.md)
- [StreamingSpecification](docs/StreamingSpecification.md)
- [StreamingSpecificationPage](docs/StreamingSpecificationPage.md)
- [StreamingSpecificationSummary](docs/StreamingSpecificationSummary.md)
- [StreamingTranscriptPage](docs/StreamingTranscriptPage.md)
- [StreamingTransport](docs/StreamingTransport.md)

### Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
#### BearerAuth


- **Type**: HTTP Bearer Token authentication (JWT)

## About

This TypeScript SDK client supports the [Fetch API](https://fetch.spec.whatwg.org/)
and is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1.0.0-alpha.7`
- Package version: `0.1.0`
- Generator version: `7.22.0`
- Build package: `org.openapitools.codegen.languages.TypeScriptFetchClientCodegen`

The generated npm module supports the following:

- Environments
  * Node.js
  * Webpack
  * Browserify
- Language levels
  * ES5 - you must have a Promises/A+ library installed
  * ES6
- Module systems
  * CommonJS
  * ES6 module system

For more information, please visit [https://ste.software](https://ste.software)

## Development

### Building

To build the TypeScript source code, you need to have Node.js and npm installed.
After cloning the repository, navigate to the project directory and run:

```bash
npm install
npm run build
```

### Publishing

Once you've built the package, you can publish it to npm:

```bash
npm publish
```

## License

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
