# AI categorizer
def auto_categorize(text):

    text = text.lower()

    if "pizza" in text:
        return "Food"

    if "bus" in text:
        return "Travel"

    if "movie" in text:
        return "Entertainment"

    return "Other"