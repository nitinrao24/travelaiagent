# travelaiagent
## Summary
This project is an **AI-powered travel assistant** built with **LangChain** and **Pydantic**. It generates structured travel itineraries, answers destination-related queries, and saves results for later use. By connecting a language model with **custom tools**, the agent moves beyond simple text generation to act as an **interactive planner** for real-world travel scenarios.

The system demonstrates how large language models can be extended with **runtime tools** and **schemas** to ensure reliable, reproducible outputs.

---

## Features
- **Conversational Itinerary Planning**: Create day-by-day schedules tailored to user preferences.  
- **Custom Tools (`tools.py`)**:
  - Destination search and filtering  
  - Itinerary building with structured day/time outputs  
  - File saving for generated itineraries and research notes  
- **Pydantic Schemas**: Enforce output consistency across different queries.  
- **Output Storage**: All itineraries and research results are saved in `research_output.txt`.  

---

## Tech Stack
- **Python 3.10+**  
- **LangChain** — LLM orchestration and agent logic  
- **Pydantic** — data validation and schema definition  
- **OpenAI API** — LLM backend  

---

## Example Output
### Example Query
```bash
Plan a 5-day trip to Tokyo focused on food, culture, and shopping.
Example Output (abridged)
Day 1: Arrival, Shinjuku street food tour

Day 2: Tsukiji Outer Market, Ginza shopping, Senso-ji Temple

Day 3: Day trip to Nikko shrines and waterfalls

Day 4: Harajuku fashion, Meiji Shrine, Shibuya nightlife

Day 5: Souvenir shopping and departure

All results are saved automatically in research_output.txt.
```
## How to Run
1. Clone the Repository
```bash
git clone <repo-url>
cd travel-ai-agent
```
2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Add Your API Key
Create a .env file in the project root:
```bash
OPENAI_API_KEY=your_api_key_here
```
5. Run the Agent
```bash
python main.py
```
## Key Insights
Enforcing structured outputs with Pydantic reduces LLM unpredictability.

Saving results into research_output.txt makes itineraries reproducible and trackable.

Custom tools in tools.py allow the agent to perform function calls instead of just generating free-form text.

## Next Steps
Integrate real APIs (Google Maps, Yelp) for live results.

Add budget constraints and cost breakdowns.

Expand GUI or web app frontend for non-technical users.

Use a database for persistent memory across multiple travel plans.

## Project Structure
```plaintext
travel-ai-agent/
│── __pycache__/            # Compiled cache files
│── main.py                 # Entry point for running the agent
│── tools.py                # Custom tools for itinerary and file saving
│── research_output.txt     # Generated itineraries and results
│── requirements.txt        # Python dependencies
│── README.md               # Documentation
