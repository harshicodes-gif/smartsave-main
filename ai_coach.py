import streamlit as st
import pandas as pd

from budget_service import get_transactions

def show_ai_coach():

    st.header("🤖 SmartSave AI Coach")

    transactions = get_transactions()

    if not transactions:

        st.info(
            "Add expenses first to receive advice."
        )

        return

    df = pd.DataFrame(
        transactions,
        columns=[
            "ID",
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
            "Excellent! Your spending is under control."
        )

    elif total < 3000:

        st.warning(
            "Try reducing unnecessary purchases."
        )

    else:

        st.error(
            "Your expenses are high. Consider setting a budget."
        )

    st.subheader("Recommendation")

    st.info(
        f"Try reducing {top_category} expenses by 10-15% this month."
    )
