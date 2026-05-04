from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "data" / "outputs"

ML_RESULTS_PATH = OUTPUT_DIR / "ml_results_summary.csv"


def save_horizontal_metric_plot(df, metric, output_name, title, xlabel):
    """
    Create a readable horizontal bar chart for a model evaluation metric.
    The plot is sorted from lowest to highest so that the best-performing
    model appears at the top.
    """
    plot_df = df.copy()
    plot_df["model_label"] = plot_df["model"] + " | " + plot_df["feature_set"]
    plot_df = plot_df.sort_values(metric, ascending=True)

    plt.figure(figsize=(12, 7))
    bars = plt.barh(plot_df["model_label"], plot_df[metric])

    for bar in bars:
        width = bar.get_width()
        plt.text(
            width + 0.005,
            bar.get_y() + bar.get_height() / 2,
            f"{width:.3f}",
            va="center",
            fontsize=9,
        )

    plt.xlabel(xlabel)
    plt.title(title)
    plt.xlim(0, max(0.60, plot_df[metric].max() + 0.06))
    plt.tight_layout()

    output_path = OUTPUT_DIR / output_name
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Saved {metric} plot to {output_path}")


def main():
    if not ML_RESULTS_PATH.exists():
        raise FileNotFoundError(
            f"ML results file not found: {ML_RESULTS_PATH}. "
            "Please run notebooks/ml_compare.py first."
        )

    df = pd.read_csv(ML_RESULTS_PATH)

    required_columns = {"model", "feature_set", "accuracy", "f1", "roc_auc"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns in ML results file: {missing}")

    save_horizontal_metric_plot(
        df=df,
        metric="accuracy",
        output_name="model_accuracy_comparison.png",
        title="Model Accuracy Comparison",
        xlabel="Accuracy",
    )

    save_horizontal_metric_plot(
        df=df,
        metric="f1",
        output_name="model_f1_comparison.png",
        title="Model F1-Score Comparison",
        xlabel="F1-score",
    )

    save_horizontal_metric_plot(
        df=df,
        metric="roc_auc",
        output_name="model_roc_auc_comparison.png",
        title="Model ROC-AUC Comparison",
        xlabel="ROC-AUC",
    )


if __name__ == "__main__":
    main()