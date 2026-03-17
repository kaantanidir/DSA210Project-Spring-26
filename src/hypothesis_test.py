from pathlib import Path
import pandas as pd
from scipy.stats import pearsonr, ttest_ind

ROOT = Path(__file__).resolve().parents[1]
in_path = ROOT / "data" / "processed" / "bitcoin_features.csv"

df = pd.read_csv(in_path)
df = df.dropna(subset=["google_trends_score", "daily_return", "volatility_7d"])

corr_ret, p_ret = pearsonr(df["google_trends_score"], df["daily_return"])
corr_vol, p_vol = pearsonr(df["google_trends_score"], df["volatility_7d"])

print("Correlation with daily return:", corr_ret, "p-value:", p_ret)
print("Correlation with volatility_7d:", corr_vol, "p-value:", p_vol)

median_trend = df["google_trends_score"].median()
high = df[df["google_trends_score"] >= median_trend]["daily_return"].dropna()
low = df[df["google_trends_score"] < median_trend]["daily_return"].dropna()

t_stat, p_val = ttest_ind(high, low, equal_var=False)
print("T-test high vs low trends daily return")
print("t-stat:", t_stat, "p-value:", p_val)
