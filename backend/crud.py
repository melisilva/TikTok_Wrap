import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import aiohttp
import asyncio

# Check if this works as global variables

history = pd.read_csv('data/unique_video_browsing_history_full_tiktok_data.csv')
likes = pd.read_csv('data/likes_full_tiktok_data.csv')
favorites = pd.read_csv('data/favorite_videos_full_tiktok_data.csv')
share = pd.read_csv('data/share_history_full_tiktok_data.csv')
hashtags = pd.read_csv('data/clean_hashtags/after_hashtags.csv')

user_photos = pd.read_csv("backend/user_photos.csv")
hashtag_photos = pd.read_csv("backend/hashtag_photos.csv")
sound_photos = pd.read_csv("backend/sound_photos.csv")


history = history.sort_values(by=["Date"])
likes = likes.sort_values(by=["Date"])
favorites = favorites.sort_values(by=["Date"])
share = share.sort_values(by=["Date"])

oldest_date_likes = likes['Date'].min()
oldest_date_favorites = favorites['Date'].min()
base_date = max(oldest_date_likes, oldest_date_favorites)

print(base_date)

history = history[history['Date'] >= base_date]
likes = likes[likes['Date'] >= base_date]
favorites = favorites[favorites['Date'] >= base_date]
share = share[share['Date'] >= base_date]

async def scrape_tiktok_photo_user(link, session):
    async with session.get(link) as response:
        content = await response.text()

        soup = BeautifulSoup(content, "lxml")        
        photo = soup.find("img", {"class":"tiktok-1zpj2q-ImgAvatar e1e9er4e1"})
        if(photo != None):
            photo = photo['src']
        else:
            photo = ""
        return photo

async def scrape_tiktok_photo_hashtag(link, session):
    async with session.get(link) as response:
        content = await response.text()

        soup = BeautifulSoup(content, "lxml")        
        div = soup.find("div", {"class":"tiktok-fcfffm-DivShareInfo ekmpd5l2"})
        photo = div.find("img", {"class":"tiktok-1zpj2q-ImgAvatar e1e9er4e1"})
        if(photo != None):
            photo = photo['src']
        else:
            photo = ""
        return photo

async def scrape_tiktok_sound_photo(link,session):
    link = "https://" + link
    async with session.get(link) as response:
        content = await response.text()
    
        soup = BeautifulSoup(content, "lxml")
        photo = soup.find("div", {"class":"tiktok-uur1tb-DivMusicCardContainer ervjp3i1"})
        if(photo != None):
            photo = photo['style'].split('background-image:url')[1].split('(')[1].split(')')[0]
        else:
            photo = ""
        return photo


async def fetch_photos(link, creators, indicator):
    async with aiohttp.ClientSession() as session:
        if indicator == 'Username':
            tasks = [scrape_tiktok_photo_user(link + creator, session) for creator in creators]
        else:
            tasks = [scrape_tiktok_photo_hashtag(link + creator, session) for creator in creators]
        return await asyncio.gather(*tasks)

async def fetch_photos_sounds(sounds):
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_tiktok_sound_photo(sound, session) for sound in sounds]
        return await asyncio.gather(*tasks)

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

    # check if the sound link equal to "www.tiktok.com/" exists and drop it
    df_copy.drop(df_copy.loc[df_copy['Sound Link'] == "www.tiktok.com/"].index, inplace=True)

    sound_counts = df_copy['Sound Link'].value_counts().reset_index()

    # Rename the columns for clarity
    sound_counts.columns = ['Sound Link', 'Count']

    # Sort the DataFrame based on the 'Count' column
    sorted_sound_counts = sound_counts.sort_values(by='Count', ascending=False)

    # Display the sorted and counted data
    return sorted_sound_counts

def top_hashtag(need_photo = True):
    # Sort the DataFrame based on the 'Count' column
    sorted_hashtag_counts = hashtags.sort_values(by='Count', ascending=False)

    top = sorted_hashtag_counts.head(5).reset_index()

    """
    if(need_photo):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            top['Photo'] = loop.run_until_complete(fetch_photos("https://www.tiktok.com/tag/", top['Hashtag'], 'Hashtag'))
        finally:
            loop.close()
    """

    photos = []
    for i in range(len(top)):
        hashtag = top['Hashtag'][i]
        photo = hashtag_photos[hashtag_photos['Hashtag'] == hashtag]['Photo'].item()
        photos.append(photo)

    top['Photo'] = photos

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

    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        top['Photo'] = loop.run_until_complete(fetch_photos("https://www.tiktok.com/@", top['Username'], 'Username'))
    finally:
        loop.close()
    """

    photos = []

    for i in range(len(top)):
        username = top['Username'][i]
        photo = user_photos[user_photos['Username'] == username]['Photo'].item()
        photos.append(photo)

    top['Photo'] = photos

    top = top.to_dict()
    return top

def top_creator_likes():
    top_history = top_following(history).head(5)
    top_likes = top_following(likes).head(5)
    top = compare_positions(top_history, top_likes, 'History', 'Likes', 'Username')
    top.drop(['Count_x', 'Position_History', 'Position_Likes', 'Change'], axis=1, inplace=True)

    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        top['Photo'] = loop.run_until_complete(fetch_photos("https://www.tiktok.com/@", top['Username'], 'Username'))
    finally:
        loop.close()
    """

    photos = []
    for i in range(len(top)):
        username = top['Username'][i]
        photo = user_photos[user_photos['Username'] == username]['Photo'].item()
        photos.append(photo)

    top['Photo'] = photos

    top = top.to_dict()
    return top

