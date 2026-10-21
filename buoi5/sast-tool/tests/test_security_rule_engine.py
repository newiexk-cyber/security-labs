import unittest
import json
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sast_tool.security_rule_engine import SecurityRuleEngine

class TestSecurityRuleEngine(unittest.TestCase):
    def setUp(self):
        self.rules = [
            {"type": "Use of eval", "severity": "high"},
            {"type": "Pattern Match", "severity": "medium"}
        ]
        self.rules_file = os.path.join(os.path.dirname(__file__), "temp_rules.json")
        with open(self.rules_file, "w", encoding="utf-8") as f:
            json.dump(self.rules, f)
        self.engine = SecurityRuleEngine(self.rules_file)

    def tearDown(self):
        if os.path.exists(self.rules_file):
            os.remove(self.rules_file)

    def test_evaluate(self):
        ast_issues = [{"type": "Use of eval", "message": "msg", "lineno": 1, "col_offset": 0}]
        pattern_issues = [{"type": "Pattern Match", "message": "msg", "lineno": 2, "col_offset": 1}]
        results = self.engine.evaluate(ast_issues, pattern_issues)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['severity'], "high")
        self.assertEqual(results[1]['severity'], "medium")

if __name__ == '__main__':
    unittest.main()
