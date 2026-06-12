import streamlit as st
import pandas as pd

from budget_service import get_transactions
from ai_coach_service import get_tip
from translations import translations


def show_ai_coach():

    language = st.session_state.language
    t = translations[language]

    st.header(t["ai_coach"])

    transactions = get_transactions(
        st.session_state.user
    )

    if not transactions:

        st.info(
            "Add expenses first to receive advice."
        )

        return

    df = pd.DataFrame(
        transactions,
        columns=[
            "ID",
            "Username",
            "Category",
            "Amount",
            "Description"
        ]
    )

    total = df["Amount"].sum()

    top_category = (
        df.groupby("Category")["Amount"]
        .sum()
        .idxmax()
    )

    st.subheader(
        "Your Financial Analysis"
    )

    st.write(
        f"Total Spending: ₹{total:.2f}"
    )

    st.write(
        f"Highest Spending Category: {top_category}"
    )

    if total < 1000:

        st.success(
            """
            Excellent work.

            Your spending is under control.
            """
        )

    elif total < 3000:

        st.warning(
            """
            Try reducing non-essential spending
            by 10%.
            """
        )

    else:

        st.error(
            """
            Spending is high.

            Consider setting weekly limits.
            """
        )

    balance = 5000 - total

    st.subheader(
        t["recommendation"]
    )

    st.info(
        get_tip(balance)
    )

    provider = st.session_state.get(
        "ai_provider",
        "Ollama (Local)"
    )

    st.success(
        f"AI Provider: {provider}"
    )
