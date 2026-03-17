import pandas as pd
import matplotlib.pyplot as plt

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Logistic Regression",
        "Random Forest",
        "Random Forest"
    ],
    "Feature Set": [
        "Baseline",
        "With Trends",
        "Baseline",
        "With Trends"
    ],
    "Accuracy": [
        0.48723404255319147,
        0.48723404255319147,
        0.5074468085106383,
        0.5085106382978724
    ]
})

labels = results["Model"] + " - " + results["Feature Set"]

plt.figure(figsize=(10, 5))
plt.bar(labels, results["Accuracy"])
plt.xticks(rotation=20)
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.tight_layout()
plt.savefig("data/model_accuracy_comparison.png")
plt.close()

print("Saved to data/model_accuracy_comparison.png")