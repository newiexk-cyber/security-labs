import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from security_behavior_checker import SecurityBehaviorChecker

class TestSecurityBehaviorChecker(unittest.TestCase):
    def test_suspicious_calls(self):
        sbc = SecurityBehaviorChecker()
        self.assertIsInstance(sbc.suspicious_calls(), list)

if __name__ == '__main__':
    unittest.main()
