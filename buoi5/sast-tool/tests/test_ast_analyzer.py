import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sast_tool.ast_analyzer import ASTAnalyzer

class TestASTAnalyzer(unittest.TestCase):
    def test_eval_detection(self):
        code = "eval('2+2')"
        analyzer = ASTAnalyzer()
        issues = analyzer.analyze(code)
        self.assertTrue(any(i['type'] == 'Use of eval' for i in issues))

if __name__ == '__main__':
    unittest.main()
