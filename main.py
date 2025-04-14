from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import time

app = FastAPI()

@app.get("/")
def scrape_animepahe():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
                      "AppleWebKit/537.36 (KHTML, like Gecko) " +
                      "Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://animepahe.ru/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }

    url = "https://animepahe.ru"

    # Delay is optional here
    time.sleep(5)

    session = requests.Session()
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        return {"status": "success", "title": title}
    else:
        return {"status": "error", "code": response.status_code}
