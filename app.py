import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st

from backend.database.db import init_db

from frontend.pages.dashboard import show_dashboard
from frontend.pages.analytics import show_analytics
from frontend.pages.ai_coach import show_ai_coach
from frontend.pages.savings_game import show_game

init_db()

st.set_page_config(
    page_title="SmartSave",
    page_icon="💰",
    layout="wide"
)

st.title("💰 SmartSave")

menu = st.sidebar.selectbox(
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
