import streamlit as st
from gamification_service import get_level

def show_game():

    st.header("Savings Game")

    saved = st.number_input(
        "Amount Saved",
        min_value=0.0
    )

    st.success(
        get_level(saved)
    )
