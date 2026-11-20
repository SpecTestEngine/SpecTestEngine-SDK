import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

VALIDATE = Path(__file__).resolve().parents[1] / 'validate-contract.py'

class ContractOperationCountTest(unittest.TestCase):
    def test_counts_only_path_operations_not_component_example_fields(self):
        contract = '''openapi: 3.0.3
paths:
  /test:
    get:
      operationId: readTest
      x-sdk-stability: stable
      x-idempotent: true
components:
  schemas:
    ProblemDetails:
      example:
        operationId: sampleField
  securitySchemes:
    BearerAuth:
      type: http
'''
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'contract.yaml'
            source.write_text(contract)
            result = subprocess.run([sys.executable, str(VALIDATE), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('1 operations', result.stdout)
