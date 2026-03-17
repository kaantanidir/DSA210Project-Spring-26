import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/bitcoin_features.csv")
df["date"] = pd.to_datetime(df["date"])

# 1. Fiyat
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["price"])
plt.title("Bitcoin Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("data/plot_price.png")
plt.close()

# 2. Google Trends
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["google_trends_score"])
plt.title("Google Trends Score Over Time")
plt.xlabel("Date")
plt.ylabel("Trend Score")
plt.tight_layout()
plt.savefig("data/plot_trends.png")
plt.close()

# 3. Scatter
plt.figure(figsize=(8, 5))
plt.scatter(df["google_trends_score"], df["daily_return"], alpha=0.5)
plt.title("Google Trends vs Daily Return")
plt.xlabel("Google Trends Score")
plt.ylabel("Daily Return")
plt.tight_layout()
plt.savefig("data/plot_trends_vs_return.png")
plt.close()

print("Plots saved.")