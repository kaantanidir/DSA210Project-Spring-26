# DSA210 Project — Public Attention, Market Sentiment, and Short-Term Bitcoin Market Behavior

## Project Overview

This project investigates whether public attention and market sentiment indicators can help explain short-term Bitcoin market behavior.

The project combines historical Bitcoin market data, Google Trends search-interest data, and the Alternative.me Crypto Fear & Greed Index. The analysis evaluates whether attention- and sentiment-based variables improve next-day Bitcoin direction prediction and whether they are more strongly associated with Bitcoin volatility.

The main research question is:

**Can public attention and market sentiment indicators improve short-term Bitcoin direction prediction and help explain Bitcoin market volatility?**

The project follows the full data science pipeline: data collection, preprocessing, feature engineering, exploratory data analysis, hypothesis testing, machine learning, visualization, and interpretation.

---

## Motivation

Bitcoin is one of the most visible and volatile financial assets. Its price behavior may be influenced not only by market variables, but also by public attention and investor sentiment. Search behavior and market sentiment indices may therefore help explain periods of volatility, fear, greed, and market turbulence.

This project tests whether these external indicators provide useful information beyond standard market-based variables.

---

## Main Findings

The results suggest that predicting next-day Bitcoin direction remains difficult, even after adding public attention and sentiment-based variables.

### Statistical findings

The strongest statistical relationship was observed between Google Trends and 7-day Bitcoin volatility. This suggests that public search attention is more closely related to market turbulence than to next-day directional returns.

Fear & Greed Index provided an additional sentiment-based enrichment layer. However, lagged sentiment features did not show strong standalone predictive power for next-day Bitcoin direction.

### Machine learning findings

The machine learning models showed limited predictive performance for next-day Bitcoin direction. The best F1-scores were approximately in the 0.49–0.55 range, indicating that short-term Bitcoin direction remains difficult to classify reliably.

The final model comparison includes:

- market-only models,
- Google Trends-only models,
- Fear & Greed-only models,
- market + Google Trends models,
- market + Fear & Greed models,
- market + Google Trends + Fear & Greed models.

Detailed results are available in:

```text
data/outputs/ml_results_summary.csv
reports/ml_results_summary.md
reports/ml_detailed_report.md
```

### Interpretation

Overall, Google Trends and Fear & Greed Index appear more useful for understanding attention, sentiment, and volatility behavior than for producing strong next-day directional forecasts.

---

## Data Sources

### 1. CoinGecko

Used for:

- Bitcoin price,
- market capitalization,
- total trading volume.

The raw file is stored as:

```text
data/raw/btc-usd-max.csv
```

### 2. Google Trends

Used as a proxy for public attention toward Bitcoin.

The raw file is stored as:

```text
data/raw/google_trends_bitcoin.csv
```

Because the exported Google Trends data is weekly, the values are aligned with daily Bitcoin market observations and forward-filled within the available Google Trends period.

### 3. Alternative.me Crypto Fear & Greed Index

Used as a market sentiment indicator. The index provides a daily sentiment score between 0 and 100, where lower values indicate fear and higher values indicate greed.

The Fear & Greed data is downloaded using:

```text
src/fetch_fear_greed.py
```

and saved as:

```text
data/raw/fear_greed_index_raw.csv
data/outputs/fear_greed_index.csv
```

The original proposal focused on CoinGecko and Google Trends. After peer feedback and API reproducibility concerns with GDELT, the final project was extended with the Alternative.me Crypto Fear & Greed Index as a stable sentiment-based enrichment source.

---

## Data Analysis

The project includes the following stages:

1. **Market data preparation**  
   The raw CoinGecko data is cleaned and converted into a daily Bitcoin market dataset.

2. **Google Trends integration**  
   Weekly Google Trends values are merged with the daily Bitcoin market data.

3. **Trend value filling**  
   Google Trends values are forward-filled across daily observations within the valid Google Trends period.

4. **Fear & Greed data collection**  
   Daily Crypto Fear & Greed Index values are downloaded and cleaned.

5. **Feature engineering**  
   Market, attention, sentiment, lagged, rolling, and target variables are created.

6. **Exploratory data analysis**  
   Time-series plots, scatter plots, grouped comparisons, and correlation visualizations are generated.

7. **Hypothesis testing**  
   Statistical tests examine relationships between attention/sentiment indicators and Bitcoin returns or volatility.

8. **Machine learning modeling**  
   Logistic Regression and Random Forest models are compared using multiple feature sets.

9. **Result interpretation**  
   Model performance and statistical findings are interpreted in relation to the research question.

---

## Repository Structure

```text
DSA210Project-Spring-26/
│
├── data/
│   ├── raw/
│   │   ├── btc-usd-max.csv
│   │   ├── google_trends_bitcoin.csv
│   │   └── fear_greed_index_raw.csv
│   │
│   ├── processed/
│   │   ├── bitcoin_market_clean.csv
│   │   ├── bitcoin_with_trends.csv
│   │   ├── bitcoin_with_trends_filled.csv
│   │   └── bitcoin_features.csv
│   │
│   └── outputs/
│       ├── fear_greed_index.csv
│       ├── feature_summary.csv
│       ├── hypothesis_test_results.csv
│       ├── ml_results_summary.csv
│       ├── model_accuracy_comparison.png
│       ├── model_f1_comparison.png
│       ├── model_roc_auc_comparison.png
│       ├── plot_price.png
│       ├── plot_trends.png
│       ├── plot_trends_vs_return.png
│       ├── plot_trends_vs_volatility.png
│       ├── plot_fear_greed.png
│       ├── plot_fear_greed_vs_return.png
│       ├── plot_correlation_matrix.png
│       ├── random_forest_feature_importance.csv
│       └── random_forest_feature_importance.png
│
├── src/
│   ├── prepare_market_data.py
│   ├── merge_with_trends.py
│   ├── fill_trends.py
│   ├── fetch_fear_greed.py
│   ├── feature_engineering.py
│   ├── results_table.py
│   └── results_plot.py
│
├── notebooks/
│   ├── hypothesis_test.py
│   ├── plots.py
│   └── ml_compare.py
│
├── reports/
│   ├── DSA210_Bitcoin_Final_Report.docx
│   ├── DSA210_Project_Report.pdf
│   ├── hypothesis_test_report.md
│   ├── ml_detailed_report.md
│   └── ml_results_summary.md
│
├── AI_Usage_Disclosure.md
├── Project_proposal.pdf
├── README.md
└── requirements.txt
```

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

