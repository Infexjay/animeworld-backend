from fastapi import FastAPI
import requests
import random

app = FastAPI()

BASE_URL = "https://api.consumet.org/anime/gogoanime"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}

@app.get("/")
def root():
    return {"message": "Anime World API is online"}

@app.get("/random-anime")
def get_random_anime():
    query = random.choice(["naruto", "bleach", "one piece", "tokyo ghoul", "demon slayer", "my hero academia"])
    url = f"{BASE_URL}?keyw={query}"

    try:
        res = requests.get(url, headers=HEADERS)
        res.raise_for_status()
        data = res.json()

        if not data or not isinstance(data, list):
            return {"error": "Invalid or empty data from API", "raw": data}

        selected = random.choice(data)

        return {
            "title": selected.get("title"),
            "image": selected.get("image"),
            "id": selected.get("id"),
            "url": selected.get("url")
        }
    except Exception as e:
        return {"error": str(e), "debug_url": url}
