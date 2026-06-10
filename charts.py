import pandas as pd
import plotly.express as px
import streamlit as st

def expense_chart(data):

    if len(data) == 0:
        return

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Category",
            "Amount",
            "Description"
        ]
    )

    fig = px.pie(
        df,
        names="Category",
        values="Amount",
        title="Expense Breakdown"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
