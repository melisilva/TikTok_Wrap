import unittest
import pandas as pd
from datetime import datetime

# Import your functions from the script
from crud import top_following, total_minutes, top_hashtag

class TestYourFunctions(unittest.TestCase):

    #Date,Link,Username,Description,Hashtags,Sound Name,Sound Link


    def setUp(self):
        # Create sample data for testing
        self.sample_history_data = {
            'Date': ['2023-12-01 10:00:00', '2023-12-01 12:30:00', '2023-12-01 15:45:00'],
            'Link': ['https://www.tiktokv.com/share/video/7283922901265419563/', "https://www.tiktokv.com/share/video/7283618975903255854/", "https://www.tiktokv.com/share/video/7283618975903255809/"],
            'Username': ['user1', 'user2', 'user3'],
            'Description': ['text1', 'text2', 'text3'],
            'Hashtags': ['tag1', 'tag2', 'tag3'],
            'Sound Name': ['sound1', 'sound2', 'sound3'],
            'Sound Link': ['www.tiktok.com/music/original-sound-7283922937491589930', 'www.tiktok.com/music/I-Can-See-You-Taylor%E2%80%99s-Version-From-The-Vault-7252896191606999041', 'www.tiktok.com/music/This-Will-Be-An-Everlasting-Love-6926839226684147714']
        }

        self.sample_likes_data = {
            'Date': ['2023-12-01 10:30:00', '2023-12-01 13:00:00', '2023-12-01 16:00:00'],
            'Username': ['user4', 'user3', 'user2'],
            # Add other required columns in the likes DataFrame
        }

        # Create DataFrames
        self.sample_history = pd.DataFrame(self.sample_history_data)
        self.sample_likes = pd.DataFrame(self.sample_likes_data)

    def test_top_following(self):
        # Call the function with the sample data
        result = top_following(self.sample_history)

        # Check if the result is a DataFrame and has the expected columns
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(all(col in result.columns for col in ['Username', 'Count']))

    def test_total_minutes(self):
        # Call the function with the sample data
        result = total_minutes()

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(all(key in result for key in ['Minutes', 'Quote']))

    def test_top_hashtag(self):
        # Call the function with the sample data
        result = top_hashtag(False)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(all(key in result for key in ['Hashtag', 'Count', 'Photo']))

if __name__ == '__main__':
    unittest.main()