The project was developed in Python. All analysis scripts are located in `src/` and `notebooks/`.

---

## Reproducible Pipeline

Run the scripts in the following order:

```bash
python src/prepare_market_data.py
python src/merge_with_trends.py
python src/fill_trends.py
python src/fetch_fear_greed.py
python src/feature_engineering.py
python notebooks/hypothesis_test.py
python notebooks/plots.py
python notebooks/ml_compare.py
python src/results_table.py
python src/results_plot.py
```

The final processed datasets are saved under:

```text
data/processed/
```

The final tables, figures, and model outputs are saved under:

```text
data/outputs/
reports/
```

---

## Features Used in Modeling

### Market-based features

- price,
- market capitalization,
- total trading volume,
- daily return,
- log return,
- rolling volatility,
- moving averages,
- volume change,
- lagged return features.

### Public attention features

- Google Trends score,
- Google Trends change,
- lagged Google Trends variables,
- rolling Google Trends features.

### Sentiment features

- Fear & Greed Index value,
- Fear & Greed change,
- lagged Fear & Greed variables,
- rolling Fear & Greed features.

### Target variable

- `target_up_next_day`: binary target indicating whether Bitcoin price increased the following day.
- `target_high_volatility_next_7d`: binary target indicating whether the next 7-day volatility is high.

---

## Outputs

Key generated outputs include:

```text
data/processed/bitcoin_features.csv
data/outputs/hypothesis_test_results.csv
data/outputs/ml_results_summary.csv
data/outputs/model_accuracy_comparison.png
data/outputs/model_f1_comparison.png
data/outputs/model_roc_auc_comparison.png
data/outputs/random_forest_feature_importance.png
reports/hypothesis_test_report.md
reports/ml_detailed_report.md
reports/ml_results_summary.md
```

---

## Limitations

- Google Trends measures search attention, not actual investor intent.
- Fear & Greed Index is a market sentiment proxy, but it does not directly measure individual investor decisions.
- Google Trends data is weekly in the exported file and had to be aligned with daily market data.
- The models use historical features and cannot fully capture sudden news shocks or unexpected market events.
- Short-term Bitcoin direction is inherently noisy and difficult to predict.
- The current modeling setup uses relatively simple classifiers; more advanced time-aware models may improve robustness.

---

## Future Work

- Add stable news-intensity features from a reliable archived news dataset or API.
- Apply time-series cross-validation.
- Test additional time-aware models.
- Explore separate volatility prediction models.
- Compare attention and sentiment indicators across multiple cryptocurrencies.

---

## Response to Peer Feedback

Based on peer feedback, the project was strengthened in three main ways:

1. **Originality**  
   The project was reframed from a simple Bitcoin direction prediction task into a broader analysis of public attention, market sentiment, direction prediction, and volatility behavior.

2. **Dataset enrichment**  
   In addition to CoinGecko market data and Google Trends attention data, the final project adds the Alternative.me Crypto Fear & Greed Index as a third sentiment-based data source.

3. **Analytical interpretation**  
   Visualizations, hypothesis tests, and machine learning outputs were expanded to emphasize interpretation. The final analysis highlights that attention and sentiment variables are more informative for understanding volatility and market turbulence than for reliably predicting next-day direction.

---

## References

- **CoinGecko. Bitcoin historical market data.**  
  Bitcoin market data was downloaded from CoinGecko as a CSV file using the maximum available historical range. The raw file covers 2013-04-28 to 2026-03-17 and includes daily price, market capitalization, and total trading volume. The final analysis period begins later because the dataset is restricted to dates with available Google Trends data.  
  Source: https://www.coingecko.com/en/coins/bitcoin/historical_data

- **Google Trends. Search interest data for the keyword “Bitcoin”.**  
  Google Trends data was manually downloaded for the keyword “Bitcoin” and used as a proxy for public attention. Since the exported Google Trends data is weekly, it was forward-filled to align with daily Bitcoin market observations.  
  Source: https://trends.google.com/

- **Alternative.me. Crypto Fear & Greed Index.**  
  The Alternative.me Crypto Fear & Greed Index was used as a sentiment-based enrichment source. The data was downloaded through the public API using `src/fetch_fear_greed.py`.  
  Source: https://alternative.me/crypto/fear-and-greed-index/  
  API used in this project: https://api.alternative.me/fng/?limit=0&format=json
  
---

## AI Usage Disclosure

AI tools were used for documentation revision, coding support, debugging support, and repository organization. The final processed datasets, statistical test outputs, figures, and machine learning results were generated locally by running the project scripts. Full details are provided in:

```text
AI_Usage_Disclosure.md
```
