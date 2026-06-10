import streamlit as st

from db import init_db
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

st.markdown("""
<h1 style='text-align:center;'>
💰 SmartSave
</h1>

<h4 style='text-align:center;color:gray;'>
Manage Pocket Money Smarter
</h4>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1554224155-6726b3ff858f",
    use_container_width=True
)

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "",
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
