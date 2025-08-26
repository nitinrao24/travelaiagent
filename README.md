# travelaiagent
Project Overview:
Travel AI Agent is a Python application that takes your stated interests and destination, then generates a day-by-day plan of activities, lodging, dining, and transit recommendations.

Features Developed:

1 ) Isolated Python Environment:
    Created a venv to manage all dependencies separately from global packages, ensuring consistent installs and reproducible runs on any machine.

2 ) User → AI → Parser Pipeline (LangChain):
    Integrated LangChain to coordinate prompt templates, chain executions, and parser functions—so raw user text flows into the LLM and comes out as structured itinerary data.

3 ) Strict Data Schemas (Pydantic):
    Defined Pydantic models for UserProfile, RecommendationRequest, and ItineraryItem, enabling automatic type checking, input validation, and clear error messages whenever data formats don’t match.

4 ) LLM-Driven Recommendations:
    Hooked into GPT-style endpoints to interpret natural-language interests, blending open-ended language understanding with custom rules for travel planning.

5 ) Embedding-Based Collaborative Filtering:
    Generated vector embeddings for user preferences and candidate activities via the embedding API, then ranked options by cosine similarity to surface the most relevant suggestions.

6 ) Custom Runtime Tools:
    Built Python functions that the LLM can invoke at runtime to
    Query external APIs (e.g., place searches)
    Write completed itineraries to timestamped .txt files automatically

Each feature was designed for clarity, modularity, and ease of review so that you can see exactly how data moves from user input through AI processing to a saved trip plan.
