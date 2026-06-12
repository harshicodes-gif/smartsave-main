import streamlit as st
import pandas as pd

from budget_service import get_transactions
from ai_coach_service import get_tip
from translations import translations


def show_ai_coach():

    language = st.session_state.language
    t = translations[language]

    st.header(
        t["ai_coach"]
    )

    transactions = get_transactions(
        st.session_state.user
    )

    if not transactions:

        message = {
            "English": "Add expenses first to receive advice.",
            "Hindi": "सलाह प्राप्त करने के लिए पहले खर्च जोड़ें।",
            "Telugu": "సలహా పొందడానికి ముందుగా ఖర్చులు జోడించండి."
        }[language]

        st.info(
            message
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

    top_category = (
        df.groupby("Category")["Amount"]
        .sum()
        .idxmax()
    )

    st.subheader(
        t["financial_analysis"]
    )

    total_text = {
        "English": f"Total Spending: ₹{total:.2f}",
        "Hindi": f"कुल खर्च: ₹{total:.2f}",
        "Telugu": f"మొత్తం ఖర్చు: ₹{total:.2f}"
    }[language]

    st.write(
        total_text
    )

    category_text = {
        "English": f"Highest Spending Category: {top_category}",
        "Hindi": f"सबसे अधिक खर्च की श्रेणी: {top_category}",
        "Telugu": f"అత్యధిక ఖర్చు చేసిన వర్గం: {top_category}"
    }[language]

    st.write(
        category_text
    )

    if total < 1000:

        message = {
            "English": "Excellent work. Your spending is under control.",
            "Hindi": "बहुत बढ़िया। आपका खर्च नियंत्रण में है।",
            "Telugu": "అద్భుతం. మీ ఖర్చులు నియంత్రణలో ఉన్నాయి."
        }[language]

        st.success(
            message
        )

    elif total < 3000:

        message = {
            "English": "Try reducing non-essential spending by 10%.",
            "Hindi": "अनावश्यक खर्चों को 10% कम करने का प्रयास करें।",
            "Telugu": "అవసరం లేని ఖర్చులను 10% తగ్గించడానికి ప్రయత్నించండి."
        }[language]

        st.warning(
            message
        )

    else:

        message = {
            "English": "Spending is high. Consider setting weekly limits.",
            "Hindi": "खर्च अधिक है। साप्ताहिक सीमा निर्धारित करें।",
            "Telugu": "ఖర్చు ఎక్కువగా ఉంది. వారాంతపు పరిమితులను నిర్ణయించండి."
        }[language]

        st.error(
            message
        )

    balance = 5000 - total

    st.subheader(
        t["recommendation"]
    )

    st.info(
        get_tip(balance)
    )

    provider = st.session_state.get(
        "ai_provider",
        "Ollama (Local)"
    )

    provider_text = {
        "English": f"AI Provider: {provider}",
        "Hindi": f"एआई प्रदाता: {provider}",
        "Telugu": f"ఏఐ ప్రొవైడర్: {provider}"
    }[language]

    st.success(
        provider_text
    )
