import unittest
import pandas as pd
from datetime import datetime

# Import your functions from the script
import crud

class TestYourFunctions(unittest.TestCase):

    #Date,Link,Username,Description,Hashtags,Sound Name,Sound Link

    def setUp(self):
        # Create sample data for testing
        self.sample_history_data = {
            'Date': ['2023-12-01 10:00:00','2023-12-01 12:30:00','2023-12-01 15:45:00','2023-09-24 06:13:25','2023-09-28 07:38:44','2023-10-31 07:38:44','2023-09-27 19:26:51','2023-09-27 19:24:04','2023-12-02 08:15:00','2023-12-02 14:00:00','2023-12-03 09:30:00','2023-10-15 16:45:00','2023-10-18 20:12:30','2023-11-20 14:30:00','2023-09-25 22:10:15','2023-09-26 05:45:00','2023-09-26 13:20:00','2023-09-29 18:30:00','2023-09-29 21:45:00','2023-10-05 11:00:00','2023-10-08 07:30:00','2023-10-12 16:15:00','2023-11-05 22:00:00','2023-11-10 07:45:00','2023-11-15 13:20:00','2023-11-23 19:30:00','2023-11-25 07:05:00','2023-11-28 09:10:00','2023-12-05 14:55:00','2023-12-10 18:20:00'],
            'Link': ['link1', 'link2', 'link3', 'link4', 'link5', 'link6', 'link7', 'link8','link9','link10', 'link11','link12','link13','link14','link15', 'link16','link17','link18','link19','link20','link21','link22','link23','link24','link25','link26','link27','link28','link29','link30'],
            'Username': ['rory', 'batfamilyprotector', 'lily', 'lindsaybrookethomas','badwolf', 'rory', 'rory', 'lily','badwolf','rory', 'badwolf', 'lindsaybrookethomas', 'lindsaybrookethomas', 'rory', 'badwolf','ikeapt','tacobell','ikeapt','ikeapt','ikeapt','tacobell','ikeapt','tacobell','tacobell','disney','disney','disney','microsoft','microsoft','playstation'],
            'Description': ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9', 'text10', 'text11', 'text12', 'text13', 'text14','text15','text16','text17','text18','text19','text20','text21','text22','text23','text24','text25','text26','text27','text28','text29','text30'],
            'Hashtags': ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6','tag7','tag8','tag9', 'tag10','tag11','tag12','tag13','tag14','tag15','tag16','tag17','tag18','tag19','tag20','tag21','tag22','tag23','tag24','tag25','tag26','tag27','tag28','tag29','tag30'],
            'Sound Name': ['sound5', 'sound3','sound4','sound1','sound1','sound2','sound2','sound4','sound1','sound2','sound1','sound3','sound3','sound2','sound1','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music'],
            'Sound Link': ['www.tiktok.com/music/sound5', 'www.tiktok.com/music/sound3','www.tiktok.com/music/sound4', 'www.tiktok.com/music/sound1','www.tiktok.com/music/sound1', 'www.tiktok.com/music/sound2','www.tiktok.com/music/sound2', 'www.tiktok.com/music/sound4','www.tiktok.com/music/sound1', 'www.tiktok.com/music/sound2','www.tiktok.com/music/sound1','www.tiktok.com/music/sound3','www.tiktok.com/music/sound3','www.tiktok.com/music/sound2','www.tiktok.com/music/sound1','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/ikeapt','www.tiktok.com/music/ikeapt','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/tacobell','www.tiktok.com/music/disney','www.tiktok.com/music/disney','www.tiktok.com/music/disney','www.tiktok.com/music/microsoft','www.tiktok.com/music/microsoft','www.tiktok.com/music/playstation']
        }

        self.sample_likes_data = {
            'Date': ['2023-12-01 10:00:00','2023-12-01 12:30:00','2023-12-01 15:45:00','2023-09-24 06:13:25','2023-09-28 07:38:44','2023-10-31 07:38:44','2023-09-27 19:26:51','2023-09-27 19:24:04','2023-12-02 08:15:00','2023-12-02 14:00:00','2023-12-03 09:30:00','2023-10-15 16:45:00','2023-10-18 20:12:30','2023-11-20 14:30:00','2023-09-25 22:10:15','2023-09-26 05:45:00','2023-09-26 13:20:00','2023-09-29 18:30:00','2023-09-29 21:45:00','2023-10-05 11:00:00','2023-10-08 07:30:00','2023-10-12 16:15:00','2023-11-05 22:00:00','2023-11-10 07:45:00','2023-11-15 13:20:00','2023-11-23 19:30:00','2023-11-25 07:05:00','2023-11-28 09:10:00','2023-12-05 14:55:00','2023-12-10 18:20:00'],
            'Link': ['link1', 'link2', 'link3', 'link4', 'link5', 'link6', 'link7', 'link8','link9','link10', 'link11','link12','link13','link14','link15', 'link16','link17','link18','link19','link20','link21','link22','link23','link24','link25','link26','link27','link28','link29','link30'],
            'Username': ['badwolf','batfamilyprotector', 'emma', 'lindsaybrookethomas', 'badwolf','rory', 'rory', 'emma', 'badwolf','rory', 'badwolf', 'batfamilyprotector', 'batfamilyprotector', 'rory', 'badwolf','ikeapt','tacobell','ikeapt','ikeapt','ikeapt','tacobell','ikeapt','tacobell','tacobell','disney','disney','disney','microsoft','microsoft','playstation'],
            'Description': ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9', 'text10', 'text11', 'text12', 'text13', 'text14','text15','text16','text17','text18','text19','text20','text21','text22','text23','text24','text25','text26','text27','text28','text29','text30'],
            'Hashtags': ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6','tag7','tag8','tag9', 'tag10','tag11','tag12','tag13','tag14','tag15','tag16','tag17','tag18','tag19','tag20','tag21','tag22','tag23','tag24','tag25','tag26','tag27','tag28','tag29','tag30'],
            'Sound Name': ['sound5', 'sound6','sound4','sound1','sound2','sound2','sound2','sound4','sound1','sound2','sound1','sound6','sound6','sound2','sound1','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music'],
            'Sound Link': ['www.tiktok.com/music/sound5', 'www.tiktok.com/music/sound6','www.tiktok.com/music/sound4', 'www.tiktok.com/music/sound1','www.tiktok.com/music/sound2', 'www.tiktok.com/music/sound2','www.tiktok.com/music/sound2', 'www.tiktok.com/music/sound4','www.tiktok.com/music/sound1', 'www.tiktok.com/music/sound2','www.tiktok.com/music/sound1','www.tiktok.com/music/sound6','www.tiktok.com/music/sound6','www.tiktok.com/music/sound2','www.tiktok.com/music/sound1','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/ikeapt','www.tiktok.com/music/ikeapt','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/tacobell','www.tiktok.com/music/disney','www.tiktok.com/music/disney','www.tiktok.com/music/disney','www.tiktok.com/music/microsoft','www.tiktok.com/music/microsoft','www.tiktok.com/music/playstation']
        }

        self.sample_favorites_data = {
            'Date': ['2023-12-01 10:00:00','2023-12-01 12:30:00','2023-12-01 15:45:00','2023-09-24 06:13:25','2023-09-28 07:38:44','2023-10-31 07:38:44','2023-09-27 19:26:51','2023-09-27 19:24:04','2023-12-02 08:15:00','2023-12-02 14:00:00','2023-12-03 09:30:00','2023-10-15 16:45:00','2023-10-18 20:12:30','2023-11-20 14:30:00','2023-09-25 22:10:15','2023-09-26 05:45:00','2023-09-26 13:20:00','2023-09-29 18:30:00','2023-09-29 21:45:00','2023-10-05 11:00:00','2023-10-08 07:30:00','2023-10-12 16:15:00','2023-11-05 22:00:00','2023-11-10 07:45:00','2023-11-15 13:20:00','2023-11-23 19:30:00','2023-11-25 07:05:00','2023-11-28 09:10:00','2023-12-05 14:55:00','2023-12-10 18:20:00'],
            'Link': ['link1', 'link2', 'link3', 'link4', 'link5', 'link6', 'link7', 'link8','link9','link10', 'link11','link12','link13','link14','link15', 'link16','link17','link18','link19','link20','link21','link22','link23','link24','link25','link26','link27','link28','link29','link30'],
            'Username': ['badwolf', 'taylor','emma', 'lindsaybrookethomas', 'lindsaybrookethomas', 'rory', 'rory', 'emma', 'lindsaybrookethomas','rory', 'lindsaybrookethomas', 'taylor','taylor','rory', 'lindsaybrookethomas','ikeapt','tacobell','ikeapt','ikeapt','ikeapt','tacobell','ikeapt','tacobell','tacobell','disney','disney','disney','microsoft','microsoft','playstation'],
            'Description': ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9', 'text10', 'text11', 'text12', 'text13', 'text14','text15','text16','text17','text18','text19','text20','text21','text22','text23','text24','text25','text26','text27','text28','text29','text30'],
            'Hashtags': ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6','tag7','tag8','tag9', 'tag10','tag11','tag12','tag13','tag14','tag15','tag16','tag17','tag18','tag19','tag20','tag21','tag22','tag23','tag24','tag25','tag26','tag27','tag28','tag29','tag30'],
            'Sound Name': ['sound7', 'sound4','sound4','sound1','sound1','sound2','sound2','sound4','sound1','sound2','sound1','sound3','sound3','sound2','sound1','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music','Promoted Music'],
            'Sound Link': ['www.tiktok.com/music/sound7', 'www.tiktok.com/music/sound4','www.tiktok.com/music/sound4', 'www.tiktok.com/music/sound1','www.tiktok.com/music/sound1', 'www.tiktok.com/music/sound2','www.tiktok.com/music/sound2', 'www.tiktok.com/music/sound4','www.tiktok.com/music/sound1', 'www.tiktok.com/music/sound2','www.tiktok.com/music/sound1','www.tiktok.com/music/sound3','www.tiktok.com/music/sound3','www.tiktok.com/music/sound2','www.tiktok.com/music/sound1','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/ikeapt','www.tiktok.com/music/ikeapt','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/ikeapt','www.tiktok.com/music/tacobell','www.tiktok.com/music/tacobell','www.tiktok.com/music/disney','www.tiktok.com/music/disney','www.tiktok.com/music/disney','www.tiktok.com/music/microsoft','www.tiktok.com/music/microsoft','www.tiktok.com/music/playstation']
        }

        self.sample_hashtag_data = {
            'Hashtag': ['007', '00sbaby', '100k', '100layers', '100million', '100solodateideas', '100years', '101dalmatians', '101daysofgamora', '1080p', '10k', '10millionadoptions', '10monthsold', '10sbabe', '10stephaircareroutine', '10tags5questions', '10thdoctor', '10thdoctoredit', '10thhungergames', '10thingsihataboutyou', '10yearchallenge', '10years', '11andthepondsedit', '11doctorwho', '11monthsold', '11thdoctor', '11thdoctoredit', '11weeksold', '12', '123letsgobitc', '123lgb'],
            'Cluster': ["['007']", "['00sbaby', 'baby']", "['100k', 'daimonia100k', 'isaacs100keditcomp', 'kandi', 'the100', 'zexo100kcomp']", "['100layers', 'the100']", "['100million', 'million', 'the100']", "['100solodateideas', 'cheapdateideas', 'datedayideas', 'falldateideas', 'seasonaldateideas', 'solobookdate', 'uniquedateideas']", "['100years', 'disney100yearsofmagic', 'the100', 'years']", "['101dalmatians']", "['101daysofgamora']", "['1080p', 'pll']", "['10k', 'kandi', 'karish10kcomp', 'ourscardigan10k', 'stel10kcomp']", "['10millionadoptions']", "['10monthsold', '11monthsold', '14monthsold']", "['10sbabe', 'babe']", "['10stephaircareroutine', 'haircare', 'haircareroutine']", "['10tags5questions']", "['10thdoctor', '10thdoctoredit', '10thhungergames', '11thdoctor', '12thdoctor', '9thdoctor', 'doctorwho60thanniversary', 'twelvthdoctor']", "['10thdoctoredit', '10thhungergames', '11thdoctoredit', '12thdoctoredit']", "['10thhungergames', 'effiehungergames', 'hungergamesdeluxe', 'ruehungergames', 'thehungergames']", "['10thingsihataboutyou']", "['10yearchallenge']", "['10years', 'first10years', 'years']", "['11andthepondsedit']", "['11doctorwho', '11thdoctor', 'doctorwho']", "['11monthsold', '11weeksold', '14monthsold']", "['11thdoctor', '11thdoctoredit', '12thdoctor', '9thdoctor', 'august11th', 'doctorwho60thanniversary', 'twelvthdoctor']", "['11thdoctoredit', '12thdoctoredit', 'august11th']", "['11weeksold', '14weeksold', 'sixweeksold']", "['12', '12apostles', '12clara', 'day12', 'district12', 'local12', 'year12']", "['123letsgobitc']", "['123lgb']"],
            'Count':  [2, 98, 52, 7, 21, 35, 22, 2, 3, 30, 59, 1, 15,5, 12, 1, 194, 62, 410, 4, 1, 16, 2, 399, 10, 175, 53, 5, 71, 1, 10]
        }

        self.sample_sound_trends_data = {
            'Sound Name': ['sound7', 'sound4', 'sound3'],
            'Sound Link': ['www.tiktok.com/music/sound7', 'www.tiktok.com/music/sound4', 'www.tiktok.com/music/sound3']
        }

        self.sample_tiktok_trend_data = {
            'Trends': ['text1', 'trend2', 'trend3']
        }

        # Create DataFrames
        self.sample_history = pd.DataFrame(self.sample_history_data)
        self.sample_likes = pd.DataFrame(self.sample_likes_data)
        self.sample_favorites = pd.DataFrame(self.sample_favorites_data)
        self.sample_hashtag = pd.DataFrame(self.sample_hashtag_data)
        self.sample_sound_trends = pd.DataFrame(self.sample_sound_trends_data)
        self.sample_tiktok_trends = pd.DataFrame(self.sample_tiktok_trend_data)

    def test_top_following(self):
        # Call the function with the sample data
        result = crud.top_following(self.sample_history)

        # Check if the result is a DataFrame and has the expected columns
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(all(col in result.columns for col in ['Username', 'Count']))

    def test_top_creator_history(self):
        result = crud.top_creator_history(self.sample_history)

        self.assertIsInstance(result, dict)
        self.assertTrue(len(result['Username']) == 5)
        self.assertTrue(result['Username'][0] == 'rory')
        self.assertTrue(result['Username'][1] == 'badwolf')
        self.assertTrue(result['Username'][2] == 'lindsaybrookethomas')
        self.assertTrue(result['Username'][3] == 'lily')
        self.assertTrue(result['Username'][4] == 'batfamilyprotector')
        self.assertTrue(result['Count'][0] == 5)
        self.assertTrue(result['Count'][1] == 4)
        self.assertTrue(result['Count'][2] == 3)
        self.assertTrue(result['Count'][3] == 2)
        self.assertTrue(result['Count'][4] == 1)

    def test_top_creator_likes(self):
        # Call the function with the sample data
        result = crud.top_creator_likes(self.sample_history, self.sample_likes)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result['Username']) == 5)
        self.assertTrue(result['Username'][0] == 'badwolf')
        self.assertTrue(result['Username'][1] == 'rory')
        self.assertTrue(result['Username'][2] == 'batfamilyprotector')
        self.assertTrue(result['Username'][3] == 'emma')
        self.assertTrue(result['Username'][4] == 'lindsaybrookethomas')
        self.assertTrue(result['Count_y'][0] == 5)
        self.assertTrue(result['Count_y'][1] == 4)
        self.assertTrue(result['Count_y'][2] == 3)
        self.assertTrue(result['Count_y'][3] == 2)
        self.assertTrue(result['Count_y'][4] == 1)
        self.assertTrue(result['Arrow'][0] == 'up')
        self.assertTrue(result['Arrow'][1] == 'down')
        self.assertTrue(result['Arrow'][2] == 'up')
        self.assertTrue(result['Arrow'][3] == 'New Entry')
        self.assertTrue(result['Arrow'][4] == 'down')

    def test_top_creator_favorites(self):
        # Call the function with the sample data
        result = crud.top_creator_favorites(self.sample_likes, self.sample_favorites)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result['Username']) == 5)
        self.assertTrue(result['Username'][0] == 'lindsaybrookethomas')
        self.assertTrue(result['Username'][1] == 'rory')
        self.assertTrue(result['Username'][2] == 'taylor')
        self.assertTrue(result['Username'][3] == 'emma')
        self.assertTrue(result['Username'][4] == 'badwolf')
        self.assertTrue(result['Count_y'][0] == 5)
        self.assertTrue(result['Count_y'][1] == 4)
        self.assertTrue(result['Count_y'][2] == 3)
        self.assertTrue(result['Count_y'][3] == 2)
        self.assertTrue(result['Count_y'][4] == 1)
        self.assertTrue(result['Arrow'][0] == 'up')
        self.assertTrue(result['Arrow'][1] == 'same')
        self.assertTrue(result['Arrow'][2] == 'New Entry')
        self.assertTrue(result['Arrow'][3] == 'same')
        self.assertTrue(result['Arrow'][4] == 'down')

    def test_top_sound_history(self):
        # Call the function with the sample data
        result = crud.top_sound_history(self.sample_history)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result['Sound Name']) == 5)
        self.assertTrue(result['Sound Name'][0] == 'sound1')
        self.assertTrue(result['Sound Name'][1] == 'sound2')
        self.assertTrue(result['Sound Name'][2] == 'sound3')
        self.assertTrue(result['Sound Name'][3] == 'sound4')
        self.assertTrue(result['Sound Name'][4] == 'sound5')
        self.assertTrue(result['Count'][0] == 5)
        self.assertTrue(result['Count'][1] == 4)
        self.assertTrue(result['Count'][2] == 3)
        self.assertTrue(result['Count'][3] == 2)
        self.assertTrue(result['Count'][4] == 1)

    def test_top_sound_likes(self):
        # Call the function with the sample data
        result = crud.top_sound_likes(self.sample_history, self.sample_likes)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result['Sound Name']) == 5)
        self.assertTrue(result['Sound Name'][0] == 'sound2')
        self.assertTrue(result['Sound Name'][1] == 'sound1')
        self.assertTrue(result['Sound Name'][2] == 'sound6')
        self.assertTrue(result['Sound Name'][3] == 'sound4')
        self.assertTrue(result['Sound Name'][4] == 'sound5')
        self.assertTrue(result['Count_y'][0] == 5)
        self.assertTrue(result['Count_y'][1] == 4)
        self.assertTrue(result['Count_y'][2] == 3)
        self.assertTrue(result['Count_y'][3] == 2)
        self.assertTrue(result['Count_y'][4] == 1)
        self.assertTrue(result['Arrow'][0] == 'up')
        self.assertTrue(result['Arrow'][1] == 'down')
        self.assertTrue(result['Arrow'][2] == 'New Entry')
        self.assertTrue(result['Arrow'][3] == 'same')
        self.assertTrue(result['Arrow'][4] == 'same')

    def test_top_sound_favorites(self):
        # Call the function with the sample data
        result = crud.top_sound_favorites(self.sample_likes, self.sample_favorites)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result['Sound Name']) == 5)
        self.assertTrue(result['Sound Name'][0] == 'sound1')
        self.assertTrue(result['Sound Name'][1] == 'sound2')
        self.assertTrue(result['Sound Name'][2] == 'sound4')
        self.assertTrue(result['Sound Name'][3] == 'sound3')
        self.assertTrue(result['Sound Name'][4] == 'sound7')
        self.assertTrue(result['Count_y'][0] == 5)
        self.assertTrue(result['Count_y'][1] == 4)
        self.assertTrue(result['Count_y'][2] == 3)
        self.assertTrue(result['Count_y'][3] == 2)
        self.assertTrue(result['Count_y'][4] == 1)
        self.assertTrue(result['Arrow'][0] == 'up')
        self.assertTrue(result['Arrow'][1] == 'down')
        self.assertTrue(result['Arrow'][2] == 'up')
        self.assertTrue(result['Arrow'][3] == 'New Entry')
        self.assertTrue(result['Arrow'][4] == 'New Entry')
    
    def test_top_hashtag(self):
        # Call the function with the sample data
        result = crud.top_hashtag(self.sample_hashtag, False)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result['Hashtag']) == 5)
        self.assertTrue(result['Hashtag'][0] == '10thhungergames')
        self.assertTrue(result['Hashtag'][1] == '11doctorwho')
        self.assertTrue(result['Hashtag'][2] == '10thdoctor')
        self.assertTrue(result['Hashtag'][3] == '11thdoctor')
        self.assertTrue(result['Hashtag'][4] == '00sbaby')
        self.assertTrue(result['Count'][0] == 410)
        self.assertTrue(result['Count'][1] == 399)
        self.assertTrue(result['Count'][2] == 194)
        self.assertTrue(result['Count'][3] == 175)
        self.assertTrue(result['Count'][4] == 98)

    def test_total_minutes(self):
        # Call the function with the sample data
        result = crud.total_minutes(self.sample_history)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(all(key in result for key in ['Minutes', 'Quote']))

        self.assertTrue(result['Minutes'] == 13460)
        self.assertTrue(result['Quote'] == "Procrastination level: Expert! The real question is, how many times did you think about doing chores?")

    def test_time_of_day(self):
        # Call the function with the sample data
        result = crud.time_of_day(self.sample_history)

        # Check if the result is a dictionary and has the expected keys
        self.assertIsInstance(result, dict)
        self.assertTrue(all(key in result for key in ['Time', 'Quote']))

        self.assertTrue(result['Time'] == '7-8')
        self.assertTrue(result['Quote'] == "Rise and shine! Are you on a mission to out-early-bird the early birds? The worm's not ready, but you're already catching the laughs!")

    def test_top_creator_overall(self):
        result = crud.top_creator_overall(self.sample_history, self.sample_likes, self.sample_favorites)

        self.assertIsInstance(result, dict)
        
        self.assertTrue(result['Username'][0] == 'rory')
        self.assertTrue(result['Photo'][0] == '')
        self.assertTrue(result['Count_History'][0] == 5)
        self.assertTrue(result['Count_Likes'][0] == 4)
        self.assertTrue(result['Count_Favorites'][0] == 4)


    def test_ads(self):
        result = crud.ads(self.sample_history)

        self.assertIsInstance(result, dict)
        self.assertTrue(result['Username'][0] == 'ikeapt')
        self.assertTrue(result['Username'][1] == 'tacobell')
        self.assertTrue(result['Username'][2] == 'disney')
        self.assertTrue(result['Username'][3] == 'microsoft')
        self.assertTrue(result['Username'][4] == 'playstation')
        self.assertTrue(result['Count'][0] == 5)
        self.assertTrue(result['Count'][1] == 4)
        self.assertTrue(result['Count'][2] == 3)
        self.assertTrue(result['Count'][3] == 2)
        self.assertTrue(result['Count'][4] == 1)
        self.assertTrue(result['Percentage'][0] == 50.0)
        
    def test_summary(self):
        result = crud.summary(self.sample_history, self.sample_likes, self.sample_favorites, self.sample_hashtag)
        
        self.assertIsInstance(result, dict)
        self.assertTrue(result['Total Minutes'] == 13460)
        self.assertTrue(result['Top Creators']['Username'][0] == 'rory')
        self.assertTrue(result['Top Creators']['Username'][1] == 'badwolf')
        self.assertTrue(result['Top Creators']['Username'][2] == 'lindsaybrookethomas')
        self.assertTrue(result['Top Creators']['Username'][3] == 'lily')
        self.assertTrue(result['Top Creators']['Username'][4] == 'batfamilyprotector')
        self.assertTrue(result['Top Hashtags']['Hashtag'][0] == '10thhungergames')
        self.assertTrue(result['Top Hashtags']['Hashtag'][1] == '11doctorwho')
        self.assertTrue(result['Top Hashtags']['Hashtag'][2] == '10thdoctor')
        self.assertTrue(result['Top Hashtags']['Hashtag'][3] == '11thdoctor')
        self.assertTrue(result['Top Hashtags']['Hashtag'][4] == '00sbaby')
    
    def test_top_sound(self):
        result = crud.top_sound(self.sample_history)

        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result['Sound Link'][0] == 'www.tiktok.com/music/sound1')
        self.assertTrue(result['Sound Link'][1] == 'www.tiktok.com/music/sound2')
        self.assertTrue(result['Sound Link'][2] == 'www.tiktok.com/music/sound3')
        self.assertTrue(result['Sound Link'][3] == 'www.tiktok.com/music/sound4')
        self.assertTrue(result['Sound Link'][4] == 'www.tiktok.com/music/sound5')
        self.assertTrue(result['Count'][0] == 5)
        self.assertTrue(result['Count'][1] == 4)
        self.assertTrue(result['Count'][2] == 3)
        self.assertTrue(result['Count'][3] == 2)
        self.assertTrue(result['Count'][4] == 1)

    def test_compare_positions(self):
        top_history = crud.top_following(self.sample_history).head(5)
        top_likes = crud.top_following(self.sample_likes).head(5)
        result = crud.compare_positions(top_history, top_likes, 'History', 'Likes', 'Username')

        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result['Username'][0] == 'badwolf')
        self.assertTrue(result['Username'][1] == 'rory')
        self.assertTrue(result['Username'][2] == 'batfamilyprotector')
        self.assertTrue(result['Username'][3] == 'emma')
        self.assertTrue(result['Username'][4] == 'lindsaybrookethomas')
        self.assertTrue(result['Count_x'][0] == 4.0)
        self.assertTrue(result['Count_x'][1] == 5.0)
        self.assertTrue(result['Count_x'][2] == 1.0)
        self.assertTrue(result['Count_x'][4] == 3.0)
        self.assertTrue(result['Position_History'][0] == 2.0)
        self.assertTrue(result['Position_History'][1] == 1.0)
        self.assertTrue(result['Position_History'][2] == 5.0)
        self.assertTrue(result['Position_History'][4] == 3.0)
        self.assertTrue(result['Count_y'][0] == 5)
        self.assertTrue(result['Count_y'][1] == 4)
        self.assertTrue(result['Count_y'][2] == 3)
        self.assertTrue(result['Count_y'][3] == 2)
        self.assertTrue(result['Count_y'][4] == 1)
        self.assertTrue(result['Position_Likes'][0] == 1)
        self.assertTrue(result['Position_Likes'][1] == 2)
        self.assertTrue(result['Position_Likes'][2] == 3)
        self.assertTrue(result['Position_Likes'][3] == 4)
        self.assertTrue(result['Position_Likes'][4] == 5)
        self.assertTrue(result['Change'][0] == 1.0)
        self.assertTrue(result['Change'][1] == -1.0)
        self.assertTrue(result['Change'][2] == 2.0)
        self.assertTrue(result['Change'][4] == -2.0)
        self.assertTrue(result['Arrow'][0] == 'up')
        self.assertTrue(result['Arrow'][1] == 'down')
        self.assertTrue(result['Arrow'][2] == 'up')
        self.assertTrue(result['Arrow'][3] == 'New Entry')
        self.assertTrue(result['Arrow'][4] == 'down')

    def test_top_creators(self):
        top_history = crud.top_following(self.sample_history)
        top_likes = crud.top_following(self.sample_likes)
        top_favorites = crud.top_following(self.sample_favorites)
        result = crud.top_creators(top_history, top_likes, top_favorites).head(5)

        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result['Username'][0] == 'rory')
        self.assertTrue(result['Username'][1] == 'badwolf')
        self.assertTrue(result['Username'][2] == 'lindsaybrookethomas')
        self.assertTrue(result['Username'][3] == 'lily')
        self.assertTrue(result['Username'][4] == 'batfamilyprotector')
        self.assertTrue(result['Count'][0] == 15.0)
        self.assertTrue(result['Count'][1] == 12.0)
        self.assertTrue(result['Count'][2] == 9.0)
        self.assertTrue(result['Count'][3] == 6.0)
        self.assertTrue(result['Count'][4] == 3.0)

    def test_get_tiktok_sound_trends(self):
        result = crud.get_tiktok_sound_trends(self.sample_history, self.sample_sound_trends)

        self.assertIsInstance(result, dict)
        self.assertTrue(result['Trends']['Sound Name'][0] == 'sound7')
        self.assertTrue(result['Trends']['Sound Name'][1] == 'sound4')
        self.assertTrue(result['Trends']['Sound Name'][2] == 'sound3')
        self.assertTrue(result['Trends']['Sound Link'][0] == 'www.tiktok.com/music/sound7')
        self.assertTrue(result['Trends']['Sound Link'][1] == 'www.tiktok.com/music/sound4')
        self.assertTrue(result['Trends']['Sound Link'][2] == 'www.tiktok.com/music/sound3')
        self.assertTrue(result['Trends']['Count'][0] == 0)
        self.assertTrue(result['Trends']['Count'][1] == 2)
        self.assertTrue(result['Trends']['Count'][2] == 3)


    def test_get_tiktok_trends(self):
        result = crud.get_tiktok_trends(self.sample_history, self.sample_tiktok_trends)

        self.assertIsInstance(result, dict)
        self.assertTrue(result['Trends'][0] == 'text1')
        self.assertTrue(result['Trends'][1] == 'trend2')
        self.assertTrue(result['Trends'][2] == 'trend3')
        self.assertTrue(result['Total Trends'] == 3)
        self.assertTrue(result['Seen Trends'] == 1)


    def test_hex_to_rgv(self):
        result = crud.hex_to_rgb('#ffffff')

        self.assertIsInstance(result, tuple)
        self.assertTrue(result[0] == 255)
        self.assertTrue(result[1] == 255)
        self.assertTrue(result[2] == 255)

    def test_rgb_to_hex(self):
        rgb = (255, 255, 255)
        result = crud.rgb_to_hex(rgb)

        self.assertIsInstance(result, str)
        self.assertTrue(result == '#ffffff')

    

if __name__ == '__main__':
    unittest.main()
