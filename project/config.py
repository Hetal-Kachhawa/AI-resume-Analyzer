
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

if not MISTRAL_API_KEY:
    MISTRAL_API_KEY = st.secrets["MISTRAL_API_KEY"]

MODEL_NAME = "mistral-small-2603"