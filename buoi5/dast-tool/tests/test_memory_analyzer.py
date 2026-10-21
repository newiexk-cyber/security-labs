import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory_analyzer import MemoryAnalyzer

class TestMemoryAnalyzer(unittest.TestCase):
    def test_check_overflow(self):
        ma = MemoryAnalyzer()
        self.assertTrue(ma.check_overflow(2**64))
        self.assertFalse(ma.check_overflow(100))

if __name__ == '__main__':
    unittest.main()
