import streamlit as st

def show_game():

    st.header("🎮 Savings Challenge")

    saved = st.number_input(
        "How much have you saved?",
        min_value=0.0
    )

    if saved < 1000:

        level = "🥉 Bronze Saver"

    elif saved < 5000:

        level = "🥈 Silver Saver"

    else:

        level = "🏆 Gold Saver"

    st.success(
        f"Current Level: {level}"
    )

    progress = min(saved / 5000, 1.0)

    st.progress(progress)
    
