import requests
from bs4 import BeautifulSoup

GENIUS_API_TOKEN = "Bearer api_key_here"


def search_song_lyrics(song_title):
    search_url = "https://api.genius.com/search"
    headers = {"Authorization": GENIUS_API_TOKEN}
    params = {"q": song_title}

    try:
        res = requests.get(search_url, headers=headers, params=params)
        res.raise_for_status()
        results = res.json()["response"]["hits"]
        if not results:
            return "Şarkı bulunamadı."

        song_path = results[0]["result"]["path"]
        page = requests.get("https://genius.com" + song_path)
        soup = BeautifulSoup(page.text, "html.parser")

        lyrics = ""
        for div in soup.find_all("div"):
            if div.get("data-lyrics-container") == "true":
                lyrics += div.get_text(separator="\n")

        return lyrics.strip() if lyrics else "Sözler alınamadı."

    except Exception as e:
        return f"Hata: {e}"