def top_creator_favorites():
    top_likes = top_following(likes).head(5)
    top_favorites = top_following(favorites).head(5)
    top = compare_positions(top_likes, top_favorites, 'Likes', 'Favorites', 'Username')
    top.drop(['Count_x', 'Position_Likes', 'Position_Favorites', 'Change'], axis=1, inplace=True)

    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        top['Photo'] = loop.run_until_complete(fetch_photos("https://www.tiktok.com/@", top['Username'], 'Username'))
    finally:
        loop.close()
    """

    photos = []
    for i in range(len(top)):
        username = top['Username'][i]
        photo = user_photos[user_photos['Username'] == username]['Photo'].item()
        photos.append(photo)

    top['Photo'] = photos

    top = top.to_dict()
    return top

def top_sound_history():
    top = top_sound(history).head(5)

    sound_names = []
    for i in top['Sound Link']:
        sound_name = history.loc[history['Sound Link'] == i, 'Sound Name'].head(1).item()
        sound_names.append(sound_name)

    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        top['Photo'] = loop.run_until_complete(fetch_photos_sounds(top['Sound Link']))
    finally:
        loop.close()
    """

    photos = []
    for i in range(len(top)):
        sound_link = top['Sound Link'][i]
        photo = sound_photos[sound_photos['Sound Link'] == sound_link]['Photo'].item()
        photos.append(photo)

    top['Photo'] = photos

    top['Sound Name'] = sound_names
    top.drop(['Sound Link'], axis=1, inplace=True)
    top = top.to_dict()
    return top

def top_sound_likes():
    top_history = top_sound(history).head(5)
    top_likes = top_sound(likes).head(5)
    top = compare_positions(top_history, top_likes, 'History', 'Likes', 'Sound Link')
    top.drop(['Count_x', 'Position_History', 'Position_Likes', 'Change'], axis=1, inplace=True)

    sound_names = []
    for i in top['Sound Link']:
        sound_name = history.loc[history['Sound Link'] == i, 'Sound Name'].head(1).item()
        sound_names.append(sound_name)

    top['Sound Name'] = sound_names

    photos = []
    for i in range(len(top)):
        sound_link = top['Sound Link'][i]
        photo = sound_photos[sound_photos['Sound Link'] == sound_link]['Photo'].item()
        photos.append(photo)

    top['Photo'] = photos

    top.drop(['Sound Link'], axis=1, inplace=True)
    top = top.to_dict()
    return top

def top_sound_favorites():
    top_likes = top_sound(likes).head(5)
    top_favorites = top_sound(favorites).head(5)
    top = compare_positions(top_likes, top_favorites, 'Likes', 'Favorites', 'Sound Link')
    top.drop(['Count_x', 'Position_Likes', 'Position_Favorites', 'Change'], axis=1, inplace=True)

    sound_names = []
    for i in top['Sound Link']:
        sound_name = history.loc[history['Sound Link'] == i, 'Sound Name'].head(1).item()
        sound_names.append(sound_name)

    top['Sound Name'] = sound_names

    photos = []
    for i in range(len(top)):
        sound_link = top['Sound Link'][i]
        photo = sound_photos[sound_photos['Sound Link'] == sound_link]['Photo'].item()
        photos.append(photo)

    top['Photo'] = photos

    top.drop(['Sound Link'], axis=1, inplace=True)
    top = top.to_dict()
    return top

