import json

with open('user_data.json', 'r', encoding = 'utf-8') as file:
    data = file.read()
    json_data = json.loads(data)

# Extract the "Favorite Effects" column
# I don't have this
# favorite_effects = json_data["Activity"]["Favorite Effects"]["FavoriteEffectsList"]

# Extract the "Favorite Hashtags" column
# I don't have this
# favorite_hashtags = json_data["Activity"]["Favorite Hashtags"]["FavoriteHashtagList"]

# Extract the "Favorite Sounds" column
# I don't have this
# favorite_sounds = json_data["Activity"]["Favorite Sounds"]["FavoriteSoundList"]

# Extract the "Favorite Videos" column
favorite_videos = json_data["Activity"]["Favorite Videos"]["FavoriteVideoList"]

filename = "data/favorite_videos.csv"
f = open(filename, "w")
f.write("Date,Link\n")
for video in favorite_videos:
    date = video["Date"]
    link = video["Link"]

    f.write(date + "," + link + "\n")

f.close()

"""
# Extract Followers List
followers_list = json_data["Activity"]["Follower List"]["FansList"]

# Extract Following list
following_list = json_data["Activity"]["Following List"]["Following"]

# Extract Hashtags used list
hashtag_list = json_data["Activity"]["Hashtag"]["HashtagList"]

# Extract Likes list
likes_list = json_data["Activity"]["Like List"]["ItemFavoriteList"]

# Extract Search List
search_list = json_data["Activity"]["Search History"]["SearchList"]

# Extract Login History List
login_history_list = json_data["Activity"]["Login History"]["LoginHistoryList"]

# Extract Share History List
share_history_list = json_data["Activity"]["Share History"]["ShareHistoryList"]

# Extract Video Browsing History List
video_browsing_history_list = json_data["Video Browsing History"]["VideoList"]

# Extract Video Upload History List
video_upload_history_list = json_data["Video"]["Videos"]["VideoList"]

# Extract Comments List
comments_list = json_data["Comment"]["Comments"]["CommentsList"]

# Extract Ad Interests List
ad_interests_list = json_data["Ads and data"]["Ad Interests"]["AdInterestCategories"]
"""