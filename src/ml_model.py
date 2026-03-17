import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Veriyi oku
df = pd.read_csv("data/bitcoin_features.csv")

# Gerekli kolonları seç
features = [
    "price",
    "market_cap",
    "total_volume",
    "daily_return",
    "volatility_7d",
    "google_trends_score",
    "trends_change",
    "price_change"
]

target = "target_up_next_day"

# Eksik verileri temizle
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# Train-test split
# shuffle=False kullanıyoruz çünkü bu bir zaman serisi benzeri veri
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# 1. Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

print("=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, y_pred_log))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_log))
print("Classification Report:")
print(classification_report(y_test, y_pred_log))

# 2. Random Forest
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42
)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

print("\n=== Random Forest ===")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))
print("Classification Report:")
print(classification_report(y_test, y_pred_rf))

# Feature importance
importances = pd.DataFrame({
    "feature": features,
    "importance": rf_model.feature_importances_
}).sort_values("importance", ascending=False)

print("\n=== Random Forest Feature Importances ===")
print(importances)