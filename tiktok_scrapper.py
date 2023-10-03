# div tiktok-15ip68j-DivDescriptionContentWrapper-StyledDetailContentWrapper eqrezik14
# has tiktok username + description + photo + tags + sound

import requests
from bs4 import BeautifulSoup
import csv

header = ["Date", "Link", "Username", "Description", "Hashtags", "Sound Name", "Sound Link"]

csv_file_path = "favorite_videos.csv"
with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
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
        tiktok_username = tiktok_info.find("span", {"class": "tiktok-1c7urt-SpanUniqueId evv7pft1"}).text
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
        csv_file_path = "tiktok_data.csv"

        # Check if the CSV file exists or not and write the data to it
    
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            if(csv_file.tell() == 0):
                writer.writerow(header)
            writer.writerow(tiktok_data)
            print(f"Data appended to {csv_file_path}")

