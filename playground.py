import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq

import os
import phi
from phi.playground import Playground, serve_playground_app

# Load environmnet variable from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

## Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role = "Search the web for information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["1. Perform targeted searches to find the most relevant and recent financial information.",
        "2. Always verify the credibility of sources before including them in the response.",
        "3. Summarize the information concisely and include direct links to the sources.",
        "4. If no relevant information is found, state this clearly and suggest alternative search terms."],
    show_tools_calls=True,
    markdown=True,
)

## Financial Agent
finance_agent = Agent(
    name="Financial Agent",
    role="Get and analyze financial data",
    model=Groq(id="llama3-70b-8192"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True),
    ],
    instructions=[
        "1. Use tables to display stock data for better readability.",
        "2. Always include the following details for any stock:",
        "   - Current price",
        "   - Key fundamentals (e.g., P/E ratio, market cap)",
        "   - Latest analyst recommendations (Buy/Hold/Sell)",
        "   - Recent company news (last 7 days)",
        "3. If data is unavailable, explain why and suggest alternative tools or sources.",
        "4. Keep the response concise and avoid unnecessary details.",
    ],
    show_tools_calls=True,
    markdown=True,
)


app=Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playground:app",reload=True)

