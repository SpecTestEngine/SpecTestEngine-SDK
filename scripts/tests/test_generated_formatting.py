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

    def test_normalization_is_idempotent(self):
        content = module.normalize_generated_whitespace("first\r\n\r\n")
        self.assertEqual(module.normalize_generated_whitespace(content), content)


if __name__ == "__main__":
    unittest.main()
