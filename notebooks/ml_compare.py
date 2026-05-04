from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.base import clone

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
OUTPUT_DIR = ROOT / "data" / "outputs"
REPORT_DIR = ROOT / "reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

in_path = PROCESSED_DIR / "bitcoin_features.csv"
df = pd.read_csv(in_path)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

target = "target_up_next_day"

market_features = [
    "return_lag_1", "return_lag_3", "return_lag_7",
    "log_return_lag_1", "volatility_7d_lag_1", "volatility_7d_lag_7",
    "volume_change_lag_1", "volume_change_lag_7",
    "price_to_ma7", "price_to_ma30",
]

trend_features = [
    "google_trends_score", "trends_change", "trends_pct_change",
    "trends_lag_1", "trends_lag_7", "trends_change_lag_1",
    "trends_rolling_mean_7d", "trends_rolling_std_7d",
]

sentiment_features = [
    "fear_greed_value", "fear_greed_change", "fear_greed_rolling_mean_7d",
    "fear_greed_rolling_std_7d", "fear_greed_lag_1", "fear_greed_lag_7",
    "fear_greed_change_lag_1",
]

news_features = [
    "news_count", "news_count_change", "news_count_rolling_mean_7d",
    "news_count_lag_1", "news_count_lag_7",
]


def available(features):
    cols = []
    for c in features:
        if c in df.columns and df[c].notna().any():
            cols.append(c)
    return cols

market_features = available(market_features)
trend_features = available(trend_features)
sentiment_features = available(sentiment_features)
news_features = available(news_features)

feature_sets = {
    "Market only": market_features,
    "Google Trends only": trend_features,
    "Market + Google Trends": market_features + trend_features,
}

if sentiment_features:
    feature_sets["Fear & Greed only"] = sentiment_features
    feature_sets["Market + Fear & Greed"] = market_features + sentiment_features
    feature_sets["Market + Google Trends + Fear & Greed"] = market_features + trend_features + sentiment_features

if news_features:
    feature_sets["Market + News"] = market_features + news_features
    feature_sets["Market + Google Trends + News"] = market_features + trend_features + news_features
    if sentiment_features:
        feature_sets["All enriched features"] = market_features + trend_features + sentiment_features + news_features

needed_cols = sorted(set(sum(feature_sets.values(), [])) | {target, "date"})
model_df = df[needed_cols].dropna(subset=[target]).copy()
# Drop rows where all non-target feature values are missing.
model_df = model_df.dropna(subset=sorted(set(sum(feature_sets.values(), []))), how="all")

split_index = int(len(model_df) * 0.8)
train_df = model_df.iloc[:split_index].copy()
test_df = model_df.iloc[split_index:].copy()

models = {
    "Majority Class Baseline": DummyClassifier(strategy="most_frequent"),
    "Logistic Regression": Pipeline([
        ("imputer", SimpleImputer(strategy="median", keep_empty_features=True)),
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=5000, class_weight="balanced")),
    ]),
    "Random Forest": Pipeline([
        ("imputer", SimpleImputer(strategy="median", keep_empty_features=True)),
        ("model", RandomForestClassifier(
            n_estimators=300,
            max_depth=6,
            min_samples_leaf=10,
            random_state=42,
            class_weight="balanced_subsample",
        )),
    ]),
}

rows = []
reports = []
best_rf = None
best_rf_features = None
best_rf_f1 = -np.inf

for feature_set_name, features in feature_sets.items():
    if not features:
        continue
    # Some engineered columns may be available overall but empty in the training period
    # after a temporal split. Remove those columns to keep imputers and feature
    # importance outputs aligned.
    features = [c for c in features if train_df[c].notna().any()]
    if not features:
        continue
    X_train = train_df[features]
    y_train = train_df[target].astype(int)
    X_test = test_df[features]
    y_test = test_df[target].astype(int)

    for model_name, base_model in models.items():
        if model_name == "Majority Class Baseline" and feature_set_name != "Market only":
            continue
        model = clone(base_model)
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X_test)[:, 1]
        else:
            proba = pred
        try:
            auc = roc_auc_score(y_test, proba)
        except ValueError:
            auc = np.nan
        metrics = {
            "model": model_name,
            "feature_set": feature_set_name,
            "n_features": len(features),
            "train_rows": len(train_df),
            "test_rows": len(test_df),
            "accuracy": accuracy_score(y_test, pred),
            "precision": precision_score(y_test, pred, zero_division=0),
            "recall": recall_score(y_test, pred, zero_division=0),
            "f1": f1_score(y_test, pred, zero_division=0),
            "roc_auc": auc,
        }
        rows.append(metrics)
        reports.append(
            f"## {model_name} — {feature_set_name}\n\n"
            f"Features: {', '.join(features)}\n\n"
            f"Confusion matrix:\n\n{confusion_matrix(y_test, pred)}\n\n"
            f"Classification report:\n\n{classification_report(y_test, pred, zero_division=0)}\n"
        )
        if model_name == "Random Forest" and metrics["f1"] > best_rf_f1:
            best_rf_f1 = metrics["f1"]
            best_rf = model
            best_rf_features = list(features)

results = pd.DataFrame(rows).sort_values(["f1", "accuracy"], ascending=False)
out_csv = OUTPUT_DIR / "ml_results_summary.csv"
results.to_csv(out_csv, index=False)

with open(REPORT_DIR / "ml_detailed_report.md", "w", encoding="utf-8") as f:
    f.write("# Machine Learning Detailed Report\n\n")
    f.write("Temporal split: first 80% of observations for training, last 20% for testing.\n\n")
    f.write(results.to_markdown(index=False))
    f.write("\n\n")
    f.write("\n---\n".join(reports))

# Plot comparison by F1-score and accuracy.
plot_df = results.copy()
plot_df["label"] = plot_df["model"] + "\n" + plot_df["feature_set"]
plt.figure(figsize=(13, 6))
plt.bar(plot_df["label"], plot_df["f1"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("F1-score")
plt.title("Model Comparison by F1-score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "model_f1_comparison.png")
plt.close()

plt.figure(figsize=(13, 6))
plt.bar(plot_df["label"], plot_df["accuracy"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("Accuracy")
plt.title("Model Comparison by Accuracy")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "model_accuracy_comparison.png")
plt.close()

# Feature importance for the strongest Random Forest specification.
if best_rf is not None and best_rf_features:
    rf = best_rf.named_steps["model"]
    # SimpleImputer may drop features that are entirely missing in the training split
    # in some scikit-learn versions. Align the importance vector defensively.
    n_importances = len(rf.feature_importances_)
    aligned_features = best_rf_features[:n_importances]
    importances = pd.DataFrame({
        "feature": aligned_features,
        "importance": rf.feature_importances_,
    }).sort_values("importance", ascending=False)
    importances.to_csv(OUTPUT_DIR / "random_forest_feature_importance.csv", index=False)
    top = importances.head(15).sort_values("importance")
    plt.figure(figsize=(9, 6))
    plt.barh(top["feature"], top["importance"])
    plt.xlabel("Importance")
    plt.title("Top Random Forest Feature Importances")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "random_forest_feature_importance.png")
    plt.close()

print(results)
print(f"Saved ML summary to {out_csv}")
