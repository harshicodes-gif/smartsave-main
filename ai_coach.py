import streamlit as st
from ai_coach_service import get_tip

def show_ai_coach():

    st.header("AI Savings Coach")

    balance = st.number_input(
        "Current Balance",
        min_value=0.0
    )

    if st.button("Get Advice"):

        st.success(
            get_tip(balance)
        )
