package spectestengine

import("encoding/json";"testing")
func TestPreparationProtocolAndOutputRoundTrip(t *testing.T){
 for _,protocol:=range []string{"REST","SOAP","GRAPHQL","STREAMING"}{
  wire:=`{"id":"019f9400-0000-7000-8000-000000000001","stableKey":"login","name":"Login","protocol":"`+protocol+`","outputs":{"accessToken":{"path":"/accessToken","type":"string","required":true},"count":{"path":"/count","type":"number","required":false}}}`
  var model PreparationSummary
  if err:=json.Unmarshal([]byte(wire),&model);err!=nil{t.Fatal(err)}
  encoded,err:=json.Marshal(model);if err!=nil{t.Fatal(err)}
  var expected,actual interface{};json.Unmarshal([]byte(wire),&expected);json.Unmarshal(encoded,&actual)
  a,_:=json.Marshal(expected);b,_:=json.Marshal(actual);if string(a)!=string(b){t.Fatalf("round trip changed %s",protocol)}
 }
}

func TestPathOperandPresenceRoundTrip(t *testing.T) {
 for _,wire:=range []string{`{"path":"/x","value":null}`,`{"path":"/x","value":false}`,`{"path":"/x","value":7}`,`{"path":"/x","value":"123"}`,`{"path":"/x","pattern":"foo*"}`} {
  var model BrowserPathExpectation
  if err:=json.Unmarshal([]byte(wire),&model);err!=nil{t.Fatal(err)}
  encoded,err:=json.Marshal(model);if err!=nil{t.Fatal(err)}
  var want,got interface{};json.Unmarshal([]byte(wire),&want);json.Unmarshal(encoded,&got)
  a,_:=json.Marshal(want);b,_:=json.Marshal(got);if string(a)!=string(b){t.Fatalf("operand changed: %s -> %s",wire,encoded)}
 }
 model:=NewBrowserPathExpectation("/x");model.SetValue(nil);encoded,_:=json.Marshal(model)
 var fields map[string]interface{};json.Unmarshal(encoded,&fields);if _,ok:=fields["value"];!ok{t.Fatal("SetValue(nil) lost explicit null")}
}

func TestWholeBodyPresenceRoundTrip(t *testing.T) {
 for _,wire:=range []string{`{"headers":{"accept":"application/json"}}`,`{"body":null}`,`{"candidateBody":null}`,`{"expectedBody":null}`,`{"expectedBody":false}`,`{"expectedBody":7}`,`{"expectedBody":"123"}`} {
  var model BrowserNetworkExpectation
  if err:=json.Unmarshal([]byte(wire),&model);err!=nil{t.Fatal(err)}
  encoded,err:=json.Marshal(model);if err!=nil{t.Fatal(err)}
  var want,got interface{};json.Unmarshal([]byte(wire),&want);json.Unmarshal(encoded,&got)
  a,_:=json.Marshal(want);b,_:=json.Marshal(got);if string(a)!=string(b){t.Fatalf("body presence changed: %s -> %s",wire,encoded)}
 }
}
