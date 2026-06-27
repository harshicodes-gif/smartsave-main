import pandas as pd
import streamlit as st
from budget_service import get_pocket_money, get_transactions
from translations import translations


def show_expense_predictor():
    # Current language translations
    t = translations[st.session_state.language]

    st.header(t["expense_predictor"])

    transactions = get_transactions(st.session_state.user)

    if not transactions:
        st.warning(t["insufficient_history"])
        return

    df = pd.DataFrame(
        transactions,
        columns=[
            "ID",
            "Username",
            "Category",
            "Amount",
            "Description",
        ],
    )

    pocket_money = get_pocket_money(st.session_state.user)

    total_spent = df["Amount"].sum()
    avg_expense = df["Amount"].mean()
    transaction_count = len(df)

    st.subheader(t["current_spending_summary"])

    col1, col2, col3 = st.columns(3)

    col1.metric(
        t["total_spent"],
        f"₹{total_spent:.2f}",
    )

    col2.metric(
        t["transactions"],
        transaction_count,
    )

    col3.metric(
        t["average_expense"],
        f"₹{avg_expense:.2f}",
    )

    st.divider()

    expected_transactions = st.number_input(
        t["expected_transactions"],
        min_value=0,
        value=5,
        step=1,
    )

    predicted_total = total_spent + (avg_expense * expected_transactions)

    remaining = pocket_money - predicted_total

    st.subheader(t["prediction"])

    st.metric(
        t["predicted_month_end"],
        f"₹{predicted_total:.2f}",
    )

    if pocket_money > 0:
        progress = min(predicted_total / pocket_money, 1.0)
    else:
        progress = 0.0

    st.progress(progress)

    if predicted_total > pocket_money:
        st.error(f"{t['exceed_budget']} ₹{abs(remaining):.2f}")
    else:
        st.success(
            f"{t['stay_budget']}\n\n" f"{t['estimated_remaining']}: ₹{remaining:.2f}"
        )
