from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.recommender import (
    get_recommendations,
    get_recommendations_by_genre,
    get_recommendations_by_artist
)

app = FastAPI(title="Music Recommendation API")

# Mount static files (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set templates directory (HTML)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


class RecommendationRequest(BaseModel):
    song_title: str | None = None
    genre: str | None = None
    artist: str | None = None
    top_n: int = 10


@app.post("/recommend")
def recommend(request: RecommendationRequest):
    results = []

    if request.song_title:
        song_results = get_recommendations(request.song_title, request.top_n)
        if "recommendations" in song_results:
            results.extend(song_results["recommendations"])

    if request.genre:
        genre_results = get_recommendations_by_genre(request.genre, request.top_n)
        if "recommendations" in genre_results:
            results.extend(genre_results["recommendations"])

    if request.artist:
        artist_results = get_recommendations_by_artist(request.artist, request.top_n)
        if "recommendations" in artist_results:
            results.extend(artist_results["recommendations"])

    # Remove duplicates
    seen = set()
    unique = []
    for item in results:
        key = (item['name'], item['artists'])
        if key not in seen:
            seen.add(key)
            unique.append(item)

    # ✅ Fallback demo recommendations
    if not unique:
        fallback_recommendations = [
            {"name": "Blinding Lights", "artists": "The Weeknd"},
            {"name": "Levitating", "artists": "Dua Lipa"},
            {"name": "Save Your Tears", "artists": "The Weeknd"},
            {"name": "Peaches", "artists": "Justin Bieber"},
            {"name": "Heat Waves", "artists": "Glass Animals"},
        ]
        return {"recommendations": fallback_recommendations[:request.top_n]}

    return {"recommendations": unique[:request.top_n]}
