# Created with Openapi Generator

<a id="cli"></a>
## Creating the library
Create a config.yaml file similar to what is below, then run the following powershell command to generate the library `java -jar "<path>/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar" generate -c config.yaml`

```yaml
generatorName: csharp
inputSpec: /workspace/openapi/spectestengine-public-v1.yaml
outputDir: out

# https://openapi-generator.tech/docs/generators/csharp
additionalProperties:
  packageGuid: '{C3ADD0DC-40C4-4556-B8EE-250F941D91A4}'

# https://openapi-generator.tech/docs/integrations/#github-integration
# gitHost:
# gitUserId:
# gitRepoId:

# https://openapi-generator.tech/docs/globals
# globalProperties:

# https://openapi-generator.tech/docs/customization/#inline-schema-naming
# inlineSchemaOptions:

# https://openapi-generator.tech/docs/customization/#name-mapping
# modelNameMappings:
# nameMappings:

# https://openapi-generator.tech/docs/customization/#openapi-normalizer
# openapiNormalizer:

# templateDir: https://openapi-generator.tech/docs/templating/#modifying-templates

# releaseNote:
```

<a id="usage"></a>
## Using the library in your project

```cs
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;
using SpecTestEngine.Sdk.Api;
using SpecTestEngine.Sdk.Client;
using SpecTestEngine.Sdk.Model;
using Org.OpenAPITools.Extensions;

namespace YourProject
{
    public class Program
    {
        public static async Task Main(string[] args)
        {
            var host = CreateHostBuilder(args).Build();
            var api = host.Services.GetRequiredService<IBrowserVisualReviewsApi>();
            IExcludeBrowserVisualAreaAndRecompareApiResponse apiResponse = await api.ExcludeBrowserVisualAreaAndRecompareAsync("todo");
            BrowserVisualComparison? model = apiResponse.Ok();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) => Host.CreateDefaultBuilder(args)
          .ConfigureApi((context, services, options) =>
          {
              // The type of token here depends on the api security specifications
              // Available token types are ApiKeyToken, BasicToken, BearerToken, HttpSigningToken, and OAuthToken.
              BearerToken token = new("<your token>");
              options.AddTokens(token);

              // optionally choose the method the tokens will be provided with, default is RateLimitProvider
              options.UseProvider<RateLimitProvider<BearerToken>, BearerToken>();

              options.ConfigureJsonOptions((jsonOptions) =>
              {
                  // your custom converters if any
              });

              options.AddApiHttpClients(client =>
              {
                  // client configuration
              }, builder =>
              {
                  builder
                      .AddRetryPolicy(2)
                      .AddTimeoutPolicy(TimeSpan.FromSeconds(5))
                      .AddCircuitBreakerPolicy(10, TimeSpan.FromSeconds(30));
                      // add whatever middleware you prefer
                  }
              );
          });
    }
}
```
<a id="questions"></a>
## Questions

- What about HttpRequest failures and retries?
  Configure Polly in the IHttpClientBuilder
- How are tokens used?
  Tokens are provided by a TokenProvider class. The default is RateLimitProvider which will perform client side rate limiting.
  Other providers can be used with the UseProvider method.
- Does an HttpRequest throw an error when the server response is not Ok?
  It depends how you made the request. If the return type is ApiResponse<T> no error will be thrown, though the Content property will be null.
  StatusCode and ReasonPhrase will contain information about the error.
  If the return type is T, then it will throw. If the return type is TOrDefault, it will return null.
- How do I validate requests and process responses?
  Use the provided On and After partial methods in the api classes.

## Api Information
- appName: SpecTestEngine Public API
- appVersion: 1.0.0-alpha.7
- appDescription: The versioned integration contract for creating, running, observing, and exporting SpecTestEngine test assets. The API is project-scoped: the bearer token selects the company and active project, and clients must not send internal owner identifiers.  Every operation requires a short-lived OAuth 2.0 bearer access token. Interactive integrations use Authorization Code with PKCE; CI and server-to-server integrations use Client Credentials. A SpecTestEngine company administrator registers the integration and approves capabilities through the Integration Builder. The builder offers only capabilities included in the company&#39;s subscription and maps the selection to token scopes. A valid token cannot enable a capability outside the current subscription. Generate or browse an SDK without credentials, then provide a token only when calling the API. See the SDK authentication guide for the complete public procedure.  This alpha contract covers stable request/response workflows plus the bounded asynchronous lifecycle for WebSocket/WSS, SSE, gRPC Streaming, and MQTT tests. Interactive browser recording, MCP tools, and AI conversations are documented separately. Browser visual comparison review is exposed as a bounded preview workflow; live WebRTC transport and worker coordination remain internal implementation details.

## Build
This C# SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project.

- SDK version: 0.1.0
- Generator version: 7.22.0
- Build package: org.openapitools.codegen.languages.CSharpClientCodegen
