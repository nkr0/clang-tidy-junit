"""tests for clang_tidy_junit"""

import filecmp
import tempfile
import unittest
import clang_tidy_junit as ctj


class TestClangTidyJunit(unittest.TestCase):
    """unittest class for clang_tidy_junit"""

    def test_junit(self) -> None:
        """test output junit files"""
        with tempfile.TemporaryDirectory() as d:
            for f in range(3):
                with self.subTest(f):
                    f1 = f"tests/samples/{f}"
                    f2 = f"{d}/{f}"
                    print(f1, f2)
                    ctj.process(f"{f1}.log", f"{f2}.xml")
                    assert filecmp.cmp(f"{f1}.xml", f"{f2}.xml", shallow=False)


if __name__ == "__main__":
    unittest.main()
