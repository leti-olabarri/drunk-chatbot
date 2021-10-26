import streamlit as st
from pages.chatbot import chatbot

st.header("Chatbot borracho")

st.sidebar.title("Navegación")
pages = st.sidebar.radio("Páginas", ["Chatbot"])

if pages == "Chatbot":
    chatbot()