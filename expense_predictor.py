import pandas as pd
import streamlit as st
from budget_service import get_pocket_money, get_transactions


def show_expense_predictor():

    st.header("📈 Expense Predictor")

    transactions = get_transactions(st.session_state.user)

    if not transactions:
        st.warning("No transaction data available for prediction.")
        return

    df = pd.DataFrame(
        transactions,
        columns=["ID", "Username", "Category", "Amount", "Description"],
    )

    pocket_money = get_pocket_money(st.session_state.user)

    total_spent = df["Amount"].sum()
    avg_expense = df["Amount"].mean()
    transaction_count = len(df)

    st.subheader("Current Spending Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Spent", f"₹{total_spent:.2f}")
    c2.metric("Transactions", transaction_count)
    c3.metric("Average Expense", f"₹{avg_expense:.2f}")

    st.divider()

    expected_transactions = st.number_input(
        "Expected remaining transactions this month",
        min_value=0,
        value=5,
        step=1,
    )

    predicted_total = total_spent + (avg_expense * expected_transactions)

    remaining = pocket_money - predicted_total

    st.subheader("Prediction")

    st.metric(
        "Predicted Month-End Spending",
        f"₹{predicted_total:.2f}",
    )

    progress = min(predicted_total / pocket_money, 1.0)
    st.progress(progress)

    if predicted_total > pocket_money:
        st.error(f"You are likely to exceed your budget by ₹{abs(remaining):.2f}")
    else:
        st.success(
            f"You are likely to stay within your budget.\n\nEstimated remaining: ₹{remaining:.2f}"
        )
