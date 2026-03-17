import pandas as pd

df = pd.read_csv("data/bitcoin_with_trends.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Trends değerlerini ileri ve geri doldur
df["google_trends_score"] = df["google_trends_score"].ffill().bfill()

df.to_csv("data/bitcoin_with_trends_filled.csv", index=False)

print(df.head())
print(df.tail())
print(df.isna().sum())
print("Saved to data/bitcoin_with_trends_filled.csv")