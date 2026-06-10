# Statement parser
def parse_expense(text):

    try:
        parts = text.split(",")

        return {
            "amount": float(parts[0]),
            "description": parts[1]
        }

    except:
        return None