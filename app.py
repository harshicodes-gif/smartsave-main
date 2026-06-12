import streamlit as st

from db import init_db
from auth_service import register_user, login_user
from dashboard import show_dashboard
from analytics import show_analytics
from ai_coach import show_ai_coach
from savings_game import show_game
from ai_settings import show_ai_settings
from translations import translations

init_db()

st.set_page_config(
    page_title="SmartSave",
    page_icon="💰",
    layout="wide"
)

if "user" not in st.session_state:
    st.session_state.user = None

if "language" not in st.session_state:
    st.session_state.language = "English"

if "ai_provider" not in st.session_state:
    st.session_state.ai_provider = "Ollama (Local)"

language_label = {
    "English": "🌐 Language",
    "Hindi": "🌐 भाषा",
    "Telugu": "🌐 భాష"
}[st.session_state.language]

language_options = {
    "English": "English",
    "हिन्दी": "Hindi",
    "తెలుగు": "Telugu"
}

reverse_language_options = {
    "English": "English",
    "Hindi": "हिन्दी",
    "Telugu": "తెలుగు"
}

selected_language = st.sidebar.selectbox(
    language_label,
    list(language_options.keys()),
    index=list(language_options.keys()).index(
        reverse_language_options[
            st.session_state.language
        ]
    ),
    key="language_selector"
)

st.session_state.language = language_options[
    selected_language
]

t = translations[
    st.session_state.language
]

# LOGIN / REGISTER PAGE

if st.session_state.user is None:

    st.title(
        t["app_name"]
    )

    st.subheader(
        t["tagline"]
    )

    tab1, tab2 = st.tabs(
        [
            t["login"],
            t["register"]
        ]
    )

    with tab1:

        username = st.text_input(
            t["username"]
        )

        password = st.text_input(
            t["password"],
            type="password"
        )

        if st.button(
            t["login"]
        ):

            user = login_user(
                username,
                password
            )

            if user:

                st.session_state.user = username
                st.rerun()

            else:

                st.error(
                    t["invalid_login"]
                )

    with tab2:

        new_user = st.text_input(
            t["create_username"]
        )

        new_pass = st.text_input(
            t["create_password"],
            type="password"
        )

        if st.button(
            t["register"]
        ):

            if register_user(
                new_user,
                new_pass
            ):

                st.success(
                    t["account_created"]
                )

            else:

                st.error(
                    t["username_exists"]
                )

    st.stop()

logged_in_text = {
    "English": f"Logged in as: {st.session_state.user}",
    "Hindi": f"लॉग इन उपयोगकर्ता: {st.session_state.user}",
    "Telugu": f"లాగిన్ అయిన వినియోగదారు: {st.session_state.user}"
}[st.session_state.language]

st.sidebar.success(
    logged_in_text
)

if st.sidebar.button(
    t["logout"]
):
    st.session_state.user = None
    st.rerun()

st.title(
    t["app_name"]
)

st.caption(
    t["tagline"]
)

menu = st.sidebar.radio(
    t["navigation"],
    [
        t["dashboard"],
        t["analytics"],
        t["ai_coach"],
        t["ai_settings"],
        t["savings_game"]
    ]
)

if menu == t["dashboard"]:

    show_dashboard()

elif menu == t["analytics"]:

    show_analytics()

elif menu == t["ai_coach"]:

    show_ai_coach()

elif menu == t["ai_settings"]:

    show_ai_settings()

elif menu == t["savings_game"]:

    show_game()
