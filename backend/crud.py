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


def get_date():
    likes = pd.read_csv('data/likes_full_tiktok_data.csv')
    favorites = pd.read_csv('data/favorite_videos_full_tiktok_data.csv')

    likes = likes.sort_values(by=["Date"])
    favorites = favorites.sort_values(by=["Date"])

    oldest_date_likes = likes['Date'].min()
    oldest_date_favorites = favorites['Date'].min()
    base_date = max(oldest_date_likes, oldest_date_favorites)

    return base_date


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



def top_following(df, name):

    # Assuming 'Username' is the column containing usernames in the history DataFrame
    username_counts = df['Username'].value_counts().reset_index()

    # Rename the columns for clarity
    username_counts.columns = ['Username', 'Count']

    # Sort the DataFrame based on the 'Username' column
    sorted_username_counts = username_counts.sort_values(by='Count', ascending=False)

    # Display the sorted and counted data
    return sorted_username_counts

def top_creator_history():
    history = pd.read_csv('data/unique_video_browsing_history_full_tiktok_data.csv')
    history = history.sort_values(by=["Date"])
    date = get_date()
    history = history[history['Date'] >= date]
    top = top_following(history, "History").head(10)
    top['Photo'] = top['Username'].apply(scrape_tiktok_photo)
    top = top.to_dict()
    return top
