import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/bitcoin_features.csv")

market_features = [
    "price",
    "market_cap",
    "total_volume",
    "daily_return",
    "volatility_7d",
    "price_change"
]

all_features = market_features + [
    "google_trends_score",
    "trends_change"
]

target = "target_up_next_day"

df = df.dropna(subset=all_features + [target])

split_index = int(len(df) * 0.8)
train_df = df.iloc[:split_index]
test_df = df.iloc[split_index:]

def evaluate(features, model, label):
    X_train = train_df[features]
    y_train = train_df[target]
    X_test = test_df[features]
    y_test = test_df[target]

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"{label}")
    print("Features:", features)
    print("Accuracy:", acc)
    print("-" * 50)

print("=== Logistic Regression ===")
evaluate(market_features, LogisticRegression(max_iter=1000), "Baseline")
evaluate(all_features, LogisticRegression(max_iter=1000), "With Trends")

print("=== Random Forest ===")
evaluate(market_features, RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42), "Baseline")
evaluate(all_features, RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42), "With Trends")