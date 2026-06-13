import streamlit as st
import pandas as pd
import plotly.express as px

from budget_service import (
    get_transactions,
    get_pocket_money
)

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
                "English":
                    "No expense data available.",

                "Hindi":
                    "कोई खर्च डेटा उपलब्ध नहीं है।",

                "Telugu":
                    "ఖర్చుల సమాచారం అందుబాటులో లేదు."
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

    pocket_money = get_pocket_money(
        st.session_state.user
    )

    total_spent = df[
        "Amount"
    ].sum()

    remaining = (
        pocket_money
        - total_spent
    )

    utilization = (
        total_spent
        / pocket_money
        * 100
    ) if pocket_money > 0 else 0

    savings_rate = (
        remaining
        / pocket_money
        * 100
    ) if pocket_money > 0 else 0

    c1, c2, c3 = st.columns(3)

    c1.metric(
        {
            "English":
                "Pocket Money",

            "Hindi":
                "पॉकेट मनी",

            "Telugu":
                "పాకెట్ మనీ"
        }[language],
        f"₹{pocket_money:.0f}"
    )

    c2.metric(
        {
            "English":
                "Spent",

            "Hindi":
                "खर्च",

            "Telugu":
                "ఖర్చు"
        }[language],
        f"₹{total_spent:.0f}"
    )

    c3.metric(
        {
            "English":
                "Remaining",

            "Hindi":
                "शेष",

            "Telugu":
                "మిగిలినది"
        }[language],
        f"₹{remaining:.0f}"
    )

    c4, c5 = st.columns(2)

    c4.metric(
        {
            "English":
                "Budget Utilization",

            "Hindi":
                "बजट उपयोग",

            "Telugu":
                "బడ్జెట్ వినియోగం"
        }[language],
        f"{utilization:.1f}%"
    )

    c5.metric(
        {
            "English":
                "Savings Rate",

            "Hindi":
                "बचत दर",

            "Telugu":
                "పొదుపు శాతం"
        }[language],
        f"{savings_rate:.1f}%"
    )

    if utilization >= 80:

        st.error(
            {
                "English":
                    "You have used more than 80% of your budget.",

                "Hindi":
                    "आपने अपने बजट का 80% से अधिक उपयोग कर लिया है।",

                "Telugu":
                    "మీరు మీ బడ్జెట్‌లో 80% కంటే ఎక్కువ ఉపయోగించారు."
            }[language]
        )

    elif utilization >= 50:

        st.warning(
            {
                "English":
                    "You have used more than 50% of your budget.",

                "Hindi":
                    "आपने अपने बजट का 50% से अधिक उपयोग कर लिया है।",

                "Telugu":
                    "మీరు మీ బడ్జెట్‌లో 50% కంటే ఎక్కువ ఉపయోగించారు."
            }[language]
        )

    else:

        st.success(
            {
                "English":
                    "Great job managing your budget.",

                "Hindi":
                    "आप अपना बजट अच्छी तरह प्रबंधित कर रहे हैं।",

                "Telugu":
                    "మీరు మీ బడ్జెట్‌ను బాగా నిర్వహిస్తున్నారు."
            }[language]
        )

    st.subheader(
        t["category_spending"]
    )

    category_summary = (
        df.groupby(
            "Category"
        )["Amount"]
        .sum()
        .reset_index()
    )

    chart_title = {
        "English":
            "Spending By Category",

        "Hindi":
            "श्रेणी अनुसार खर्च",

        "Telugu":
            "వర్గాల వారీగా ఖర్చులు"
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
        category_summary[
            "Amount"
        ].idxmax()
    ]

    highest_text = {

        "English":
            f"Highest spending category: {highest['Category']} (₹{highest['Amount']:.2f})",

        "Hindi":
            f"सबसे अधिक खर्च की श्रेणी: {highest['Category']} (₹{highest['Amount']:.2f})",

        "Telugu":
            f"అత్యధిక ఖర్చు చేసిన వర్గం: {highest['Category']} (₹{highest['Amount']:.2f})"
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
