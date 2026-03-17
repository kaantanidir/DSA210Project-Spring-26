# DSA210 Project — Can Google Trends Help Predict Short-Term Bitcoin Direction?

## Project Overview
This project investigates whether online public attention, measured through Google Trends, can improve short-term Bitcoin price direction prediction.

The main research question is:

**Can Google Trends data meaningfully improve next-day Bitcoin up/down prediction compared with market-only models?**

The project combines historical Bitcoin market data with Google Trends search-interest data, performs preprocessing and feature engineering, and evaluates the relationship using statistical analysis and machine learning models.

---

## Main Findings
The current results suggest that **Google Trends variables do not meaningfully improve next-day Bitcoin direction prediction**.

### Statistical findings
- Correlation between `google_trends_score` and `daily_return`: **-0.0813**  
  - p-value: **0.0005**
- Correlation between `google_trends_score` and `volatility_7d`: **0.4966**  
  - p-value: **< 0.001**
- Difference in daily return between high-trend and low-trend days:
  - t-statistic: **-0.5404**
  - p-value: **0.5890**

### Machine learning findings
| Model | Feature Set | Accuracy |
|---|---|---:|
| Logistic Regression | Baseline (market only) | 0.5096 |
| Logistic Regression | With Google Trends | 0.5096 |
| Random Forest | Baseline (market only) | 0.4904 |
| Random Forest | With Google Trends | 0.4849 |

### Interpretation
- Google Trends had a **weak negative association** with daily returns.
- Google Trends had a **moderate positive association** with volatility.
- Adding Google Trends variables did **not improve** prediction accuracy.
- In Random Forest, adding Google Trends slightly **reduced** performance.

These findings suggest that Google Trends may be more closely related to **attention and market turbulence** than to **short-term directional returns**.

---

## Data Sources

### 1. CoinGecko
Used for:
- Bitcoin price
- market capitalization
- total trading volume

### 2. Google Trends
Used for:
- search interest for the keyword **Bitcoin**
- proxy for public attention

---

## Repository Structure

```text
DSA210Project-Spring-26/
│
├── data/
│   ├── raw/
│   │   ├── btc-usd-max.csv
│   │   └── google_trends_bitcoin.csv
│   │
│   ├── processed/
│   │   ├── bitcoin_market_clean.csv
│   │   ├── bitcoin_with_trends.csv
│   │   ├── bitcoin_with_trends_filled.csv
│   │   └── bitcoin_features.csv
│   │
│   └── outputs/
│       ├── ml_results_summary.csv
│       ├── model_accuracy_comparison.png
│       ├── plot_price.png
│       ├── plot_trends.png
│       └── plot_trends_vs_return.png
│
├── src/
│   ├── prepare_market_data.py
│   ├── merge_with_trends.py
│   ├── fill_trends.py
│   ├── feature_engineering.py
│   ├── eda.py
│   ├── plots.py
│   ├── hypothesis_test.py
│   ├── ml_model.py
│   ├── ml_compare.py
│   ├── results_table.py
│   └── results_plot.py
│
├── notebooks/
├── README.md
└── requirements.txt
