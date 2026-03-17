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
        0.5095890410958904,
        0.5095890410958904,
        0.4904109589041096,
        0.4849315068493151,
    ],
})

out_path = OUTPUT_DIR / "ml_results_summary.csv"
results.to_csv(out_path, index=False)

print(results)
print(f"Saved to {out_path}")