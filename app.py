import streamlit as st
from services.groq_chat import GroqChat
from services.tavily_search import TavilySearch
from services.csv_agent import CSVAgent
from utils.session import init_session, clear_session
import pandas as pd

# Fixed: page_title (lowercase), spelling
st.set_page_config(page_title="Groq AI Assistant", layout="wide")

init_session()

with st.sidebar:
    st.title("🤖 AI Assistant")  # Added emoji for better UI
    mode = st.radio("Select Mode:", ["💬 Chat", "🔍 Search", "📊 CSV Analyze"])
    
    if st.button("Clear Session", type="secondary"):
        clear_session()
        st.rerun()

st.title("Groq AI Assistant")

# Fixed: Consistent variable naming
chat_service = GroqChat()  # Changed from chat_services to chat_service
search_service = TavilySearch()
csv_agent = CSVAgent()

if mode == "💬 Chat":
    # Display chat history
    for msg in st.session_state.chat_history:
        # Fixed: st.chat_message (not st.chat_meassage)
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        # Show user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Get and show assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Fixed: Using chat_service (not chat_services)
                response = chat_service.chat(prompt, st.session_state.chat_history)
                st.write(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})

elif mode == "🔍 Search":
    query = st.text_input("Search query:")
    
    if query:
        with st.spinner("Searching..."):
            results = search_service.search(query)
            
            st.subheader("Search Results")
            for i, result in enumerate(results, 1):
                with st.expander(f"Result {i}: {result['title'][:50]}..."):
                    st.write(result['content'])
                    st.caption(f"Source: {result['url']}")

else:  # CSV Mode
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:", df.head())
        
        question = st.text_input("Ask about your data:")
        
        if question:
            with st.spinner("Analyzing..."):
                response = csv_agent.analyze(df, question)
                st.write("🤖 Analysis:", response)  # Added emoji