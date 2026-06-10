import streamlit as st
from budget_service import get_transactions

def show_dashboard():

    st.header("Dashboard")

    transactions = get_transactions()

    total = sum(
        row[2]
        for row in transactions
    )

    st.metric(
        "Total Expenses",
        f"₹{total:.2f}"
    )

    st.subheader("Transactions")

    st.write(transactions)
