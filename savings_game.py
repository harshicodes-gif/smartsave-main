# Savings Game page
import streamlit as st
from backend.services.gamification_service import get_level

def show_game():

    st.header("Savings Game")

    saved = st.number_input(
        "Amount Saved"
    )

    st.success(
        get_level(saved)
    )