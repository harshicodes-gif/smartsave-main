import streamlit as st

from db import init_db
from auth_service import (
    register_user,
    login_user
)

from dashboard import show_dashboard
from analytics import show_analytics
from ai_coach import show_ai_coach
from savings_game import show_game

init_db()

st.set_page_config(
    page_title="SmartSave",
    page_icon="💰",
    layout="wide"
)

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:

    st.markdown("""
    # 💰 SmartSave

    Pocket Money Manager For Students
    """)

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Register"
        ]
    )

    with tab1:

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = login_user(
                username,
                password
            )

            if user:

                st.session_state.user = username

                st.rerun()

            else:

                st.error(
                    "Invalid credentials"
                )

    with tab2:

        new_user = st.text_input(
            "Create Username"
        )

        new_pass = st.text_input(
            "Create Password",
            type="password"
        )

        if st.button("Register"):

            if register_user(
                new_user,
                new_pass
            ):

                st.success(
                    "Account created!"
                )

            else:

                st.error(
                    "Username already exists"
                )

    st.stop()

st.sidebar.success(
    f"Logged in as {st.session_state.user}"
)

if st.sidebar.button("Logout"):

    st.session_state.user = None

    st.rerun()

st.markdown("""
<style>

.stApp{
background:#F8F8F4;
}

</style>
""",
unsafe_allow_html=True)

st.title("💰 SmartSave")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "AI Coach",
        "Savings Game"
    ]
)

if menu == "Dashboard":
    show_dashboard()

elif menu == "Analytics":
    show_analytics()

elif menu == "AI Coach":
    show_ai_coach()

elif menu == "Savings Game":
    show_game()
