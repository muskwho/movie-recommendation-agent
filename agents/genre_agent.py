class GenreAgent:
    def normalize_genre(self, user_input):
        """Normalize user input to standard genre names."""
        user_input = user_input.strip().lower()
        genre_map = {
            "sci fi": "Sci-Fi",
            "science fiction": "Sci-Fi",
            "romantic": "Romance",
            "thrill": "Thriller",
            "com": "Comedy",
        }
        for key, val in genre_map.items():
            if key in user_input:
                return val
        return user_input.title()
