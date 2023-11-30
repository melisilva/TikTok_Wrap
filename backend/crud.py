import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Check if this works as global variables

history = pd.read_csv('data/unique_video_browsing_history_full_tiktok_data.csv')
likes = pd.read_csv('data/likes_full_tiktok_data.csv')
favorites = pd.read_csv('data/favorite_videos_full_tiktok_data.csv')
share = pd.read_csv('data/share_history_full_tiktok_data.csv')
hashtags = pd.read_csv('data/clean_hashtags/after_hashtags.csv')

history = history.sort_values(by=["Date"])
likes = likes.sort_values(by=["Date"])
favorites = favorites.sort_values(by=["Date"])
share = share.sort_values(by=["Date"])

oldest_date_likes = likes['Date'].min()
oldest_date_favorites = favorites['Date'].min()
base_date = max(oldest_date_likes, oldest_date_favorites)

history = history[history['Date'] >= base_date]
likes = likes[likes['Date'] >= base_date]
favorites = favorites[favorites['Date'] >= base_date]
share = share[share['Date'] >= base_date]

def scrape_tiktok_photo(link):
    page = requests.get(link)
    
    soup = BeautifulSoup(page.content, "lxml")
    photo = soup.find("img", {"class":"tiktok-1zpj2q-ImgAvatar e1e9er4e1"})
    if(photo != None):
        photo = photo['src']
    else:
        photo = ""
    return photo

def scrape_tiktok_hashtag_photo(link):
    page = requests.get(link)
    
    soup = BeautifulSoup(page.content, "lxml")
    div = soup.find("div", {"class":"tiktok-fcfffm-DivShareInfo ekmpd5l2"})
    photo = div.find("img", {"class":"tiktok-1zpj2q-ImgAvatar e1e9er4e1"})
    if(photo != None):
        photo = photo['src']
    else:
        photo = ""
    return photo

def scrape_tiktok_sound_photo(link):
    link = "https://" + link
    page = requests.get(link)
    
    soup = BeautifulSoup(page.content, "lxml")
    photo = soup.find("div", {"class":"tiktok-uur1tb-DivMusicCardContainer ervjp3i1"})
    if(photo != None):
        photo = photo['style'].split('background-image:url')[1].split('(')[1].split(')')[0]
    else:
        photo = ""
    return photo

def top_following(df):
    # Assuming 'Username' is the column containing usernames in the history DataFrame
    username_counts = df['Username'].value_counts().reset_index()

    # Rename the columns for clarity
    username_counts.columns = ['Username', 'Count']

    # Sort the DataFrame based on the 'Username' column
    sorted_username_counts = username_counts.sort_values(by='Count', ascending=False)

    # Display the sorted and counted data
    return sorted_username_counts

def top_sound(df):
    df_copy = df.copy()

    # Drop every row where the 'Sound Name' contains "Promoted Music"
    df_copy = df_copy[~df_copy['Sound Name'].str.contains("Promoted Music")]

    sound_counts = df_copy['Sound Link'].value_counts().reset_index()

    # Rename the columns for clarity
    sound_counts.columns = ['Sound Link', 'Count']

    # Sort the DataFrame based on the 'Count' column
    sorted_sound_counts = sound_counts.sort_values(by='Count', ascending=False)

    # Display the sorted and counted data
    return sorted_sound_counts

def top_hashtag():
    # Sort the DataFrame based on the 'Count' column
    sorted_hashtag_counts = hashtags.sort_values(by='Count', ascending=False)

    top = sorted_hashtag_counts.head(5).reset_index()

    top['Photo'] = ("https://www.tiktok.com/tag/" + top['Hashtag']).apply(scrape_tiktok_hashtag_photo)
    top.drop(['index', 'Cluster'], axis=1, inplace=True)

    # Display the sorted and counted data
    return top.to_dict()

# Function to compare the position change between two DataFrames
def compare_positions(df1, df2, name1, name2, element_name):
    df1['Position_' + name1] = df1.index + 1 
    df2['Position_' + name2] = df2.index + 1

    merged_df = pd.merge(df1, df2, on=element_name, how='right')

    # Calculate the change in positions
    merged_df['Change'] = merged_df['Position_' + name1] - merged_df['Position_' + name2]
    merged_df['Arrow'] = merged_df['Change'].apply(lambda x: 'up' if x > 0 else ('down' if x < 0 else ('same' if x == 0 else 'New Entry')))

    return merged_df

def top_creator_history(): # taking a lil bit
    top = top_following(history).head(5)

    top['Photo'] = ("https://www.tiktok.com/@" + top['Username']).apply(scrape_tiktok_photo)
    top = top.to_dict()
    return top

def top_creator_likes():
    top_history = top_following(history).head(5)
    top_likes = top_following(likes).head(5)
    top = compare_positions(top_history, top_likes, 'History', 'Likes', 'Username')
    top.drop(['Count_x', 'Position_History', 'Position_Likes', 'Change'], axis=1, inplace=True)

    top['Photo'] = ("https://www.tiktok.com/@" + top['Username']).apply(scrape_tiktok_photo)
    top = top.to_dict()
    return top

