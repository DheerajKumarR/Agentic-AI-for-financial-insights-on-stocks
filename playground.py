import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os
import phi
from phi.playground import Playground, serve_playground_app
# Load env variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

## web search agent 
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources in your response"],
    show_tools_calls=True, 
    markdown=True, 
)

## financial agent
finance_agent = Agent(
    name="Finance AI Agent",
    role="Analyze stocks and provide financial recommendations",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to diaplay the data"],
    show_tools_calls=True,
    markdown=True,
)

app=Playground(agents=[web_search_agent,finance_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)