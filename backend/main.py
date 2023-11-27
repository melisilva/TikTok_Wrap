import uvicorn
from fastapi import FastAPI
import crud
app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

# scrap photos of stuff
# can see if there's a most watched video and scrap it idk

# top creator history
@app.get("/top-creator-history")
def top_creator_history():
    crud.top_creator_history()
    return {"Hello": "World"}
# top creator likes
# top creator favorites
# top sound history
# top sound likes
# top sound favorites
# top hashtag history
# top hashtag likes
# top hashtag favorites
# total number of minutes
# time of the day most active
# top creator overall + number of videos watched; liked and favorited

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)