def top_creator_favorites():
    top_likes = top_following(likes).head(5)
    top_favorites = top_following(favorites).head(5)
    top = compare_positions(top_likes, top_favorites, 'Likes', 'Favorites', 'Username')
    top.drop(['Count_x', 'Position_Likes', 'Position_Favorites', 'Change'], axis=1, inplace=True)

    top['Photo'] = ("https://www.tiktok.com/@" + top['Username']).apply(scrape_tiktok_photo)
    top = top.to_dict()
    return top

def top_sound_history():
    top = top_sound(history).head(5)

    sound_names = []
    for i in top['Sound Link']:
        sound_name = history.loc[history['Sound Link'] == i, 'Sound Name'].head(1).item()
        sound_names.append(sound_name)


    top['Photo'] = top['Sound Link'].apply(scrape_tiktok_sound_photo)
    top['Sound Name'] = sound_names
    top.drop(['Sound Link'], axis=1, inplace=True)
    top = top.to_dict()
    return top

def top_sound_likes():
    top_history = top_sound(history).head(5)
    top_likes = top_sound(likes).head(5)
    top = compare_positions(top_history, top_likes, 'History', 'Likes', 'Sound Name')
    top.drop(['Count_x', 'Position_History', 'Position_Likes', 'Change'], axis=1, inplace=True)

    sound_names = []
    for i in top['Sound Link']:
        sound_name = history.loc[history['Sound Link'] == i, 'Sound Name'].head(1).item()
        sound_names.append(sound_name)


    top['Photo'] = top['Sound Link'].apply(scrape_tiktok_sound_photo)
    top['Sound Name'] = sound_names
    top.drop(['Sound Link'], axis=1, inplace=True)
    top = top.to_dict()
    return top

def top_sound_favorites():
    top_likes = top_sound(likes).head(5)
    top_favorites = top_sound(favorites).head(5)
    top = compare_positions(top_likes, top_favorites, 'Likes', 'Favorites', 'Sound Name')
    top.drop(['Count_x', 'Position_Likes', 'Position_Favorites', 'Change'], axis=1, inplace=True)

    sound_names = []
    for i in top['Sound Link']:
        sound_name = history.loc[history['Sound Link'] == i, 'Sound Name'].head(1).item()
        sound_names.append(sound_name)


    top['Photo'] = top['Sound Link'].apply(scrape_tiktok_sound_photo)
    top['Sound Name'] = sound_names
    top.drop(['Sound Link'], axis=1, inplace=True)
    top = top.to_dict()
    return top

def total_minutes():
    # Convert date strings to datetime objects
    dates = [datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S") for date_str in history['Date']]

    # Calculate time differences between consecutive dates
    time_diff = [dates[i + 1] - dates[i] for i in range(len(dates) - 1)]

    # Sum up the total time difference in minutes
    total_minutes = sum(td.total_seconds() / 60 for td in time_diff)

    #calculate total of minutes
    return round(total_minutes)

def time_of_day():
    ## Convert the 'Date' column to a datetime object
    history['Date'] = pd.to_datetime(history['Date'])

    ## Extract the hour information
    history['Hour'] = history['Date'].dt.hour

    ## Count the occurences of each hour
    hourly_counts = history['Hour'].value_counts().reset_index()

    hourly_counts.columns = ['Hour', 'Count']

    sorted_hourly_counts = hourly_counts.sort_values(by='Count', ascending=False)

    # Display the sorted and counted data
    return sorted_hourly_counts.head(1)['Hour'][0].item()

def top_creator_overall():
    top_history = top_following(history)
    top_likes = top_following(likes)
    top_favorites = top_following(favorites)

    ratio_likes = top_history['Count'] / top_likes['Count']
    ratio_favorites = top_history['Count'] / top_favorites['Count']

    top = top_history.copy()
    top['Count'] = top_history['Count'] + (top_likes['Count'] * ratio_likes) + (top_favorites['Count'] * ratio_favorites)

    top = top.sort_values(by='Count', ascending=False).head(1)


    top['Photo'] = scrape_tiktok_photo("https://www.tiktok.com/@" + top['Username'].item())
    top['Count_History'] = top_history[top_history['Username'] == top['Username'].item()]['Count'].item()

    if(top['Username'].item() in top_likes['Username'].values):
        top['Count_Likes'] = top_likes[top_likes['Username'] == top['Username'].item()]['Count'].item()
    
    if(top['Username'].item() in top_favorites['Username'].values):
        top['Count_Favorites'] = top_favorites[top_favorites['Username'] == top['Username'].item()]['Count'].item()
    top.drop(['Count'], axis=1, inplace=True)
    top = top.to_dict()
    return top

def ads():
    ads = history[history['Sound Name'] == 'Promoted Music']

    ads_counts = ads['Sound Link'].value_counts().reset_index()

    ads_counts.columns = ['Sound Link', 'Count']

    # Sort the DataFrame based on the 'Count' column
    sorted_ads_counts = ads_counts.sort_values(by='Count', ascending=False)

    top = sorted_ads_counts.head(5)

    creators = []
    for i in top['Sound Link']:
        creator = ads.loc[history['Sound Link'] == i, 'Username'].head(1).item()
        creators.append(creator)

    top['Username'] = creators
    top['Photo'] = ("https://www.tiktok.com/@" + top['Username']).apply(scrape_tiktok_photo)
    
    top['Percentage'] = len(ads) / len(history) * 100
    top = top.to_dict()

    return top