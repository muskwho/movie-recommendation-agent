**CineMate — AI Movie Recommendation Agent**

A multi-agent, tool-driven system that recommends movies based on user genres and preferences, powered by a curated dataset, LLM reasoning, and lightweight memory.

CineMate helps users instantly discover movies tailored to their tastes. Instead of scrolling endlessly through streaming platforms, users simply describe the genre or mood they want — and the agent provides curated, intelligent recommendations. The system uses a structured dataset, a multi-agent pipeline, and an optional UI for smooth interaction.

⭐ Key Features

🎯 Multi-Agent Architecture

A pipeline of specialized agents, each responsible for one stage of reasoning:

Query Agent — interprets user input, extracts genre/mood, normalizes the query

Genre Filter Agent — retrieves matching movies from the dataset

Recommendation Agent (LLM) — ranks, refines, and explains recommendations

Memory Agent — stores user preferences across a session

🛠️ Custom Tools & Data Handling

Local JSON movie dataset (movies_250.json)

Custom Python filtering functions

Modular design (easy to extend with APIs like TMDB/IMDB later)

🧠 Memory & Session Management

Remembers previously chosen genres

Adapts future recommendations

Lightweight memory stored as JSON

🔄 Context Engineering & Logging

Query cleaning + context compression

Simple logging for debugging and observability

🖥️ Dual Interface Support

Command-line (Python) — run directly through VS Code

Optional Streamlit UI — more interactive browsing

📁 Clean and Extensible Project Structure

Easy to update the dataset

Swap out agents or add new ones without breaking the system

🚀 Purpose

Choosing a movie is surprisingly difficult — people spend minutes (sometimes hours) bouncing across apps, reading reviews, and making unsatisfying choices.

CineMate solves this by acting as a personal movie concierge, reducing decision time and giving high-quality recommendations instantly.

🧠 Agent Architecture

CineMate uses a multi-agent pipeline, where each agent performs one well-defined role.

1. Query Agent (LLM Agent)

Interprets user input

Extracts genres, moods, keywords

Handles vague or ambiguous queries

Normalizes context before passing it forward

2. Genre Filter Agent (Retrieval Agent)

Reads from movies_250.json

Filters by:

Primary genre

Optional keywords

Year or rating (if user mentions them)

Returns a candidate movie list

3. Recommendation Agent (LLM)

Ranks movies

Formats them into conversational output

Can generate:

Top picks

Mood-specific suggestions

Summaries or reasons to watch

4. Memory Agent

Stores last requested genre

Tracks user tendencies

Improves recommendations within the same session

📂 Dataset

The movies_250.json dataset contains 250 hand-curated movies across genres:

Action

Sci-Fi

Comedy

Romance

Thriller

Horror

Animation

Drama

Each movie includes:
title, genre, year, rating, summary, director, cast, enabling rich reasoning in a small dataset.

This dataset is intentionally lightweight — perfect for local agent experimentation.