def total_minutes():
    # Convert date strings to datetime objects
    dates = [datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S") for date_str in history['Date']]

    # Calculate time differences between consecutive dates
    time_diff = [dates[i + 1] - dates[i] for i in range(len(dates) - 1)]

    # Sum up the total time difference in minutes
    total_minutes = round(sum(td.total_seconds() / 60 for td in time_diff))

    quote = ""

    if total_minutes < 2400:
        quote = "Either you're new here or you have some serious time management skills!"
    elif 2400 <= total_minutes < 4200:
        quote = "Not bad, not bad at all! That's enough time to become a TikTok philosopher. What's your favorite deep thought from the FYP?"
    elif 4200 <= total_minutes < 7200:
        quote = "Give it up for the dedicated souls! You're not just watching, you're earning a virtual Ph.D. in TikTokology!"
    elif 7200 <= total_minutes < 18000:
        quote = "Procrastination level: Expert! The real question is, how many times did you think about doing chores?"
    elif 18000 <= total_minutes < 30000:
        quote = "Hold onto your time machines! That's enough time to create your own TikTok time capsule!"
    elif 30000 <= total_minutes:
        quote = "And the award for TikTok Marathoner goes to... you! Is there a gold medal for endless scrolling?"

    result = {'Minutes': total_minutes, 'Quote': quote}

    #calculate total of minutes
    return result

def time_of_day():
    ## Convert the 'Date' column to a datetime object
    history['Date'] = pd.to_datetime(history['Date'])

    ## Extract the hour information
    history['Hour'] = history['Date'].dt.hour

    ## Count the occurences of each hour
    hourly_counts = history['Hour'].value_counts().reset_index()

    hourly_counts.columns = ['Hour', 'Count']

    sorted_hourly_counts = hourly_counts.sort_values(by='Count', ascending=False)

    initial_time = sorted_hourly_counts.head(1)['Hour'][0].item()
    time = str(initial_time) + '-' + str(initial_time + 1)
    quote = ""
    if(initial_time >= 5 and initial_time < 8):
        quote = "Rise and shine! Are you on a mission to out-early-bird the early birds? The worm's not ready, but you're already catching the laughs!"
    elif(initial_time >= 0 and initial_time < 5):
        quote = "Burning the midnight oil, or just scrolling through TikTok? Your late-night dedication is unmatched. The real question is, do you dream in TikToks?"
    elif 8 <= initial_time < 12:
        quote = "Good morning to the late risers! You're fashionably late to the TikTok party, but the entertainment is just getting started. Grab your coffee and join the fun!"
    elif(initial_time >= 12 and initial_time < 14):
        quote = "Taking a break or breaking the internet? Your lunchtime dedication to TikTok is commendable. Your boss might be wondering why you're laughing so much during Zoom calls!"
    elif(initial_time >= 14 and initial_time < 16):
        quote = "The early afternoon crew! Dodging responsibilities and diving into TikTok. Who needs productivity when you've got endless content to enjoy?"
    elif 16 <= initial_time < 20:
        quote = "Evening delight! Spending time on TikTok between 4 to 8 PM means you've turned your evenings into a delightful TikTok escape. The sun may be setting, but your laughs are just beginning!"
    elif(initial_time >= 20 and initial_time <= 23):
        quote = "Prime time for prime content! You've chosen the perfect window to unwind with TikTok. Dinner can wait; the real feast is on your For You Page!"

    # Display the sorted and counted data
    result = {'Time': time, 'Quote': quote}
    return result

def top_creators(top_history, top_likes, top_favorites):
    ratio_likes = top_history['Count'] / top_likes['Count']
    ratio_favorites = top_history['Count'] / top_favorites['Count']

    top = top_history.copy()
    top['Count'] = top_history['Count'] + (top_likes['Count'] * ratio_likes) + (top_favorites['Count'] * ratio_favorites)

    top = top.sort_values(by='Count', ascending=False)

    return top

def top_creator_overall():
    top_history = top_following(history)
    top_likes = top_following(likes)
    top_favorites = top_following(favorites)

    top = top_creators(top_history, top_likes, top_favorites).head(1)


    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        top['Photo'] = loop.run_until_complete(fetch_photos("https://www.tiktok.com/@", top['Username'], 'Username'))
    finally:
        loop.close()
    
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

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        top['Photo'] = loop.run_until_complete(fetch_photos("https://www.tiktok.com/@", top['Username'], 'Username'))
    finally:
        loop.close()
        
    top['Percentage'] = len(ads) / len(history) * 100
    top = top.to_dict()

    return top

def summary():
    #top creators
    top_history = top_following(history)
    top_likes = top_following(likes)
    top_favorites = top_following(favorites)

    creators = top_creators(top_history, top_likes, top_favorites).head(5)

    #total minutes
    minutes = total_minutes()['Minutes']

    #top hashtags
    hashtags = top_hashtag(False)

    #user photo
    personal = pd.read_csv("data/personal.csv")
    photo = personal['Photo'].item()
    username = personal['Username'].item()

    summary = {'Top Creators': creators.to_dict(), 'Total Minutes': minutes, 'Top Hashtags': hashtags, "Photo": photo, "Username": username}
    return summary