package software.ste.sdk.generated.model;
import org.junit.jupiter.api.Test;
import software.ste.sdk.generated.JSON;
import static org.junit.jupiter.api.Assertions.assertEquals;
class PreparationContractTest {
 @Test void preservesEveryNativeProtocolAndTypedOutputContract() throws Exception {
  var mapper=new JSON().getMapper();
  for(var protocol:new String[]{"REST","SOAP","GRAPHQL","STREAMING"}){
   var wire="{\"id\":\"019f9400-0000-7000-8000-000000000001\",\"stableKey\":\"login\",\"name\":\"Login\",\"protocol\":\""+protocol+"\",\"outputs\":{\"accessToken\":{\"path\":\"/accessToken\",\"type\":\"string\",\"required\":true}}}";
   assertEquals(mapper.readTree(wire),mapper.valueToTree(mapper.readValue(wire,PreparationSummary.class)));
  }
  for(var status:new String[]{"----------------PASS-------------------","----------------FAIL-------------------","---------------ERROR-------------------"})
   assertEquals(status,mapper.readValue(mapper.writeValueAsString(RunStatus.fromValue(status)),String.class));
 }
 @Test void preservesTypedPathOperandsAndPatternAbsence() throws Exception {
  var mapper=new JSON().getMapper();
  for(var operand:new String[]{"null","false","7","\"123\""}) {
   var wire="{\"path\":\"/x\",\"value\":"+operand+"}";
   assertEquals(mapper.readTree(wire),mapper.valueToTree(mapper.readValue(wire,BrowserPathExpectation.class)));
  }
  var pattern="{\"path\":\"/x\",\"pattern\":\"foo*\"}";
  assertEquals(mapper.readTree(pattern),mapper.valueToTree(mapper.readValue(pattern,BrowserPathExpectation.class)));
  assertEquals(mapper.readTree("{\"path\":\"/x\",\"value\":null}"),mapper.valueToTree(new BrowserPathExpectation().path("/x").value(null)));
 }
 @Test void preservesWholeBodyNullAndAbsence() throws Exception {
  var mapper=new JSON().getMapper();
  for(var wire:new String[]{"{\"headers\":{\"accept\":\"application/json\"}}","{\"body\":null}","{\"candidateBody\":null}","{\"expectedBody\":null}","{\"expectedBody\":false}","{\"expectedBody\":7}","{\"expectedBody\":\"123\"}"})
   assertEquals(mapper.readTree(wire),mapper.valueToTree(mapper.readValue(wire,BrowserNetworkExpectation.class)));
 }
 @Test void preservesNestedJsonNullMembers() throws Exception {
  var mapper=new JSON().getMapper();
  var wire="{\"expectedBody\":{\"nested\":null,\"items\":[null,{\"child\":null}]}}";
  assertEquals(mapper.readTree(wire),mapper.valueToTree(mapper.readValue(wire,BrowserNetworkExpectation.class)));
 }
}
