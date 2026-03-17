"""Merge cleaned market data with a manually exported Google Trends CSV.
Expected Google Trends CSV columns can vary. This script normalizes common formats.
"""
from __future__ import annotations
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
market_path = ROOT / 'data' / 'bitcoin_market_clean.csv'
trends_path = ROOT / 'data' / 'google_trends_bitcoin.csv'
out_path = ROOT / 'data' / 'bitcoin_project_dataset.csv'

market = pd.read_csv(market_path)
market['date'] = pd.to_datetime(market['date'])

trends = pd.read_csv(trends_path)
# Try to normalize Google Trends export
first_col = trends.columns[0]
score_col = trends.columns[1]
trends = trends.rename(columns={first_col: 'date', score_col: 'google_trends_score'})
trends['date'] = pd.to_datetime(trends['date'], errors='coerce')
trends['google_trends_score'] = pd.to_numeric(trends['google_trends_score'], errors='coerce')

merged = market.merge(trends[['date', 'google_trends_score']], on='date', how='left')
merged.to_csv(out_path, index=False)
print(f'Saved merged dataset to {out_path}')
print(merged.head())
