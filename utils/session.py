import streamlit as st

def init_session():
    print("INIT SESSION LOADED")  # debug line
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def clear_session():
    st.session_state.chat_history = []
