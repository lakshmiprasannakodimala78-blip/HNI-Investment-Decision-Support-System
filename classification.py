def market_cap_category(market_cap):
    if market_cap >= 500:
        return "Above $500B"
    elif market_cap >= 100:
        return "$100B–$500B"
    else:
        return "Below $100B"

def classify_companies(df):
    df["MarketCap Category"] = df["MarketCap"].apply(market_cap_category)
    return df
