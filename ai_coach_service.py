import streamlit as st


def get_tip(balance, top_category):

    language = st.session_state.get(
        "language",
        "English"
    )

    spent = 5000 - balance

    spending_ratio = spent / 5000

    if spending_ratio >= 0.8:

        tips = {

            "English":
                f"You are spending a large portion of your pocket money. Your highest spending category is {top_category}. Consider reducing expenses in this category and setting weekly spending limits.",

            "Hindi":
                f"आप अपनी पॉकेट मनी का बड़ा हिस्सा खर्च कर रहे हैं। आपकी सबसे अधिक खर्च वाली श्रेणी {top_category} है। इस श्रेणी में खर्च कम करने और साप्ताहिक खर्च सीमा निर्धारित करने पर विचार करें।",

            "Telugu":
                f"మీరు మీ పాకెట్ మనీలో ఎక్కువ భాగం ఖర్చు చేస్తున్నారు. మీ అత్యధిక ఖర్చు వర్గం {top_category}. ఈ వర్గంలో ఖర్చులను తగ్గించి వారానికి ఒక ఖర్చు పరిమితిని నిర్ణయించండి."
        }

        return tips[language]

    elif spending_ratio >= 0.5:

        tips = {

            "English":
                f"You are managing reasonably well. Keep an eye on your spending in {top_category} and try to save a little more each week.",

            "Hindi":
                f"आप अच्छी तरह प्रबंधन कर रहे हैं। {top_category} में होने वाले खर्च पर नज़र रखें और हर सप्ताह थोड़ी अधिक बचत करने का प्रयास करें।",

            "Telugu":
                f"మీరు బాగానే నిర్వహిస్తున్నారు. {top_category} వర్గంలోని ఖర్చులను గమనించి ప్రతి వారం కొంచెం ఎక్కువ పొదుపు చేయడానికి ప్రయత్నించండి."
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
