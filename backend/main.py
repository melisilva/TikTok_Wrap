import uvicorn
from fastapi import FastAPI
import crud
app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

# can see if there's a most watched video and scrap it idk

# top creator history
@app.get("/top-creator-history")
def top_creator_history():
    return crud.top_creator_history()

# top creator likes
@app.get("/top-creator-likes")
def top_creator_likes():
    return crud.top_creator_likes()

# top creator favorites
@app.get("/top-creator-favorites")
def top_creator_favorites():
    return crud.top_creator_favorites()

# top sound history
@app.get("/top-sound-history")
def top_sound_history():
    return crud.top_sound_history()

# top sound likes
@app.get("/top-sound-likes")
def top_sound_likes():
    return crud.top_sound_likes()

# top sound favorites
@app.get("/top-sound-favorites")
def top_sound_favorites():
    return crud.top_sound_favorites()

# top hashtag history
@app.get("/top-hashtag")
def top_hashtag_history():
    return crud.top_hashtag()

# total number of minutes
# time of the day most active
# top creator overall + number of videos watched; liked and favorited

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)