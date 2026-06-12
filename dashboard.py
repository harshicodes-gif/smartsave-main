import streamlit as st
import pandas as pd
import plotly.express as px

from budget_service import (
    add_transaction,
    get_transactions,
    delete_transaction
)

from translations import translations


def show_dashboard():

    language = st.session_state.language
    t = translations[language]

    username = st.session_state.user

    st.header(
        t["dashboard"]
    )

    if "pocket_money" not in st.session_state:

    st.session_state.pocket_money = 5000.0

pocket_money = st.number_input(
    t["monthly_pocket_money"],
    min_value=0.0,
    value=st.session_state.pocket_money
)

st.session_state.pocket_money = pocket_money

    category_options = {

        "English": {
            "Food": "Food",
            "Travel": "Travel",
            "Entertainment": "Entertainment",
            "Study": "Study",
            "Shopping": "Shopping",
            "Other": "Other"
        },

        "Hindi": {
            "भोजन": "Food",
            "यात्रा": "Travel",
            "मनोरंजन": "Entertainment",
            "पढ़ाई": "Study",
            "खरीदारी": "Shopping",
            "अन्य": "Other"
        },

        "Telugu": {
            "ఆహారం": "Food",
            "ప్రయాణం": "Travel",
            "వినోదం": "Entertainment",
            "చదువు": "Study",
            "షాపింగ్": "Shopping",
            "ఇతర": "Other"
        }
    }

    selected_category = st.selectbox(
        t["category"],
        list(
            category_options[
                language
            ].keys()
        )
    )

    category = category_options[
        language
    ][
        selected_category
    ]

    amount = st.number_input(
        t["amount"],
        min_value=0.0
    )

    description = st.text_input(
        t["description"]
    )

    if st.button(
        t["add_expense"]
    ):

        add_transaction(
            username,
            category,
            amount,
            description
        )

        st.success(
            t["expense_added"]
        )

        st.rerun()

    transactions = get_transactions(
        username
    )

    if not transactions:

        st.info(
            t["no_expenses"]
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

    total = df[
        "Amount"
    ].sum()

    balance = (
        pocket_money
        - total
    )

    c1, c2, c3 = st.columns(
        3
    )

    c1.metric(
        t["pocket_money"],
        f"₹{pocket_money:.0f}"
    )

    c2.metric(
        t["spent"],
        f"₹{total:.0f}"
    )

    c3.metric(
        t["remaining"],
        f"₹{balance:.0f}"
    )

    fig = px.pie(
        df,
        names="Category",
        values="Amount",
        hole=0.6
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        t["transactions"]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader(
        t["delete_expense"]
    )

    expense_options = {

        f"ID {row['ID']} | {row['Category']} | ₹{row['Amount']}":
        row["ID"]

        for _, row in df.iterrows()
    }

    selected_expense = st.selectbox(
        t["select_expense"],
        list(
            expense_options.keys()
        )
    )

    if st.button(
        "🗑 " + t["delete_expense"]
    ):

        delete_transaction(
            expense_options[
                selected_expense
            ]
        )

        st.success(
            t["expense_deleted"]
        )

        st.rerun()
