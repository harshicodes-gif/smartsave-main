import streamlit as st
from budget_service import add_transaction, get_transactions

def show_dashboard():

    st.header("💰 Expense Tracker")

    st.subheader("Add Expense")

    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Entertainment", "Study", "Shopping", "Other"]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    description = st.text_input(
        "Description"
    )

    if st.button("Add Expense"):

        add_transaction(
            category,
            amount,
            description
        )

        st.success("Expense Added!")

    st.divider()

    st.subheader("Transaction History")

    transactions = get_transactions()

    if transactions:

        total = sum(row[2] for row in transactions)

        st.metric(
            "Total Expenses",
            f"₹{total:.2f}"
        )

        st.dataframe(
            transactions,
            use_container_width=True
        )

    else:
        st.info("No expenses recorded yet.")
