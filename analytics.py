import streamlit as st
import pandas as pd
import plotly.express as px

from budget_service import get_transactions
from translations import translations


def show_analytics():

    language = st.session_state.language
    t = translations[language]

    st.header(
        t["analytics"]
    )

    transactions = get_transactions(
        st.session_state.user
    )

    if not transactions:

        st.warning(
            {
                "English": "No expense data available.",
                "Hindi": "कोई खर्च डेटा उपलब्ध नहीं है।",
                "Telugu": "ఖర్చుల సమాచారం అందుబాటులో లేదు."
            }[language]
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

    st.subheader(
        t["category_spending"]
    )

    category_summary = (
        df.groupby("Category")["Amount"]
        .sum()
        .reset_index()
    )

    chart_title = {
        "English": "Spending By Category",
        "Hindi": "श्रेणी अनुसार खर्च",
        "Telugu": "వర్గాల వారీగా ఖర్చులు"
    }[language]

    fig = px.bar(
        category_summary,
        x="Category",
        y="Amount",
        title=chart_title
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    highest = category_summary.loc[
        category_summary["Amount"].idxmax()
    ]

    highest_text = {
        "English": f"Highest spending category: {highest['Category']} (₹{highest['Amount']:.2f})",
        "Hindi": f"सबसे अधिक खर्च की श्रेणी: {highest['Category']} (₹{highest['Amount']:.2f})",
        "Telugu": f"అత్యధిక ఖర్చు చేసిన వర్గం: {highest['Category']} (₹{highest['Amount']:.2f})"
    }[language]

    st.success(
        highest_text
    )

    st.subheader(
        t["detailed_summary"]
    )

    st.dataframe(
        category_summary,
        use_container_width=True
    )

    st.subheader(
        t["all_transactions"]
    )

    st.dataframe(
        df,
        use_container_width=True
    )
