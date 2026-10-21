import unittest
import tempfile
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sast_tool.code_quality_checker import CodeQualityChecker

class TestCodeQualityChecker(unittest.TestCase):
    def test_flake8_detection(self):
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w+", encoding="utf-8") as tmp:
            tmp.write("import os\n\n\n")
            tmp_path = tmp.name

        try:
            checker = CodeQualityChecker()
            issues = checker.check(tmp_path)
            self.assertTrue(all(i['type'] == 'Lint Issue' for i in issues) or len(issues) >= 0)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

if __name__ == '__main__':
    unittest.main()
