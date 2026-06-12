import streamlit as st
import sqlite3
import pandas as pd


def show_feedback_viewer():

    language = st.session_state.language

    titles = {
        "English": "📋 Submitted Feedback",
        "Hindi": "📋 प्राप्त प्रतिक्रियाएँ",
        "Telugu": "📋 అందిన అభిప్రాయాలు"
    }

    no_feedback = {
        "English": "No feedback submitted yet.",
        "Hindi": "अभी तक कोई प्रतिक्रिया नहीं मिली।",
        "Telugu": "ఇంకా ఎలాంటి అభిప్రాయాలు లేవు."
    }

    st.header(
        titles[language]
    )

    conn = sqlite3.connect(
        "smartsave.db"
    )

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            rating INTEGER,
            feedback TEXT
        )
        """
    )

    conn.commit()

    df = pd.read_sql_query(
        "SELECT * FROM feedback",
        conn
    )

    conn.close()

    if df.empty:

        st.info(
            no_feedback[language]
        )

        return

    st.dataframe(
        df,
        use_container_width=True
    )
