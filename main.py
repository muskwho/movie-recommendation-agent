import json
from agents.genre_agent import GenreAgent
from agents.filter_agent import FilterAgent
from agents.recommend_agent import RecommendAgent
from agents.memory_agent import MemoryAgent

def load_movies():
    with open("data/movies_250.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    movies = load_movies()
    
    genre_agent = GenreAgent()
    filter_agent = FilterAgent()
    recommend_agent = RecommendAgent()
    memory_agent = MemoryAgent()

    user_input = input("Enter a genre: ")
    normalized_genre = genre_agent.normalize_genre(user_input)
    filtered_movies = filter_agent.filter_by_genre(movies, normalized_genre)
    
    if not filtered_movies:
        print(f"No movies found for genre: {normalized_genre}")
        return

    recommendations = recommend_agent.recommend(filtered_movies)
    memory_agent.update_memory(normalized_genre)

    print(f"\nTop {len(recommendations)} {normalized_genre} Movie Recommendations:\n")
    for i, m in enumerate(recommendations, 1):
        print(f"{i}. {m['title']} ({m['year']}) — {m['rating']}/10")
        print(f"   Director: {m['director']}")
        print(f"   Cast: {', '.join(m['cast'])}")
        print(f"   Reason: {m['reason']}")
        print(f"   Summary: {m['summary']}\n")

if __name__ == "__main__":
    main()
