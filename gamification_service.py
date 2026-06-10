# Badges and points
def get_level(total_saved):

    if total_saved > 5000:
        return "Gold Saver"

    if total_saved > 2000:
        return "Silver Saver"

    return "Bronze Saver"