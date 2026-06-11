import streamlit as st
import pandas as pd
import plotly.express as px

from budget_service import (
    add_transaction,
    get_transactions
)

def show_dashboard():

    username = st.session_state.user

    st.header("📊 Dashboard")

    pocket_money = st.number_input(
        "Monthly Pocket Money",
        value=5000.0
    )

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
            username,
            category,
            amount,
            description
        )

        st.success(
            "Expense Added"
        )

    transactions = get_transactions(
        username
    )

    if not transactions:

        st.info(
            "No expenses yet."
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

    balance = pocket_money - total

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Pocket Money",
        f"₹{pocket_money:.0f}"
    )

    c2.metric(
        "Spent",
        f"₹{total:.0f}"
    )

    c3.metric(
        "Remaining",
        f"₹{balance:.0f}"
    )

    fig = px.pie(
        df,
        names="Category",
        values="Amount",
        hole=.6
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        df,
        use_container_width=True
    )
