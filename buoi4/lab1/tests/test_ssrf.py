import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scanners.ssrf_tester import SSRFTester

class TestSSRFTester(unittest.TestCase):
    def setUp(self):
        self.tester = SSRFTester()

    def test_detect_ssrf(self):
        url = "http://example.com/fetch?url=http://127.0.0.1/admin"
        findings = self.tester.scan(url)
        self.assertTrue(any(f['param'] == 'url' and 'SSRF' in f['desc'] for f in findings))

    def test_no_ssrf(self):
        url = "http://example.com/fetch?url=http://example.com"
        findings = self.tester.scan(url)
        self.assertEqual(findings, [])

if __name__ == '__main__':
    unittest.main()
