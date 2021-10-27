import streamlit as st
from api import chat
import os

def chatbot():
    st.title("¡Habla conmigo!")

    user_input = st.text_input('Dime algo')
    st.text("Leti borracha dice: ")
    if user_input:
        chat_response = chat(user_input)

        st.markdown(chat_response)

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../public/girl.jpeg"))

    st.image(path)
    st.markdown("(Ten paciencia conmigo, soy un poco lenta... la resaca, ya sabes)")