import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from network_traffic_analyzer import NetworkTrafficAnalyzer

class TestNetworkTrafficAnalyzer(unittest.TestCase):
    def test_get_network_stats(self):
        nta = NetworkTrafficAnalyzer()
        stats = nta.get_network_stats()
        self.assertIsInstance(stats, dict)

if __name__ == '__main__':
    unittest.main()
