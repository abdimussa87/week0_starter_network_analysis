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

    def test_slack_parser(self):
        all_week_1_path = os.path.join("../anonymized", 'all-week1/')
        week_1_df = self.data_loader.slack_parser(all_week_1_path)
        expected_columns = ['msg_type', 'msg_content', 'sender_name','sender_name','sender_name','time_thread_start','reply_count','reply_users_count','reply_users','tm_thread_end','channel']
        self.assertListEqual(list(week_1_df.columns), expected_columns)

   

   

if __name__ == '__main__':
    unittest.main()