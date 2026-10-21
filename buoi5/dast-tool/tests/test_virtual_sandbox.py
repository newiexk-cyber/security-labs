import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from virtual_sandbox import VirtualSandbox

class TestVirtualSandbox(unittest.TestCase):
    def test_run_isolated(self):
        vs = VirtualSandbox()
        out, err = vs.run_isolated("echo test")
        self.assertIn("test", out)
        self.assertEqual(err, "")

if __name__ == '__main__':
    unittest.main()
