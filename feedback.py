import streamlit as st
import sqlite3


def save_feedback(username, rating, feedback):

    conn = sqlite3.connect(
        "smartsave.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            rating INTEGER,
            feedback TEXT
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO feedback
        (
            username,
            rating,
            feedback
        )
        VALUES (?, ?, ?)
        """,
        (
            username,
            rating,
            feedback
        )
    )

    conn.commit()
    conn.close()


def show_feedback():

    language = st.session_state.language

    titles = {
        "English": "💬 Feedback",
        "Hindi": "💬 प्रतिक्रिया",
        "Telugu": "💬 అభిప్రాయం"
    }

    descriptions = {
        "English":
            "Share your suggestions, ideas, complaints or feature requests. You can write in any language.",

        "Hindi":
            "अपने सुझाव, विचार, शिकायतें या फीचर अनुरोध साझा करें। आप किसी भी भाषा में लिख सकते हैं।",

        "Telugu":
            "మీ సూచనలు, ఆలోచనలు, ఫిర్యాదులు లేదా ఫీచర్ అభ్యర్థనలను పంచుకోండి. మీరు ఏ భాషలోనైనా వ్రాయవచ్చు."
    }

    rating_labels = {
        "English": "Rate SmartSave",
        "Hindi": "SmartSave को रेट करें",
        "Telugu": "SmartSave కు రేటింగ్ ఇవ్వండి"
    }

    feedback_labels = {
        "English": "Your Feedback",
        "Hindi": "आपकी प्रतिक्रिया",
        "Telugu": "మీ అభిప్రాయం"
    }

    submit_labels = {
        "English": "Submit Feedback",
        "Hindi": "प्रतिक्रिया भेजें",
        "Telugu": "అభిప్రాయం పంపండి"
    }

    success_labels = {
        "English": "Thank you for your feedback!",
        "Hindi": "आपकी प्रतिक्रिया के लिए धन्यवाद!",
        "Telugu": "మీ అభిప్రాయానికి ధన్యవాదాలు!"
    }

    warning_labels = {
        "English": "Please enter feedback.",
        "Hindi": "कृपया प्रतिक्रिया दर्ज करें।",
        "Telugu": "దయచేసి అభిప్రాయం నమోదు చేయండి."
    }

    st.header(
        titles[language]
    )

    st.write(
        descriptions[language]
    )

    rating = st.slider(
        rating_labels[language],
        1,
        5,
        5
    )

    feedback = st.text_area(
        feedback_labels[language]
    )

    if st.button(
        submit_labels[language]
    ):

        if feedback.strip():

            save_feedback(
                st.session_state.user,
                rating,
                feedback
            )

            st.success(
                success_labels[language]
            )

        else:

            st.warning(
                warning_labels[language]
            )
