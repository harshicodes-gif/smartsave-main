import streamlit as st

from translations import translations


def show_game():

    language = st.session_state.language
    t = translations[language]

    st.header(
        t["savings_game"]
    )

    st.subheader(
        t["savings_challenge"]
    )

    saved = st.number_input(
        t["saved_amount"],
        min_value=0.0
    )

    if saved < 1000:

        level = t["bronze"]

    elif saved < 5000:

        level = t["silver"]

    else:

        level = t["gold"]

    current_level_text = {
        "English":
            f"Current Level: {level}",

        "Hindi":
            f"वर्तमान स्तर: {level}",

        "Telugu":
            f"ప్రస్తుత స్థాయి: {level}"
    }[language]

    st.success(
        current_level_text
    )

    progress = min(
        saved / 5000,
        1.0
    )

    st.progress(
        progress
    )

    progress_text = {
        "English":
            f"Progress: {progress * 100:.0f}%",

        "Hindi":
            f"प्रगति: {progress * 100:.0f}%",

        "Telugu":
            f"పురోగతి: {progress * 100:.0f}%"
    }[language]

    st.caption(
        progress_text
    )
