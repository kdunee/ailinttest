import unittest
from intentguard import IntentGuard, IntentGuardOptions


class TestIntentGuard(unittest.TestCase):
    def setUp(self):
        self.options = IntentGuardOptions(quorum_size=3)
        self.guard = IntentGuard(self.options)

    def test_assert_code_true(self):
        self.guard.assert_code(
            "{class} should provide a functionality of verifying code properties through natural language assertions",
            {"class": IntentGuard},
        )

    def test_assert_code_false(self):
        with self.assertRaises(AssertionError):
            self.guard.assert_code(
                "{class} should not have any methods", {"class": IntentGuard}
            )

    def test_guard_options(self):
        self.guard.assert_code(
            "{options} should have a quorum_size field",
            {"options": IntentGuardOptions},
        )

    def test_assert_code_with_multiple_objects(self):
        self.guard.assert_code(
            "{class} should use the quorum_size field from {options} to perform multiple inferences",
            {
                "class": IntentGuard,
                "options": IntentGuardOptions,
            },
        )

    def test_different_quorum_sizes(self):
        for quorum_size in [1, 5, 10]:
            options = IntentGuardOptions(quorum_size=quorum_size)
            guard = IntentGuard(options)
            guard.assert_code(
                "{class} should work with different quorum sizes",
                {"class": IntentGuard},
            )

    def test_custom_options(self):
        custom_options = IntentGuardOptions(quorum_size=5, model="gpt-4o-mini")
        self.guard.assert_code(
            "{class} should accept custom options",
            {"class": IntentGuard},
            options=custom_options,
        )


if __name__ == "__main__":
    unittest.main()
