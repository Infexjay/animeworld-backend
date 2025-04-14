from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
import logging

# Initialize app
app = FastAPI()

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# CORS (Allow all)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Anime World API is online"}

@app.get("/search-anime")
def search_anime(q: str = "naruto"):
    url = f"https://animepahe.ru/api?m=search&q={q}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json"
    }
    
    logging.info(f"Fetching from: {url}")
    logging.info(f"With headers: {headers}")
    
    try:
        r = requests.get(url, headers=headers, timeout=15)
        logging.info(f"Status Code: {r.status_code}")
        logging.info(f"Response Text Snippet: {r.text[:200]}")  # limit log output
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"RequestException: {str(e)}")
        return {"error": f"RequestException: {str(e)}"}
    except ValueError as e:
        logging.error(f"JSON Decode Error: {str(e)}")
        return {"error": f"JSON Decode Error: {str(e)}"}
