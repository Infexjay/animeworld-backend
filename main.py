from fastapi import FastAPI
from animepahe import get_anime_list
import random

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Anime World API is online"}

@app.get("/random-anime")
def random_anime():
    anime_list = get_anime_list()
    if not anime_list:
        return {"error": "No anime found."}
    return random.choice(anime_list)
