import json
import streamlit as st
from agents.genre_agent import GenreAgent
from agents.filter_agent import FilterAgent
from agents.recommend_agent import RecommendAgent
from agents.memory_agent import MemoryAgent

# Load movies
with open("data/movies_250.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

genre_agent = GenreAgent()
filter_agent = FilterAgent()
recommend_agent = RecommendAgent()
memory_agent = MemoryAgent()

st.title("🎬 Genre-Based Movie Recommendations")

user_input = st.text_input("Enter a genre (e.g., Action, Sci-Fi, Comedy):")
top_n = st.slider("Number of recommendations:", 5, 20, 10)

if st.button("Get Recommendations") and user_input:
    normalized_genre = genre_agent.normalize_genre(user_input)
    filtered = filter_agent.filter_by_genre(movies, normalized_genre)
    if not filtered:
        st.warning(f"No movies found for genre: {normalized_genre}")
    else:
        recommendations = recommend_agent.recommend(filtered, top_n=top_n)
        memory_agent.update_memory(normalized_genre)
        for m in recommendations:
            st.subheader(f"{m['title']} ({m['year']}) — {m['rating']}/10")
            st.write(f"Genres: {', '.join(m['genre'])}")
            st.write(f"Director: {m['director']}")
            st.write(f"Cast: {', '.join(m['cast'])}")
            st.write(f"Reason: {m['reason']}")
            st.write(f"Summary: {m['summary']}")
