def get_level(total_saved):

    if total_saved > 5000:
        return "🏆 Gold Saver"

    elif total_saved > 2000:
        return "🥈 Silver Saver"

    else:
        return "🥉 Bronze Saver"
