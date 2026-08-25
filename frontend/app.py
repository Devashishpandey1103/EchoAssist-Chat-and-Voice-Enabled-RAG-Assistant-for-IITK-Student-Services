"""
Streamlit Frontend for EchoAssist Chat & Voice UI
"""
import streamlit as st

st.set_page_config(page_title="EchoAssist - IITK Student Assistant", page_icon="🎓", layout="wide")

st.title("🎓 EchoAssist: Chat & Voice-Enabled RAG Assistant")
st.subheader("IIT Kanpur Student Services & Academic Guidelines")

st.sidebar.header("Navigation & Settings")
voice_mode = st.sidebar.toggle("Enable Voice Mode (STT/TTS)", value=True)

query = st.text_input("Ask a question about IITK Student Services:", placeholder="e.g. How to apply for leave or mess rebate?")

if st.button("Submit Query") or query:
    if query:
        st.info(f"User Query: {query}")
        st.success("EchoAssist: According to IITK guidelines, mess rebate applications must be submitted 3 days prior via the DOSA portal.")
    else:
        st.warning("Please enter a question.")
