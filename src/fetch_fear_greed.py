"""Fetch historical Crypto Fear & Greed Index data from Alternative.me.

This script adds a stable third data source to the project. It downloads the
complete historical Fear & Greed Index with a single API request, converts the
Unix timestamps to daily dates, and saves a clean CSV that can be merged by
src/feature_engineering.py.

Output:
    data/outputs/fear_greed_index.csv

Expected columns:
    date, fear_greed_value, fear_greed_classification
"""

from __future__ import annotations

from pathlib import Path
import time
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "outputs"
RAW_DIR = ROOT / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
RAW_DIR.mkdir(parents=True, exist_ok=True)

API_URL = "https://api.alternative.me/fng/"
OUT_PATH = OUTPUT_DIR / "fear_greed_index.csv"
RAW_OUT_PATH = RAW_DIR / "fear_greed_index_raw.csv"


def fetch_fear_greed(limit: int = 0, max_retries: int = 3) -> pd.DataFrame:
    """Download historical Fear & Greed Index data.

    Alternative.me documents limit=0 as the option for all available data.
    The endpoint is intentionally used once rather than as many daily calls;
    this makes the enrichment more reproducible and less rate-limit prone than
    daily GDELT ArticleList requests.
    """
    params = {"limit": limit, "format": "json"}
    last_error: Exception | None = None

    for attempt in range(max_retries):
        try:
            response = requests.get(API_URL, params=params, timeout=30)
            response.raise_for_status()
            payload = response.json()
            if payload.get("metadata", {}).get("error"):
                raise RuntimeError(payload["metadata"]["error"])
            records = payload.get("data", [])
            if not records:
                raise RuntimeError("Alternative.me returned no Fear & Greed records.")
            df = pd.DataFrame(records)
            return df
        except Exception as exc:  # noqa: BLE001 - keep CLI robust for students
            last_error = exc
            wait_seconds = 5 * (attempt + 1)
            print(f"Fetch attempt {attempt + 1} failed: {exc}")
            if attempt < max_retries - 1:
                print(f"Waiting {wait_seconds} seconds before retrying...")
                time.sleep(wait_seconds)

    raise RuntimeError(f"Could not fetch Fear & Greed data: {last_error}")


def clean_fear_greed(df: pd.DataFrame) -> pd.DataFrame:
    required = {"value", "value_classification", "timestamp"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Fear & Greed response is missing required columns: {missing}")

    clean = df.copy()
    clean["fear_greed_value"] = pd.to_numeric(clean["value"], errors="coerce")
    clean["date"] = pd.to_datetime(clean["timestamp"].astype(int), unit="s").dt.date
    clean["date"] = pd.to_datetime(clean["date"])
    clean = clean.rename(columns={"value_classification": "fear_greed_classification"})
    clean = clean[["date", "fear_greed_value", "fear_greed_classification"]]
    clean = clean.dropna(subset=["date", "fear_greed_value"])
    clean = clean.drop_duplicates("date").sort_values("date").reset_index(drop=True)
    return clean


def main() -> None:
    raw = fetch_fear_greed(limit=0)
    raw.to_csv(RAW_OUT_PATH, index=False)
    clean = clean_fear_greed(raw)
    clean.to_csv(OUT_PATH, index=False)
    print(f"Saved raw Fear & Greed data to {RAW_OUT_PATH}")
    print(f"Saved clean Fear & Greed data to {OUT_PATH}")
    print(f"Rows: {len(clean)}")
    print(clean.tail())


if __name__ == "__main__":
    main()
