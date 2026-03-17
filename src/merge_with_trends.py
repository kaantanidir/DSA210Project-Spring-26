import pandas as pd

market = pd.read_csv("data/bitcoin_market_clean.csv")
trends = pd.read_csv("data/google_trends_bitcoin.csv", skiprows=2)

print("Trends columns:", trends.columns.tolist())
print(trends.head())

if len(trends.columns) < 2:
    raise ValueError(
        f"Google Trends dosyası beklenen formatta değil. Kolonlar: {trends.columns.tolist()}"
    )

date_col = trends.columns[0]
score_col = trends.columns[1]

trends = trends.rename(columns={
    date_col: "date",
    score_col: "google_trends_score"
})

market["date"] = pd.to_datetime(market["date"]).dt.date
trends["date"] = pd.to_datetime(trends["date"]).dt.date

merged = market.merge(trends, on="date", how="left")
merged.to_csv("data/bitcoin_with_trends.csv", index=False)

print(merged.head())
print(merged.tail())
print("Saved to data/bitcoin_with_trends.csv")