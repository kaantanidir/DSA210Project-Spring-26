from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr, ttest_ind

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
OUTPUT_DIR = ROOT / "data" / "outputs"
REPORT_DIR = ROOT / "reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

in_path = PROCESSED_DIR / "bitcoin_features.csv"
df = pd.read_csv(in_path)

pairs = [
    ("google_trends_score", "daily_return", "Attention vs same-day return"),
    ("trends_lag_1", "daily_return", "Previous-day attention vs return"),
    ("trends_lag_7", "daily_return", "Previous-week attention vs return"),
    ("google_trends_score", "volatility_7d", "Attention vs 7-day volatility"),
    ("trends_lag_7", "volatility_7d", "Previous-week attention vs volatility"),
]
if "fear_greed_value" in df.columns and df["fear_greed_value"].notna().any():
    pairs.extend([
        ("fear_greed_value", "daily_return", "Fear & Greed vs return"),
        ("fear_greed_value", "volatility_7d", "Fear & Greed vs volatility"),
        ("fear_greed_lag_1", "daily_return", "Previous-day Fear & Greed vs return"),
        ("fear_greed_lag_7", "daily_return", "Previous-week Fear & Greed vs return"),
    ])

if "news_count" in df.columns and df["news_count"].notna().any():
    pairs.extend([
        ("news_count", "daily_return", "News intensity vs return"),
        ("news_count", "volatility_7d", "News intensity vs volatility"),
        ("news_count_lag_1", "daily_return", "Previous-day news intensity vs return"),
    ])

rows = []
for x, y, label in pairs:
    sub = df[[x, y]].replace([np.inf, -np.inf], np.nan).dropna()
    if len(sub) < 5 or sub[x].nunique() < 2 or sub[y].nunique() < 2:
        continue
    pearson_corr, pearson_p = pearsonr(sub[x], sub[y])
    spearman_corr, spearman_p = spearmanr(sub[x], sub[y])
    rows.append({
        "test": label,
        "x": x,
        "y": y,
        "n": len(sub),
        "pearson_corr": pearson_corr,
        "pearson_p_value": pearson_p,
        "spearman_corr": spearman_corr,
        "spearman_p_value": spearman_p,
    })

# High vs low attention return test.
sub = df[["google_trends_score", "daily_return"]].dropna()
median_trend = sub["google_trends_score"].median()
high = sub[sub["google_trends_score"] >= median_trend]["daily_return"]
low = sub[sub["google_trends_score"] < median_trend]["daily_return"]
t_stat, p_val = ttest_ind(high, low, equal_var=False)
rows.append({
    "test": "High vs low Google Trends days: daily return difference",
    "x": "high_trend_group",
    "y": "daily_return",
    "n": len(sub),
    "pearson_corr": np.nan,
    "pearson_p_value": np.nan,
    "spearman_corr": t_stat,
    "spearman_p_value": p_val,
})

results = pd.DataFrame(rows)
results.to_csv(OUTPUT_DIR / "hypothesis_test_results.csv", index=False)

with open(REPORT_DIR / "hypothesis_test_report.md", "w", encoding="utf-8") as f:
    f.write("# Hypothesis Testing Report\n\n")
    f.write(results.to_markdown(index=False))
    f.write("\n\n")
    f.write("## Interpretation\n\n")
    f.write(
        "The tests evaluate whether attention-related variables are associated with Bitcoin returns or volatility. "
        "The key distinction is between directional predictability and market turbulence: a weak relationship with returns "
        "but a stronger relationship with volatility would suggest that public attention reflects market stress rather than "
        "providing a stable trading signal.\n"
    )

print(results)
print("Saved hypothesis test results and report.")
