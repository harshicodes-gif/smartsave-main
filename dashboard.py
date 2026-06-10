import streamlit as st
import pandas as pd
import plotly.express as px

from budget_service import (
    add_transaction,
    get_transactions
)

def show_dashboard():

    st.header("📊 Dashboard")

    col1, col2 = st.columns([1,1])

    with col1:

        st.subheader("Add Expense")

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Travel",
                "Entertainment",
                "Study",
                "Shopping",
                "Other"
            ]
        )

        amount = st.number_input(
            "Amount",
            min_value=0.0
        )

        description = st.text_input(
            "Description"
        )

        if st.button("➕ Add Expense"):

            add_transaction(
                category,
                amount,
                description
            )

            st.success(
                "Expense Added Successfully"
            )

    transactions = get_transactions()

    if not transactions:
        st.info(
            "No expenses added yet."
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

    st.metric(
        "💸 Total Spending",
        f"₹{total:.2f}"
    )

    fig = px.pie(
        df,
        names="Category",
        values="Amount",
        hole=0.5,
        title="Expense Breakdown"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Transaction History")

    st.dataframe(
        df,
        use_container_width=True
    )
