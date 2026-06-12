import streamlit as st


def get_tip(balance, top_category):

    language = st.session_state.get(
        "language",
        "English"
    )

    if balance < 500:

        tips = {
            "English":
                f"Your highest spending category is {top_category}. Consider reducing expenses in this category to improve your savings.",

            "Hindi":
                f"आपकी सबसे अधिक खर्च वाली श्रेणी {top_category} है। बचत बढ़ाने के लिए इस श्रेणी में खर्च कम करने पर विचार करें।",

            "Telugu":
                f"మీ అత్యధిక ఖర్చు వర్గం {top_category}. పొదుపును పెంచడానికి ఈ వర్గంలోని ఖర్చులను తగ్గించడానికి ప్రయత్నించండి."
        }

        return tips[language]

    elif balance < 1000:

        tips = {
            "English":
                f"Good progress. Monitor your spending in {top_category} and try to save a little more every week.",

            "Hindi":
                f"अच्छी प्रगति। {top_category} में होने वाले खर्च पर नज़र रखें और हर सप्ताह थोड़ी अधिक बचत करने का प्रयास करें।",

            "Telugu":
                f"మంచి పురోగతి. {top_category} వర్గంలోని ఖర్చులను గమనించి ప్రతి వారం కొంచెం ఎక్కువ పొదుపు చేయడానికి ప్రయత్నించండి."
        }

        return tips[language]

    else:

        tips = {
            "English":
                "Excellent savings habit. Keep it up!",

            "Hindi":
                "उत्कृष्ट बचत आदत। इसी तरह जारी रखें!",

            "Telugu":
                "అద్భుతమైన పొదుపు అలవాటు. ఇలాగే కొనసాగించండి!"
        }

        return tips[language]
