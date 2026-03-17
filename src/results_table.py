from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Logistic Regression",
        "Random Forest",
        "Random Forest",
    ],
    "Feature Set": [
        "Baseline",
        "With Trends",
        "Baseline",
        "With Trends",
    ],
    "Accuracy": [
        0.48723404255319147,
        0.48723404255319147,
        0.5074468085106383,
        0.5085106382978724,
    ],
})

out_path = OUTPUT_DIR / "ml_results_summary.csv"
results.to_csv(out_path, index=False)
print(results)
print(f"Saved to {out_path}")
