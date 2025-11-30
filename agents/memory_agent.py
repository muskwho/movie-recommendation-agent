import json
import os

class MemoryAgent:
    def __init__(self, path="logs/memory.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                self.memory = json.load(f)
        else:
            self.memory = {"requested_genres": []}

    def update_memory(self, genre):
        self.memory["requested_genres"].append(genre)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=2)
