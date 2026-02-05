# 🤖 Groq AI Assistant

A multi-tool AI assistant built using Groq LLM, LangChain, and Streamlit for chat, live web search, and CSV data analysis.

## Live Demo

Click here to view app  
👉 https://your-streamlit-link.streamlit.app

## Features

- AI chat using Groq LLM  
- Live web search support  
- CSV data analysis with natural language queries  
- Streamlit user interface  
- Session memory handling  
- Modular tool-based design  

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/groq-langchain-ai-assistant
cd groq-langchain-ai-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

Run the app:

```bash
streamlit run app.py
```

## Usage

- Select mode from sidebar:
  - Chat
  - Search
  - CSV Analyze
- Enter your query
- Upload CSV for data analysis mode
- View AI results instantly

## Tech Stack

- Python  
- Streamlit  
- Groq API  
- LangChain  
- Pandas  
- Tavily Search API  

## About

An AI assistant project demonstrating LLM integration, tool agents, and interactive Streamlit deployment. Suitable for AI, LLM, and data tool portfolio projects.
