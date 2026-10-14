import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scanners.sql_injection_tester import SQLInjectionTester

class TestSQLInjectionTester(unittest.TestCase):
    def setUp(self):
        self.scanner = SQLInjectionTester()

    def test_detect_sql_injection(self):
        url = "http://example.com/page?id=' OR '1'='1"
        findings = self.scanner.scan(url)
        self.assertTrue(any(f['param'] == 'id' and 'SQL Injection' in f['desc'] for f in findings))

    def test_no_vulnerability(self):
        url = "http://example.com/page?id=normalvalue"
        findings = self.scanner.scan(url)
        self.assertEqual(findings, [])

if __name__ == '__main__':
    unittest.main()
