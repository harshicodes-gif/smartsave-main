import streamlit as st

def show_ai_settings():

    st.header("⚙️ AI Settings")

    st.write(
        "Configure your AI provider."
    )

    provider = st.radio(
        "Select AI Provider",
        [
            "Ollama (Local)",
            "BYOK"
        ]
    )

    st.session_state.ai_provider = provider

    if provider == "Ollama (Local)":

        st.subheader("Ollama Configuration")

        st.text_input(
            "Ollama URL",
            value="http://localhost:11434",
            key="ollama_url"
        )

        st.text_input(
            "Model Name",
            value="llama3",
            key="ollama_model"
        )

        st.success(
            "Ollama Local AI configured."
        )

    else:

        st.subheader("Bring Your Own Key")

        st.text_input(
            "API Key",
            type="password",
            key="api_key"
        )

        st.success(
            "API Key stored for current session."
        )

    st.info(
        f"Current Provider: {st.session_state.ai_provider}"
    )
