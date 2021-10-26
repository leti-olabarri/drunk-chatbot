import streamlit as st
from api import chat

def chatbot():
    st.title("¡Habla conmigo!")

    user_input = st.text_input('Dime algo')
    
    if user_input:
        chat_response = chat(user_input)

        st.text(chat_response)

    st.image("public/girl.jpeg")
    st.write("Ten paciencia conmigo, soy un poco lenta... la resaca, ya sabes")