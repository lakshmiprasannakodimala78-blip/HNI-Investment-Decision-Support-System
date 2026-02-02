import matplotlib.pyplot as plt

def plot_market_cap(df):
    plt.bar(df["Company"], df["MarketCap"])
    plt.title("Market Capitalization Comparison")
    plt.xticks(rotation=45)
    plt.ylabel("Market Cap (USD Billion)")
    plt.tight_layout()
    plt.show()
