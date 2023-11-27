import pandas as pd
import requests
from bs4 import BeautifulSoup

# Check if this works as global variables

history = pd.read_csv('data/unique_video_browsing_history_full_tiktok_data.csv')
likes = pd.read_csv('data/likes_full_tiktok_data.csv')
favorites = pd.read_csv('data/favorite_videos_full_tiktok_data.csv')
share = pd.read_csv('data/share_history_full_tiktok_data.csv')
# see how to put hashtags here

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

def scrape_tiktok_photo(name):
    link = "https://www.tiktok.com/@" + name
    page = requests.get(link)
    
    soup = BeautifulSoup(page.content, "lxml")
    photo = soup.find("img", {"class":"tiktok-1zpj2q-ImgAvatar e1e9er4e1"})
    if(photo != None):
        photo = photo['src']
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
    top['Photo'] = top['Username'].apply(scrape_tiktok_photo)
    top = top.to_dict()
    return top

def top_creator_likes():
    top_history = top_following(history).head(5)
    top_likes = top_following(likes).head(5)
    top = compare_positions(top_history, top_likes, 'History', 'Likes', 'Username')
    top.drop(['Count_x', 'Position_History', 'Position_Likes', 'Change'], axis=1, inplace=True)

    top['Photo'] = top['Username'].apply(scrape_tiktok_photo)
    top = top.to_dict()
    return top

def top_creator_favorites():
    top_likes = top_following(likes).head(5)
    top_favorites = top_following(favorites).head(5)
    top = compare_positions(top_likes, top_favorites, 'Likes', 'Favorites', 'Username')
    top.drop(['Count_x', 'Position_Likes', 'Position_Favorites', 'Change'], axis=1, inplace=True)

    top['Photo'] = top['Username'].apply(scrape_tiktok_photo)
    top = top.to_dict()
    return top
