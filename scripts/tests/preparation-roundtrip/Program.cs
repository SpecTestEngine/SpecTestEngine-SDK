using System;
using System.Text.Json;
using System.Text.Json.Nodes;
using SpecTestEngine.Sdk.Model;
var options=new JsonSerializerOptions();
options.Converters.Add(new BrowserPathExpectationJsonConverter());
options.Converters.Add(new BrowserNetworkExpectationJsonConverter());
options.Converters.Add(new PreparationSummaryJsonConverter());
options.Converters.Add(new PreparationOutputJsonConverter());
foreach(var protocol in new[]{"REST","SOAP","GRAPHQL","STREAMING"}) {
 var wire="{\"id\":\"019f9400-0000-7000-8000-000000000001\",\"stableKey\":\"login\",\"name\":\"Login\",\"protocol\":\""+protocol+"\",\"outputs\":{\"accessToken\":{\"path\":\"/accessToken\",\"type\":\"string\",\"required\":true}}}";
 var encoded=JsonSerializer.Serialize(JsonSerializer.Deserialize<PreparationSummary>(wire,options),options);
 if(!JsonNode.DeepEquals(JsonNode.Parse(wire),JsonNode.Parse(encoded)))throw new Exception("Preparation round trip changed "+protocol);
}
foreach(var status in new[]{"----------------PASS-------------------","----------------FAIL-------------------","---------------ERROR-------------------"})
 if(RunStatusValueConverter.ToJsonValue(RunStatusValueConverter.FromString(status))!=status)throw new Exception("Engine verdict changed");
Console.WriteLine("Preparation and engine verdict round trips passed for four protocols.");

foreach(var wire in new[]{"{\"path\":\"/x\",\"value\":null}","{\"path\":\"/x\",\"value\":false}","{\"path\":\"/x\",\"value\":7}","{\"path\":\"/x\",\"pattern\":\"foo*\"}"}) {
 var encoded=JsonSerializer.Serialize(JsonSerializer.Deserialize<BrowserPathExpectation>(wire,options),options);
 if(!JsonNode.DeepEquals(JsonNode.Parse(wire),JsonNode.Parse(encoded)))throw new Exception("Path operand presence changed");
}

foreach(var wire in new[]{"{\"headers\":{\"accept\":\"application/json\"}}","{\"body\":null}","{\"candidateBody\":null}","{\"expectedBody\":null}","{\"expectedBody\":false}","{\"expectedBody\":7}","{\"expectedBody\":\"123\"}"}) {
 var encoded=JsonSerializer.Serialize(JsonSerializer.Deserialize<BrowserNetworkExpectation>(wire,options),options);
 if(!JsonNode.DeepEquals(JsonNode.Parse(wire),JsonNode.Parse(encoded)))throw new Exception("Whole body presence changed");
}
