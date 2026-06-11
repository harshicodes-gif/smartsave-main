import streamlit as st
import pandas as pd

from budget_service import get_transactions

def show_ai_coach():

    st.header("🤖 SmartSave AI Coach")

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

    st.subheader("Your Financial Analysis")

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

    st.subheader("Recommendation")

    st.info(
        f"Try reducing {top_category} expenses by 10-15% this month."
    )
