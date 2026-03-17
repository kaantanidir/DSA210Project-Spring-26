from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
in_path = PROCESSED_DIR / "bitcoin_with_trends_filled.csv"
out_path = PROCESSED_DIR / "bitcoin_features.csv"

df = pd.read_csv(in_path)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

df["daily_return"] = df["price"].pct_change()
df["volatility_7d"] = df["daily_return"].rolling(7).std()
df["trends_change"] = df["google_trends_score"].diff()
df["price_change"] = df["price"].diff()
df["target_up_next_day"] = (df["daily_return"].shift(-1) > 0).astype(int)

df.to_csv(out_path, index=False)

print(df.head(10))
print(df[["daily_return", "volatility_7d", "google_trends_score", "trends_change"]].describe())
print(f"Saved to {out_path}")
