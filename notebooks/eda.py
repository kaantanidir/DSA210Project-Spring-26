from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
in_path = ROOT / "data" / "processed" / "bitcoin_with_trends.csv"

df = pd.read_csv(in_path)

print(df.head())
print(df.columns)
print(df.isna().sum())
print(df.describe())
