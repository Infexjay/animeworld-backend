from fastapi import FastAPI
import cloudscraper
import random

app = FastAPI()

@app.get("/debug-anime")
def debug_anime():
    try:
        scraper = cloudscraper.create_scraper()
        url = "https://animepahe.ru/api?m=search&q="
        response = scraper.get(url)

        # Show status and raw response text
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "text_snippet": response.text[:300]
        }

    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}
