from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
OUTPUT_DIR = ROOT / "data" / "outputs"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

in_path = PROCESSED_DIR / "bitcoin_with_trends_filled.csv"
out_path = PROCESSED_DIR / "bitcoin_features.csv"


def _first_existing(candidates: list[Path]) -> Path | None:
    for p in candidates:
        if p.exists():
            return p
    return None


def _optional_news_path() -> Path | None:
    return _first_existing([
        OUTPUT_DIR / "gdelt_bitcoin_daily.csv",
        ROOT / "data" / "raw" / "gdelt_bitcoin_daily.csv",
        PROCESSED_DIR / "gdelt_bitcoin_daily.csv",
    ])


def _optional_fear_greed_path() -> Path | None:
    return _first_existing([
        OUTPUT_DIR / "fear_greed_index.csv",
        ROOT / "data" / "raw" / "fear_greed_index.csv",
        PROCESSED_DIR / "fear_greed_index.csv",
    ])


df = pd.read_csv(in_path)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

# Optional dataset enrichment: GDELT daily Bitcoin news intensity.
# This source is intentionally optional. It is only merged if a valid file exists
# and contains at least one non-missing news_count value. This prevents an
# incomplete/rate-limited GDELT run from contaminating the final reproducible
# pipeline with empty news columns.
news_path = _optional_news_path()
valid_news_path = None
if news_path is not None:
    news = pd.read_csv(news_path)
    news["date"] = pd.to_datetime(news["date"])
    if "news_count" not in news.columns:
        raise ValueError(f"News file {news_path} must contain a 'news_count' column.")
    news = news[["date", "news_count"]].drop_duplicates("date")
    news["news_count"] = pd.to_numeric(news["news_count"], errors="coerce")
    if news["news_count"].notna().any():
        valid_news_path = news_path
        df = df.merge(news, on="date", how="left")
    else:
        df["news_count"] = np.nan
else:
    df["news_count"] = np.nan

# Third data source enrichment: Alternative.me Crypto Fear & Greed Index.
# This is used as a stable market-sentiment proxy. Unlike GDELT, it can be
# fetched with one historical API call and is therefore more reproducible.
fear_greed_path = _optional_fear_greed_path()
if fear_greed_path is not None:
    fg = pd.read_csv(fear_greed_path)
    fg["date"] = pd.to_datetime(fg["date"])
    if "fear_greed_value" not in fg.columns:
        raise ValueError(f"Fear & Greed file {fear_greed_path} must contain a 'fear_greed_value' column.")
    keep_cols = ["date", "fear_greed_value"]
    if "fear_greed_classification" in fg.columns:
        keep_cols.append("fear_greed_classification")
    fg = fg[keep_cols].drop_duplicates("date")
    df = df.merge(fg, on="date", how="left")
else:
    df["fear_greed_value"] = np.nan
    df["fear_greed_classification"] = np.nan

# Core market features.
df["daily_return"] = df["price"].pct_change()
df["log_return"] = np.log(df["price"] / df["price"].shift(1))
df["price_change"] = df["price"].diff()
df["volume_change"] = df["total_volume"].pct_change().replace([np.inf, -np.inf], np.nan)
df["volatility_7d"] = df["daily_return"].rolling(7).std()
df["volatility_14d"] = df["daily_return"].rolling(14).std()
df["ma_7"] = df["price"].rolling(7).mean()
df["ma_30"] = df["price"].rolling(30).mean()
df["price_to_ma7"] = df["price"] / df["ma_7"] - 1
df["price_to_ma30"] = df["price"] / df["ma_30"] - 1

# Attention features from Google Trends.
df["trends_change"] = df["google_trends_score"].diff()
df["trends_pct_change"] = df["google_trends_score"].pct_change().replace([np.inf, -np.inf], np.nan)
df["trends_rolling_mean_7d"] = df["google_trends_score"].rolling(7).mean()
df["trends_rolling_std_7d"] = df["google_trends_score"].rolling(7).std()

# Sentiment features from the Fear & Greed Index.
df["fear_greed_change"] = df["fear_greed_value"].diff()
df["fear_greed_rolling_mean_7d"] = df["fear_greed_value"].rolling(7).mean()
df["fear_greed_rolling_std_7d"] = df["fear_greed_value"].rolling(7).std()

# Lagged features reduce look-ahead bias and make the prediction task more realistic.
for lag in [1, 3, 7, 14]:
    df[f"return_lag_{lag}"] = df["daily_return"].shift(lag)
    df[f"log_return_lag_{lag}"] = df["log_return"].shift(lag)
    df[f"volume_change_lag_{lag}"] = df["volume_change"].shift(lag)
    df[f"volatility_7d_lag_{lag}"] = df["volatility_7d"].shift(lag)
    df[f"trends_lag_{lag}"] = df["google_trends_score"].shift(lag)
    df[f"trends_change_lag_{lag}"] = df["trends_change"].shift(lag)
    df[f"fear_greed_lag_{lag}"] = df["fear_greed_value"].shift(lag)
    df[f"fear_greed_change_lag_{lag}"] = df["fear_greed_change"].shift(lag)
    df[f"news_count_lag_{lag}"] = df["news_count"].shift(lag)

if df["news_count"].notna().any():
    df["news_count"] = df["news_count"].fillna(0)
    df["news_count_change"] = df["news_count"].diff()
    df["news_count_rolling_mean_7d"] = df["news_count"].rolling(7).mean()
else:
    df["news_count_change"] = np.nan
    df["news_count_rolling_mean_7d"] = np.nan

# Prediction targets.
df["target_up_next_day"] = (df["daily_return"].shift(-1) > 0).astype(int)
df["target_high_volatility_next_7d"] = (
    df["volatility_7d"].shift(-1) > df["volatility_7d"].median()
).astype(int)

# Last row has no true next-day information, so keep it in the CSV but it will be
# dropped by modeling scripts when target/features are missing.
df.to_csv(out_path, index=False)

summary = df.describe(include="all")
summary.to_csv(OUTPUT_DIR / "feature_summary.csv")

print(f"Saved enhanced feature dataset to {out_path}")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print("Optional valid GDELT news file:", valid_news_path if valid_news_path is not None else "not used; news features left as missing")
print("Fear & Greed sentiment file:", fear_greed_path if fear_greed_path is not None else "not found; sentiment features left as missing")
print(df.tail(3))
