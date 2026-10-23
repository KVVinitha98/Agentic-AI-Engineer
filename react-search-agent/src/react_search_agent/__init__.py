from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages  import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# # implement search tool
# def search(query:str) -> str:
#     """ Take the query string and return the weather information for that query location """
#     # Implement the actual search logic here
#     return "Weather information for " + query + " is sunny with a high of 25°C."

class Source(BaseModel):
    """Represents a source of information with a name and URL."""
    name: str = Field(..., description="Name of the source")
    url: str = Field(..., description="URL of the source")

class AgentResponse(BaseModel):
    """Represents a search result with a list of sources."""
    answer: str = Field(..., description="Answer to the search query")
    sources: List[Source] = Field(..., description="List of sources for the search result")

llm = ChatOpenAI(model="gpt-5.4-mini")
tools =[TavilySearch()]
agent = create_agent(model=llm, tools=tools,response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="search for 3 job postings for an ai engineer using langchain in and around Massachusetts on linkedin and list their details?"
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()


