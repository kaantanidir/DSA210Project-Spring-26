from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

market_path = PROCESSED_DIR / "bitcoin_market_clean.csv"
trends_path = RAW_DIR / "google_trends_bitcoin.csv"
out_path = PROCESSED_DIR / "bitcoin_with_trends.csv"

market = pd.read_csv(market_path)
trends = pd.read_csv(trends_path, skiprows=2)

print("Trends columns:", trends.columns.tolist())
print(trends.head())

if len(trends.columns) < 2:
    raise ValueError(f"Google Trends file is not in the expected format. Columns: {trends.columns.tolist()}")

date_col = trends.columns[0]
score_col = trends.columns[1]

trends = trends.rename(columns={date_col: "date", score_col: "google_trends_score"})

market["date"] = pd.to_datetime(market["date"]).dt.date
trends["date"] = pd.to_datetime(trends["date"]).dt.date

merged = market.merge(trends, on="date", how="left")
merged.to_csv(out_path, index=False)

print(merged.head())
print(merged.tail())
print(f"Saved to {out_path}")
