import unittest
import os, sys

# Add parent directory to path to import modules from src
rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)
    
from src.loader import SlackDataLoader

class TestSlackDataLoader(unittest.TestCase):

    def setUp(self):
        # Initialize SlackDataLoader with the path
        self.data_loader = SlackDataLoader("../anonymized")

    def test_get_channels(self):
        channels = self.data_loader.get_channels()
        expected_columns = ['id', 'name', 'created','creator','is_archived','is_general','members','topic','purpose']
        self.assertListEqual(list(channels.columns), expected_columns)

   

   

if __name__ == '__main__':
    unittest.main()