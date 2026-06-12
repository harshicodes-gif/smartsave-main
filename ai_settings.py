import streamlit as st

from translations import translations


def show_ai_settings():

    language = st.session_state.language
    t = translations[language]

    st.header(
        t["ai_settings"]
    )

    st.write(
        t["configure_ai"]
    )

    provider = st.radio(
        t["select_provider"],
        [
            t["ollama"],
            t["byok"]
        ]
    )

    st.session_state.ai_provider = provider

    if provider == t["ollama"]:

        st.subheader(
            t["ollama_config"]
        )

        st.text_input(
            t["ollama_url"],
            value="http://localhost:11434",
            key="ollama_url"
        )

        st.text_input(
            t["model_name"],
            value="llama3",
            key="ollama_model"
        )

        st.success(
            t["local_ai_ready"]
        )

    else:

        st.subheader(
            t["bring_your_key"]
        )

        st.text_input(
            t["api_key"],
            type="password",
            key="api_key"
        )

        st.success(
            t["api_key_saved"]
        )

    st.info(
        f"{t['current_provider']}: {provider}"
    )
