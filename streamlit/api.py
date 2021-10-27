import requests
import streamlit as st
from config import API_URI

def chat(message):
    req = {"message": message}
    res = requests.post(f"{API_URI}/chat", data=req).json()
    return res["message"]