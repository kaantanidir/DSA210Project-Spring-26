from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
OUTPUT_DIR = ROOT / "data" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(PROCESSED_DIR / "bitcoin_features.csv")
df["date"] = pd.to_datetime(df["date"])

# 1. Bitcoin price over time.
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["price"])
plt.title("Bitcoin Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_price.png")
plt.close()

# 2. Google Trends over time.
plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["google_trends_score"])
plt.title("Google Trends Score Over Time")
plt.xlabel("Date")
plt.ylabel("Google Trends Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_trends.png")
plt.close()

# 3. Google Trends vs daily return.
plt.figure(figsize=(8, 5))
plt.scatter(df["google_trends_score"], df["daily_return"], alpha=0.45)
plt.title("Google Trends vs Daily Return")
plt.xlabel("Google Trends Score")
plt.ylabel("Daily Return")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_trends_vs_return.png")
plt.close()

# 4. Google Trends vs volatility.
plt.figure(figsize=(8, 5))
plt.scatter(df["google_trends_score"], df["volatility_7d"], alpha=0.45)
plt.title("Google Trends vs 7-Day Volatility")
plt.xlabel("Google Trends Score")
plt.ylabel("7-Day Rolling Volatility")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_trends_vs_volatility.png")
plt.close()

# 5. Return distribution during low and high attention periods.
plot_df = df[["google_trends_score", "daily_return"]].dropna().copy()
plot_df["attention_group"] = np.where(
    plot_df["google_trends_score"] >= plot_df["google_trends_score"].median(),
    "High Trends", "Low Trends"
)
plt.figure(figsize=(7, 5))
plt.boxplot([
    plot_df.loc[plot_df["attention_group"] == "Low Trends", "daily_return"],
    plot_df.loc[plot_df["attention_group"] == "High Trends", "daily_return"],
], tick_labels=["Low Trends", "High Trends"], showfliers=False)
plt.ylabel("Daily Return")
plt.title("Daily Return Distribution by Attention Level")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_return_by_attention_group.png")
plt.close()

# 6. Fear & Greed sentiment over time.
if "fear_greed_value" in df.columns and df["fear_greed_value"].notna().any():
    plt.figure(figsize=(12, 5))
    plt.plot(df["date"], df["fear_greed_value"])
    plt.title("Crypto Fear & Greed Index Over Time")
    plt.xlabel("Date")
    plt.ylabel("Fear & Greed Index")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "plot_fear_greed.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.scatter(df["fear_greed_value"], df["daily_return"], alpha=0.45)
    plt.title("Fear & Greed Index vs Daily Return")
    plt.xlabel("Fear & Greed Index")
    plt.ylabel("Daily Return")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "plot_fear_greed_vs_return.png")
    plt.close()

# 7. Optional news plot. This appears only when valid non-missing GDELT values exist.
if "news_count" in df.columns and df["news_count"].notna().any():
    plt.figure(figsize=(12, 5))
    plt.plot(df["date"], df["news_count"])
    plt.title("Daily Bitcoin News Count from GDELT")
    plt.xlabel("Date")
    plt.ylabel("News Count")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "plot_news_count.png")
    plt.close()

# 8. Correlation matrix of selected analytical variables.
selected = [
    "daily_return", "volatility_7d", "volume_change",
    "google_trends_score", "trends_change",
    "fear_greed_value", "fear_greed_change",
    "return_lag_1", "trends_lag_1", "trends_lag_7", "fear_greed_lag_1", "fear_greed_lag_7",
]
if "news_count" in df.columns and df["news_count"].notna().any():
    selected += ["news_count", "news_count_lag_1"]
selected = [c for c in selected if c in df.columns and df[c].notna().any()]
corr = df[selected].corr()
plt.figure(figsize=(9, 7))
plt.imshow(corr, aspect="auto")
plt.colorbar(label="Correlation")
plt.xticks(range(len(selected)), selected, rotation=45, ha="right")
plt.yticks(range(len(selected)), selected)
plt.title("Correlation Matrix of Key Features")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "plot_correlation_matrix.png")
plt.close()

print(f"Plots saved to {OUTPUT_DIR}")
