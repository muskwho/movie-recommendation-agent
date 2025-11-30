class RecommendAgent:
    def recommend(self, movies, top_n=5):
        """Rank movies by rating and return top N."""
        ranked = sorted(movies, key=lambda x: x["rating"], reverse=True)
        recommendations = ranked[:top_n]
        # Add a reason why each matches the genre
        for m in recommendations:
            m["reason"] = f"A highly rated {m['genre']} movie directed by {m['director']}."
        return recommendations
