def auto_categorize(text):

    text = text.lower()

    if "pizza" in text:
        return "Food"

    elif "bus" in text:
        return "Travel"

    elif "movie" in text:
        return "Entertainment"

    return "Other"
