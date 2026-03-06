from pytrends.request import TrendReq

def get_trending():

    pytrends = TrendReq()

    anime = [
        "Jujutsu Kaisen",
        "Demon Slayer",
        "One Piece",
        "Chainsaw Man",
        "Solo Leveling"
    ]

    pytrends.build_payload(anime, timeframe="now 1-d")

    data = pytrends.interest_over_time()

    if data.empty:
        return anime[0]

    return data.iloc[-1].idxmax()