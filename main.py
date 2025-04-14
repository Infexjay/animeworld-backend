from fastapi import FastAPI
import requests
import random

app = FastAPI()

BASE_URL = "https://api.consumet.org/anime/gogoanime"

@app.get("/")
def root():
    return {"message": "Anime World API is up and powered by Consumet"}

@app.get("/random-anime")
def get_random_anime():
    query = random.choice(["naruto", "one piece", "bleach", "attack on titan", "demon slayer", "jujutsu kaisen", "tokyo ghoul", "my hero academia"])
    res = requests.get(f"{BASE_URL}/{query}")

    if res.status_code != 200:
        return {"error": "Failed to fetch from Consumet"}

    data = res.json()
    return {
        "title": data.get("title"),
        "image": data.get("image"),
        "episodes": data.get("episodes"),
        "description": data.get("description")
    }

@app.get("/search")
def search_anime(q: str):
    res = requests.get(f"{BASE_URL}?keyw={q}")
    if res.status_code != 200:
        return {"error": "Search failed"}

    return res.json()
