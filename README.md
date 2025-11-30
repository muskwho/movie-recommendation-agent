🎬 Movie Recommendation Agent (Genre-Based AI Multi-Agent System)

This project is a genre-based movie recommendation agent built as a capstone submission for the "AI Agents" course.  
It is a lightweight AI system that uses **multi-agent architecture**, **custom tools**, and **memory** to deliver smart movie suggestions based on user preferences.

The agent can:
- Understand the user’s movie request (genre, mood, vibe, style).
- Retrieve matching movies from a local dataset.
- Provide recommendations in a friendly, conversational style.
- Run locally through VS Code using Python.

---

🚀 Project Purpose

Many people struggle to choose what movie to watch. Manually searching across platforms wastes time and often results in poor choices.

This project solves that problem by building a **personal movie concierge agent** that recommends films instantly based on genre preferences.

---

🧠 Agent Architecture

This project uses a **multi-agent design**:

1. User Query Agent (LLM Agent)**
- Understands user input  
- Extracts genre and additional filters  
- Interprets unclear queries  
- Passes cleaned query to next agent  

2. Genre Recommendation Agent**
- Reads local `movies_250.json`  
- Filters based on selected genre  
- Returns a list of matching films  
- Acts as the “search engine” of the system  

3. Response Formatting Agent (LLM Agent)**
- Converts raw movie list into  
  - Friendly recommendations  
  - Watch-order suggestions  
  - Optional summaries  

---

 🛠️ Tools & Concepts Implemented

This project includes **more than the required 3 capstone concepts**:

 ✔ Multi-Agent System
- LLM-powered Query Agent  
- Retrieval Agent  
- Output Formatting Agent  

 ✔ Custom Tools
- Custom Movie Search Tool  
- Local JSON dataset tool  

 ✔ Sessions & Memory
- User session context preserved  
- Preferences kept inside memory  

 ✔ Context Engineering
- The query is compressed before passing to agents  
- Reduces token use and increases accuracy  

