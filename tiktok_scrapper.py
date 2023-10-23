# div tiktok-15ip68j-DivDescriptionContentWrapper-StyledDetailContentWrapper eqrezik14
# has tiktok username + description + photo + tags + sound

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os

header = ["Date", "Link", "Username", "Description", "Hashtags", "Sound Name", "Sound Link"]

def get_tiktok_video_info(input_file_path, output_file_path):
    table = pd.read_csv(input_file_path)
    row = 0
    
    if os.path.exists(output_file_path):
        # check what's the last line
        df = pd.read_csv(output_file_path)
        last_line = df.tail(1)
    
        # find the row in the input_file_path
        matching_rows = table.loc[table['Link'] == last_line['Link'].values[0]]
        matching_rows = matching_rows.loc[matching_rows['Date'] == last_line['Date'].values[0]]
        row = matching_rows.index.values[0] + 1
    
    sliced_table = table.iloc[row:,:]
    
    for index, row in sliced_table.iterrows():
        date = row['Date']
        link = row['Link']
        page = requests.get(link)
    
        soup = BeautifulSoup(page.content, "lxml")
        error_info = soup.find("div", {"class":"tiktok-u2vwc1-DivErrorWrapper elnrzms1"})
        if(error_info != None):
            print("Error: Video not found")
            continue
        tiktok_info = soup.find("div", {"class":"tiktok-15ip68j-DivDescriptionContentWrapper-StyledDetailContentWrapper eqrezik14"})
        # print(tiktok_info)
        if tiktok_info == None:
            continue
        tiktok_username = tiktok_info.find("span", {"class": "tiktok-1c7urt-SpanUniqueId evv7pft1"})
        if(tiktok_username != None):
            tiktok_username = tiktok_username.text
        else:
            continue
        tiktok_description = tiktok_info.find("span", {"class":"tiktok-j2a19r-SpanText efbd9f0"})
        if(tiktok_description != None):
            tiktok_description = tiktok_description.text
        else:
            tiktok_description = ""
    
    
        hashtag_links = tiktok_info.find_all('a', href=True)
    
        hashtags = [link.text.strip() for link in hashtag_links if link.text.strip().startswith('#')]
        print(hashtags)
    
        sound_name = tiktok_info.find("h4")
        if(sound_name != None):
            sound_name = sound_name.text
            sound_link = "www.tiktok.com"+tiktok_info.find("h4").find("a")['href']
        else:
            sound_name = ""
            sound_link = ""
        
    
        tiktok_data = [date, link, tiktok_username, tiktok_description, ', '.join(hashtags), sound_name, sound_link]
        
        if input_file_path == "data/share_history.csv":
            header.append("SharedContent")
            header.append("Method")
            shared_content = row['SharedContent']
            method = row['Method']
            tiktok_data.append(shared_content)
            tiktok_data.append(method)

    
        # Check if the CSV file exists or not and write the data to it
    
        with open(output_file_path, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            if(csv_file.tell() == 0):
                writer.writerow(header)
            writer.writerow(tiktok_data)
            print(f"Data appended to {output_file_path}")

# share_history have more information than the other videos so the header is different (see if conditions in line 63 and 68)
get_tiktok_video_info("data/favorite_videos.csv", "data/favorite_videos_full_tiktok_data.csv")
get_tiktok_video_info("data/likes.csv","data/likes_full_tiktok_data.csv") 
get_tiktok_video_info("data/share_history.csv", "data/share_history_full_tiktok_data.csv") 
get_tiktok_video_info("data/video_browsing_history.csv", "data/video_browsing_history_full_tiktok_data.csv") 


