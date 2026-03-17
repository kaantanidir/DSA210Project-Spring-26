from pathlib import Path
import matplotlib.pyplot as plt
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

labels = results["Model"] + " - " + results["Feature Set"]

plt.figure(figsize=(10, 5))
plt.bar(labels, results["Accuracy"])
plt.xticks(rotation=20)
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.tight_layout()

out_path = OUTPUT_DIR / "model_accuracy_comparison.png"
plt.savefig(out_path)
plt.close()

print(f"Saved to {out_path}")