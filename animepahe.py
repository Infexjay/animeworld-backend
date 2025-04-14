import requests

def get_anime_list():
    url = "https://animepahe.com/api?m=airing"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers)
        data = res.json()
        anime_list = data.get("data", [])

        return [
            {
                "title": anime.get("title", "Unknown Title"),
                "type": anime.get("type", ""),
                "season": anime.get("season", ""),
                "year": anime.get("year", ""),
                "episodes": anime.get("episodes", 0)
            }
            for anime in anime_list
        ]
    except Exception as e:
        return [{"error": str(e)}]
