# 📈 Financial Agentic AI Application

🚀 Financial Agentic AI Application is an AI-powered financial assistant that provides real-time stock market insights and performs web searches for financial news. It leverages Phi-Agents, Groq's LLaMA3-70B, and external tools like YFinance and DuckDuckGo to offer financial data analysis and market updates.

## 🌟 Features

🔍 Web Search Agent: Fetches the latest financial news and trends using DuckDuckGo.

📊 Financial Agent: Retrieves stock market data, company fundamentals, analyst recommendations, and recent news.

🤖 AI Model: Uses Groq LLaMA3-70B for powerful financial insights.

🛠️ Tool Integrations: Integrates with YFinance, DuckDuckGo, and more.

⚡ FastAPI & Playground UI: Provides an interactive interface for AI-driven financial analysis.

## 📦 Installation

1️⃣ Clone the Repository

$ git clone https://github.com/Yash-Pisat/Financial_Agentic_AI_Application.git
$ cd Financial_Agentic_AI_Application

2️⃣ Create a Virtual Environment (Optional but Recommended)

$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies

$ pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the project root and add:

PHI_API_KEY=your_phi_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

🚀 Running the Application

Start the FastAPI server with:

$ python playground.py

The app runs on the local host, but you can access it from the phidata dashboard.

🛠️ Tools & Technologies

Python 3.8+

FastAPI & Uvicorn

Phi-Agents (AI Framework)

Groq's LLaMA3-70B (LLM Model)

YFinance (Stock Market Data)

DuckDuckGo (Web Search)

🏗️ Future Enhancements

✅ Improve Web Search by integrating Google Search API

✅ Add Streamlit UI for a better user experience

✅ Expand financial analysis tools
