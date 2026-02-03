# 🤖 Groq LangChain AI Assistant

> A multi-tool AI assistant built with **Groq LLM**, **LangChain**, and **Streamlit** — featuring chat, live web search, and AI-powered CSV data analysis.

Built as a modular, production-style project demonstrating LLM integration, tool agents, and secure API handling.

---

## ✨ Features

 Conversational AI Chat (Groq LLM)  
 Real-time Web Search (Tavily API)  
 CSV Data Analysis Agent (LangChain Pandas Agent)  
 Modular Service Architecture  
 Streamlit Interactive UI  
 Session Memory Handling  
 Secure API Key Management (.env)  
 GitHub-ready Project Structure  

---

## 🧠 Tech Stack

| Layer | Technology |
|--------|-------------|
LLM | Groq (llama-3.1-8b-instant) |
Framework | LangChain |
UI | Streamlit |
Data Agent | LangChain Pandas Agent |
Search | Tavily API |
Language | Python |
Env Mgmt | python-dotenv |

---

## 🏗️ Project Architecture

```
app.py → UI + mode routing
services/
   groq_chat.py → LLM chat service
   tavily_search.py → web search tool
   csv_agent.py → dataframe agent
utils/
   session.py → Streamlit session manager
```

Service-oriented design — each capability is isolated and reusable.

---

## 🚀 Demo Modes

### 💬 Chat Mode
Ask general questions — powered by Groq LLM.

### 🔍 Search Mode
Live web search with summarized results.

### 📊 CSV Mode
Upload CSV → ask natural language questions → AI analyzes data.

Examples:
```
What are the top 5 values?
Show summary statistics
Which column has highest mean?
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

`.env` is excluded via `.gitignore` for security.

---

## ⚡ Quick Setup

```bash
git clone https://github.com/<your-username>/groq-langchain-ai-assistant
cd groq-langchain-ai-assistant

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
```

Run app:

```bash
streamlit run app.py
```

Open browser → http://localhost:8501

---

## 📦 Requirements

```
streamlit
groq
langchain
langchain-groq
langchain-experimental
tavily-python
pandas
python-dotenv
```

---

## 🎯 What This Project Demonstrates

- LLM API integration
- Tool-based agent design
- Modular Python architecture
- Secure secret management
- Interactive AI UI development
- Data agent orchestration
- Prompt-driven analytics

---

## 🧪 Example Use Cases

- AI assistant prototype
- Data exploration assistant
- Hackathon starter template
- LLM tool-agent demo
- Streamlit AI dashboard

---

## 📈 Possible Extensions

- Vector DB + RAG
- PDF question answering
- Memory persistence
- Multi-model selector
- Tool router agent
- Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Vikash Kumar**  
ECE Engineer • AI + IoT + LLM Projects  
GitHub: https://github.com/<your-username>

---

## ⭐ If You Found This Useful

Give the repo a star — it helps visibility and supports the project.

