from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool
load_dotenv()

class TravelResponse(BaseModel):
    flight_details: str
    destination: str
    duration_days: int
    budget_usd: float
    activities: list[str]
    housing: str
    dining_preferences: list[str]
    transportation: str
    sources_used: list[str]



llm = ChatOpenAI(model="gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object=TravelResponse)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a travel assistant that will help generate a travel plan. For flight information, use the date and time from the timestamp. For activities, suggest extremely specific names and locations with dates if possible.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools,

)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("Where would you like to travel, and how can I help plan your trip? ")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response.model_dump_json(indent=2))
except Exception as e:
    print("Error parsing response:", e, "Raw Response - ", raw_response)