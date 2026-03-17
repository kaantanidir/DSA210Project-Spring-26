from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
OUTPUT_DIR = ROOT / "data" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(PROCESSED_DIR / "bitcoin_features.csv")
df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["price"])
plt.title("Bitcoin Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_price.png")
plt.close()

plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["google_trends_score"])
plt.title("Google Trends Score Over Time")
plt.xlabel("Date")
plt.ylabel("Trend Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_trends.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["google_trends_score"], df["daily_return"], alpha=0.5)
plt.title("Google Trends vs Daily Return")
plt.xlabel("Google Trends Score")
plt.ylabel("Daily Return")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_trends_vs_return.png")
plt.close()

print(f"Plots saved to {OUTPUT_DIR}")
