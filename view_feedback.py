import streamlit as st
import sqlite3
import pandas as pd


def show_feedback_viewer():

    st.header("📋 Submitted Feedback")

    conn = sqlite3.connect(
        "smartsave.db"
    )

    df = pd.read_sql_query(
        "SELECT * FROM feedback",
        conn
    )

    conn.close()

    if df.empty:

        st.info(
            "No feedback submitted yet."
        )

        return

    st.dataframe(
        df,
        use_container_width=True
    )
