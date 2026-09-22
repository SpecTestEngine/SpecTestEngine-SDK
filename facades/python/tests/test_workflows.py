import unittest

from spectestengine_workflows import iter_sse, poll_workflow


class WorkflowSupportTest(unittest.TestCase):
    def test_poll_returns_terminal_value(self) -> None:
        values = iter([1, 2, 3])
        self.assertEqual(
            3,
            poll_workflow(
                lambda: next(values),
                lambda value: value == 3,
                interval_seconds=0.001,
                max_interval_seconds=0.001,
                timeout_seconds=1,
                backoff=1,
            ),
        )

    def test_sse_preserves_multiline_data(self) -> None:
        events = list(iter_sse(["event: progress\n", "data: first\n", "data: second\n", "\n"]))
        self.assertEqual("first\nsecond", events[0].data)


if __name__ == "__main__":
    unittest.main()
