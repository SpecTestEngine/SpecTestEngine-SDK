import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "postprocess_generated", Path(__file__).resolve().parents[1] / "postprocess-generated.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class GeneratedFormattingTest(unittest.TestCase):
    def test_removes_extra_empty_eof_lines_and_trailing_spaces(self):
        self.assertEqual(module.normalize_generated_whitespace("class A {}  \n\n\n"), "class A {}\n")

    def test_keeps_internal_blank_lines_and_tokens(self):
        content = "first\n\nsecond\n"
        self.assertEqual(module.normalize_generated_whitespace(content), content)

    def test_does_not_add_a_missing_newline(self):
        self.assertEqual(module.normalize_generated_whitespace("version"), "version")

    def test_restores_only_exact_engine_wire_literals(self):
        source = '\"- -- -- -- -- -- -- -- -PASS- -- -- -- -- -- -- -- -- --\"'
        self.assertEqual(module.restore_engine_status_literals(source), '\"----------------PASS-------------------\"')
        for literal in ('"PASS"', '"FAILED"', '"my - -- value"'):
            self.assertEqual(module.restore_engine_status_literals(literal), literal)

    def test_optional_enum_serialization_requires_presence(self):
        original = '            var policyRawValue = Model.PolicyEnumToJsonValue(model.PolicyOption.Value!.Value);\n            writer.WriteString("policy", policyRawValue);'
        result = module.preserve_optional_csharp_enums(original)
        self.assertIn("if (model.PolicyOption.IsSet)", result)
        self.assertIn('writer.WriteNull("policy")', result)
        self.assertEqual(module.preserve_optional_csharp_enums(result), result)

    def test_normalization_is_idempotent(self):
        content = module.normalize_generated_whitespace("first\r\n\r\n")
        self.assertEqual(module.normalize_generated_whitespace(content), content)


if __name__ == "__main__":
    unittest.main()
