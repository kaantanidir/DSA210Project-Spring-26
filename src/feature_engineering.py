import pandas as pd

df = pd.read_csv("data/bitcoin_with_trends_filled.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Günlük getiri
df["daily_return"] = df["price"].pct_change()

# 7 günlük volatilite
df["volatility_7d"] = df["daily_return"].rolling(7).std()

# Trends değişimi
df["trends_change"] = df["google_trends_score"].diff()

# Fiyat değişimi
df["price_change"] = df["price"].diff()

# Ertesi gün yönü
df["target_up_next_day"] = (df["daily_return"].shift(-1) > 0).astype(int)

df.to_csv("data/bitcoin_features.csv", index=False)

print(df.head(10))
print(df[["daily_return", "volatility_7d", "google_trends_score", "trends_change"]].describe())
print("Saved to data/bitcoin_features.csv")