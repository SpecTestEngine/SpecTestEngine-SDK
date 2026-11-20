"""Native alpha10 model round trips; run with the generated client's declared dependencies installed."""
import json
import unittest
from spectestengine_sdk.models.preparation_summary import PreparationSummary
from spectestengine_sdk.models.run_status import RunStatus

class PreparationModelContract(unittest.TestCase):
    def test_native_protocols_and_typed_outputs(self):
        for protocol in ("REST", "SOAP", "GRAPHQL", "STREAMING"):
            wire={"id":"019f9400-0000-7000-8000-000000000001", "stableKey":"login", "name":"Login", "protocol":protocol,
                  "outputs":{"accessToken":{"path":"/accessToken", "type":"string", "required":True},
                             "count":{"path":"/count", "type":"number", "required":False}}}
            self.assertEqual(wire, json.loads(PreparationSummary.from_json(json.dumps(wire)).to_json()))
    def test_exact_engine_verdicts(self):
        for status in ("----------------PASS-------------------", "----------------FAIL-------------------", "---------------ERROR-------------------"):
            self.assertEqual(status, RunStatus(status).value)

class PathOperandPresenceTest(unittest.TestCase):
    def test_typed_operands_and_absent_value(self):
        from spectestengine_sdk.models.browser_path_expectation import BrowserPathExpectation
        for operand in (None, False, 7, "123"):
            wire = {"path": "/x", "value": operand}
            self.assertEqual(wire, BrowserPathExpectation.from_dict(wire).to_dict())
        wire = {"path": "/x", "pattern": "foo*"}
        self.assertEqual(wire, BrowserPathExpectation.from_dict(wire).to_dict())

class WholeBodyPresenceTest(unittest.TestCase):
    def test_absent_and_explicit_null_bodies(self):
        from spectestengine_sdk.models.browser_network_expectation import BrowserNetworkExpectation
        for wire in ({"headers":{"accept":"application/json"}}, {"body":None}, {"candidateBody":None}, {"expectedBody":None}, {"expectedBody":False}, {"expectedBody":7}, {"expectedBody":"123"}):
            self.assertEqual(wire, BrowserNetworkExpectation.from_dict(wire).to_dict())
