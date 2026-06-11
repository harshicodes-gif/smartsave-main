import streamlit as st

def show_ai_settings():

    st.header("⚙️ AI Settings")

    provider = st.radio(
        "AI Provider",
        [
            "Ollama (Local)",
            "BYOK"
        ]
    )

    st.session_state.ai_provider = provider

    if provider == "Ollama (Local)":

        st.text_input(
            "Ollama URL",
            value="http://localhost:11434",
            key="ollama_url"
        )

        st.text_input(
            "Model",
            value="llama3",
            key="ollama_model"
        )

        st.success(
            "Local AI configured."
        )

    else:

        st.text_input(
            "API Key",
            type="password",
            key="api_key"
        )

        st.success(
            "API key stored for current session."
        )
