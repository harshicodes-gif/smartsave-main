import streamlit as st
import pandas as pd
import plotly.express as px

from budget_service import get_transactions
from translations import translations


def show_analytics():

    language = st.session_state.language
    t = translations[language]

    st.header(t["analytics"])

    transactions = get_transactions(
        st.session_state.user
    )

    if not transactions:

        st.warning(
            "No expense data available."
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

    st.subheader("Category Wise Spending")

    category_summary = (
        df.groupby("Category")["Amount"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_summary,
        x="Category",
        y="Amount",
        title="Spending By Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    highest = category_summary.loc[
        category_summary["Amount"].idxmax()
    ]

    st.success(
        f"Highest spending category: {highest['Category']} (₹{highest['Amount']:.2f})"
    )

    st.subheader("Detailed Summary")

    st.dataframe(
        category_summary,
        use_container_width=True
    )

    st.subheader("All Transactions")

    st.dataframe(
        df,
        use_container_width=True
    )
