# 🎵 ML-Based Music Recommendation Web App

An intelligent web application that suggests songs based on user preferences using **Content-Based Filtering** powered by machine learning. Built with **FastAPI**, **pandas**, **scikit-learn**, and deployed via **Render**.

---

## 📸 Preview

![MUSIC RECOMMENDATION](https://github.com/user-attachments/assets/667a87ee-fcd3-4d05-926c-1a5ebcfee644)

---

## 🚀 Live Demo

👉 [Try it Live on Render](https://ml-based-music-recommendation-web-app.onrender.com)

---

## 💡 Features

- 🎧 Get smart recommendations based on:
  - Song Title
  - Genre
  - Artist
- ✨ Content-Based Filtering using TF-IDF + Cosine Similarity
- 📊 Dataset: 15,000+ curated Spotify tracks
- ⚡️ Real-time API with FastAPI
- 🎨 Responsive UI with HTML, CSS, JavaScript
- 🌍 Deployed on Render with continuous integration

---

## 📁 Tech Stack

| Layer        | Technologies                                |
|--------------|---------------------------------------------|
| 💻 Frontend  | HTML5, CSS3, JavaScript                     |
| ⚙️ Backend   | Python, FastAPI, Uvicorn                    |
| 🧠 ML Logic  | scikit-learn, pandas, TF-IDF                |
| 📦 Hosting   | Render (Live Deployment)                    |
| 🗃️ Dataset   | Spotify Tracks Dataset (CSV, 15K+ entries)  |

---

## 📌 How It Works

1. **Input** a song title, genre, or artist.
2. **TF-IDF Vectorization** transforms song titles into feature vectors.
3. **Cosine Similarity** scores similarities between songs.
4. **Top-N Matches** returned as recommendations.
5. Frontend displays results dynamically.

---

## 🖼️ Dataset + ML Approach

- **Dataset:** `spotify_tracks.csv`
- **Filtering Type:** Content-Based
- **Algorithm:**
  - `TF-IDFVectorizer` from `scikit-learn`
  - `linear_kernel` for similarity computation
- **Random sampling** for genre & artist-based results

---

## 🧪 Future Enhancements

- Collaborative Filtering using user history
- Audio feature embeddings (tempo, energy, valence, etc.)
- Spotify API integration for real-time data
- User login + history-based personalization

---

## 🙋‍♀️ Author

Made with 💙 by [Shaik Alisha Muskaan](https://github.com/alisha-9)

