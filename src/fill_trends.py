from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
in_path = PROCESSED_DIR / "bitcoin_with_trends.csv"
out_path = PROCESSED_DIR / "bitcoin_with_trends_filled.csv"

df = pd.read_csv(in_path)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

df["google_trends_score"] = df["google_trends_score"].ffill().bfill()

df.to_csv(out_path, index=False)

print(df.head())
print(df.tail())
print(df.isna().sum())
print(f"Saved to {out_path}")
