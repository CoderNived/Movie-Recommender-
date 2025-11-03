import streamlit as st
import pickle
import pandas as pd
import requests

# ------------------- Load Data -------------------
movies_path = r"C:\Users\nived\OneDrive\Desktop\Movie Recommender System\movies.pkl"
similarity_path = r"C:\Users\nived\OneDrive\Desktop\Movie Recommender System\similarity.pkl"

new_df = pickle.load(open(movies_path, 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))

# ------------------- TMDB API CONFIG -------------------
API_KEY = "3417ce8b7a32ceee959905eb4e03b6f2"  # Replace with your API key

def fetch_poster(movie_title):
    """Fetch movie poster from TMDB API"""
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data["results"]:
            poster_path = data["results"][0]["poster_path"]
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
        # fallback placeholder
        return "https://via.placeholder.com/300x450?text=No+Poster"
    except Exception as e:
        print(f"Poster fetch failed for {movie_title}: {e}")
        return "https://via.placeholder.com/300x450?text=No+Poster"

# ------------------- Recommendation Function -------------------
def recommend(movie):
    try:
        movie_index = new_df[new_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_posters = []

        for i in movies_list:
            movie_title = new_df.iloc[i[0]].title
            recommended_movies.append(movie_title)
            recommended_posters.append(fetch_poster(movie_title))

        return recommended_movies, recommended_posters

    except IndexError:
        st.error("Movie not found in the database. Please try another one.")
        return [], []

# ------------------- Streamlit UI -------------------
st.set_page_config(page_title="🎬 Movie Recommender System", layout="centered")

st.title("🎥 Movie Recommender System")
st.write("Get 5 movie recommendations similar to your favorite film!")

selected_movie = st.selectbox(
    "Which movie would you like to watch?",
    new_df['title'].values
)

if st.button("Recommend"):
    recommended_movies, recommended_posters = recommend(selected_movie)

    if recommended_movies:
        st.subheader("✅ Recommended Movies:")
        cols = st.columns(5)
        for i in range(len(recommended_movies)):
            with cols[i]:
                st.image(recommended_posters[i], use_container_width=True)
                st.caption(recommended_movies[i])