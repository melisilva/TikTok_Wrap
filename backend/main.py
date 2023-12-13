import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import crud

import pandas as pd


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

print(base_date)

history = history[history['Date'] >= base_date]
likes = likes[likes['Date'] >= base_date]
favorites = favorites[favorites['Date'] >= base_date]
share = share[share['Date'] >= base_date]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"Hello": "World"}

# can see if there's a most watched video and scrap it idk

# top creator history
@app.get("/top-creator-history")
def top_creator_history():
    return crud.top_creator_history(history)

# top creator likes
@app.get("/top-creator-likes")
def top_creator_likes():
    return crud.top_creator_likes(history, likes)

# top creator favorites
@app.get("/top-creator-favorites")
def top_creator_favorites():
    return crud.top_creator_favorites(likes, favorites)

# top sound history
@app.get("/top-sound-history")
def top_sound_history():
    return crud.top_sound_history(history)

# top sound likes
@app.get("/top-sound-likes")
def top_sound_likes():
    return crud.top_sound_likes(history, likes)

# top sound favorites
@app.get("/top-sound-favorites")
def top_sound_favorites():
    return crud.top_sound_favorites(likes, favorites)

# top hashtag history
@app.get("/top-hashtag")
def top_hashtag_history():
    return crud.top_hashtag(hashtags)

# total number of minutes
@app.get("/total-minutes")
def total_minutes():
    return crud.total_minutes(history)

# time of the day most active
@app.get("/time-of-day")
def time_of_day():
    return crud.time_of_day(history)

# top creator overall + number of videos watched; liked and favorited
@app.get("/top-creator-overall")
def top_creator_overall():
    return crud.top_creator_overall(history, likes, favorites)

# % of ads and who are the creators
@app.get("/ads")
def ads():
    return crud.ads(history)

# summary of the data
@app.get("/summary")
def summary():
    return crud.summary(history, likes, favorites, hashtags)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)