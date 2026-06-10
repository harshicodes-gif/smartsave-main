def get_tip(balance):

    if balance < 500:
        return "Try reducing food delivery expenses."

    elif balance < 1000:
        return "Good job. Save a little more every week."

    else:
        return "Excellent savings habit. Keep it up!"
