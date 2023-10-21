import json

with open('data/user_data.json', 'r', encoding = 'utf-8') as file:
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


# Extract Followers List
followers_list = json_data["Activity"]["Follower List"]["FansList"]

filename = "data/followers.csv"
f = open(filename, "w")
f.write("Date,UserName\n")
for follower in followers_list:
    date = follower["Date"]
    username = follower["UserName"]

    f.write(date + "," + username + "\n")

f.close()

# Extract Following list
following_list = json_data["Activity"]["Following List"]["Following"]

filename = "data/following.csv"
f = open(filename, "w")
f.write("Date,UserName\n")
for follower in followers_list:
    date = follower["Date"]
    username = follower["UserName"]

    f.write(date + "," + username + "\n")

f.close()

# Extract Likes list
likes_list = json_data["Activity"]["Like List"]["ItemFavoriteList"]

# Put through the same scrapper as the favorite videos
filename = "data/likes.csv"
f = open(filename, "w")
f.write("Date,Link\n")
for like in likes_list:
    date = like["Date"]
    link = like["Link"]

    f.write(date + "," + link + "\n")

f.close()

# Extract Hashtags used list
hashtag_list = json_data["Activity"]["Hashtag"]["HashtagList"]

# Don't really know what we can/should scrape from this or we just don't?
filename = "data/hashtags.csv"
f = open(filename, "w")
f.write("HashtagName,HashtagLink\n")
for hashtag in hashtag_list:
    hashtag_name = hashtag["HashtagName"]
    hashtag_link = hashtag["HashtagLink"]

    f.write(hashtag_name + "," + hashtag_link + "\n")

f.close()

# Extract Login History List
login_history_list = json_data["Activity"]["Login History"]["LoginHistoryList"]

filename = "data/login_history.csv"
f = open(filename, "w")
f.write("Date,IP,DeviceModel,DeviceSystem,NetworkType,Carrier\n")
for login in login_history_list:
    date = login["Date"]
    ip = login["IP"]
    device_model = login["DeviceModel"]
    device_system = login["DeviceSystem"]
    network_type = login["NetworkType"]
    carrier = login["Carrier"]

    f.write(date + "," + ip + "," + device_model + "," + device_system + "," + network_type + "," + carrier + "\n")

f.close()


# Extract Search List
search_list = json_data["Activity"]["Search History"]["SearchList"]

# Don't really know what we can/should scrape from this or we just don't?
filename = "data/search_history.csv"
f = open(filename, "w")
f.write("Date,SearchTerm\n")
for search in search_list:
    date = search["Date"]
    search_term = search["SearchTerm"]

    f.write(date + "," + search_term + "\n")

f.close()

# Extract Share History List
share_history_list = json_data["Activity"]["Share History"]["ShareHistoryList"]

# We can scrape stuff from the link but we might not be that worth it?
filename = "data/share_history.csv"
f = open(filename, "w")
f.write("Date,SharedContent,Link,Method\n")
for share in share_history_list:
    date = share["Date"]
    shared_content = share["SharedContent"]
    link = share["Link"]
    method = share["Method"]

    f.write(date + "," + shared_content + "," + link + "," + method + "\n")

f.close()

# Extract Video Browsing History List
video_browsing_history_list = json_data["Activity"]["Video Browsing History"]["VideoList"]

filename = "data/video_browsing_history.csv"
f = open(filename, "w")
f.write("Date,Link\n")
for video in video_browsing_history_list:
    date = video["Date"]
    link = video["Link"]

    f.write(date + "," + link + "\n")

f.close()

# Extract Video Upload History List
video_upload_history_list = json_data["Video"]["Videos"]["VideoList"]

filename = "data/video_upload_history.csv"
f = open(filename, "w")
f.write("Date,Link,Likes\n")
for video in video_upload_history_list:
    date = video["Date"]
    link = video["Link"]
    likes = video["Likes"]

    f.write(date + "," + link + "," + likes + "\n")

f.close()

# Extract Comments List
comments_list = json_data["Comment"]["Comments"]["CommentsList"]

filename = "data/comments.csv"
f = open(filename, "w",encoding="utf-8")
f.write("Date,Comment\n")
for comment in comments_list:
    date = comment["Date"]
    comment = comment["Comment"]

    f.write(date + "," + comment + "\n")

f.close()

# Extract Ad Interests List
ad_interests_list = json_data["Ads and data"]["Ad Interests"]["AdInterestCategories"] # this is just strings

filename = "data/ad_interests.csv"
f = open(filename, "w")
f.write("AdInterestCategories\n")
f.write(ad_interests_list + "\n")

f.close()
