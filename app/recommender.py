import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load dataset
df = pd.read_csv('data/spotify_tracks.csv')
df.dropna(subset=['name', 'genre', 'artists'], inplace=True)
df.reset_index(drop=True, inplace=True)

# TF-IDF setup
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['name'])

def get_recommendations(song_title: str, top_n: int = 5):
    # Partial match search (case-insensitive)
    matches = df[df['name'].str.contains(song_title, case=False, na=False)]

    if matches.empty:
        return {"message": "Song not found."}

    # Use the first matching song as the reference
    idx = matches.index[0]
    cosine_sim = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = cosine_sim.argsort()[-top_n:][::-1]

    # Ensure the original song appears first
    similar_indices = [idx] + [i for i in similar_indices if i != idx][:top_n]

    recommendations = df.iloc[similar_indices][['name', 'artists', 'genre']].to_dict(orient='records')
    return {"recommendations": recommendations}
def get_recommendations_by_genre(genre: str, top_n: int = 5):
    genre_matches = df[df['genre'].str.contains(genre, case=False, na=False)]
    
    if genre_matches.empty:
        return {"message": "No songs found for this genre."}

    top_songs = genre_matches.sample(n=min(top_n, len(genre_matches)))
    recommendations = top_songs[['name', 'artists', 'genre']].to_dict(orient='records')
    
    return {"recommendations": recommendations}
def get_recommendations_by_artist(artist: str, top_n: int = 5):
    matches = df[df['artists'].str.contains(artist, case=False, na=False)]

    if matches.empty:
        return {"message": "Artist not found."}

    recommendations = matches.sample(n=min(top_n, len(matches)))[['name', 'artists', 'genre']].to_dict(orient='records')
    return {"recommendations": recommendations}
