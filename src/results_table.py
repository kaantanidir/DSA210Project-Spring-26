from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "outputs"
REPORT_DIR = ROOT / "reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

in_path = OUTPUT_DIR / "ml_results_summary.csv"
if not in_path.exists():
    raise FileNotFoundError("Run notebooks/ml_compare.py before generating the final results table.")

results = pd.read_csv(in_path)
results = results.sort_values(["f1", "accuracy"], ascending=False)
results.to_csv(OUTPUT_DIR / "ml_results_summary.csv", index=False)
with open(REPORT_DIR / "ml_results_summary.md", "w", encoding="utf-8") as f:
    f.write("# Machine Learning Results Summary\n\n")
    f.write(results.to_markdown(index=False))
    f.write("\n")

print(results)
print(f"Saved final ML results table to {OUTPUT_DIR / 'ml_results_summary.csv'}")
