from fastapi import FastAPI
import cloudscraper
import random

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Anime World API is online"}

@app.get("/random-anime")
def random_anime():
    try:
        scraper = cloudscraper.create_scraper()
        url = "https://animepahe.ru/api?m=search&q="
        response = scraper.get(url)

        data = response.json()
        anime_list = data.get("data", [])

        if not anime_list:
            return {"error": "No anime found in response."}

        selected = random.choice(anime_list)
        return {
            "title": selected.get("title"),
            "type": selected.get("type"),
            "year": selected.get("year"),
            "id": selected.get("id"),
            "slug": selected.get("slug")
        }

    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}
