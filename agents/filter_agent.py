class FilterAgent:
    def filter_by_genre(self, movies, genre):
        """Return movies filtered by genre."""
        filtered = [m for m in movies if genre in m["genre"]]
        return filtered

  
