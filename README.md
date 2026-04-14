# DSA210 Project — Can Google Trends Help Predict Short-Term Bitcoin Direction?

## Project Overview
This project investigates whether online public attention, measured through Google Trends, can improve short-term Bitcoin price direction prediction.

The main research question is:

**Can Google Trends data meaningfully improve next-day Bitcoin up/down prediction compared with market-only models?**

The project combines historical Bitcoin market data with Google Trends search-interest data, performs preprocessing and feature engineering, and evaluates the relationship using exploratory data analysis, hypothesis testing, and machine learning models.

---

## Motivation
Bitcoin is one of the most attention-driven financial assets, and public interest often changes rapidly during volatile market periods. This project explores whether public attention, approximated by Google Trends search activity, carries predictive information about short-term Bitcoin market movements.

More specifically, the goal is to test whether adding Google Trends data to market-based variables improves next-day Bitcoin direction prediction.

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

This dataset was collected from CoinGecko historical export data and stored as:
- `data/raw/btc-usd-max.csv`

### 2. Google Trends
Used for:
- search interest for the keyword **Bitcoin**
- proxy for public attention

This dataset was collected from Google Trends weekly search-interest data and stored as:
- `data/raw/google_trends_bitcoin.csv`

### Data enrichment
In accordance with the course project requirement of enriching a public dataset with an additional data source, this project combines:
- **Bitcoin market data** from CoinGecko
- **public attention data** from Google Trends

This enrichment allows testing whether attention-based variables provide information beyond standard market indicators.

---

## Data Analysis
The project currently includes the following stages of analysis:

1. **Data collection and cleaning**  
   Historical Bitcoin market data and weekly Google Trends data were collected and cleaned.

2. **Data merging and preprocessing**  
   The two sources were merged on date, and weekly trend values were aligned with daily market observations.

3. **Feature engineering**  
   Features such as daily returns, rolling volatility, trend changes, and next-day direction labels were created.

4. **Exploratory data analysis (EDA)**  
   Time-series plots and descriptive exploration were used to inspect the relationship between attention and market behavior.

5. **Hypothesis testing**  
   Correlation analysis and statistical comparison between high-trend and low-trend periods were performed.

6. **Machine learning**  
   Logistic Regression and Random Forest classifiers were trained to predict next-day Bitcoin direction.

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
│   ├── results_table.py
│   └── results_plot.py
│
├── notebooks/
│   ├── eda.py
│   ├── hypothesis_test.py
│   ├── ml_model.py
│   ├── ml_compare.py
│   └── plots.py
│
├── Project_proposal.pdf
├── README.md
└── requirements.txt
```

---

## Pipeline

### 1. Prepare market data
Cleans the raw CoinGecko export and creates a daily Bitcoin market dataset.

```bash
python src/prepare_market_data.py
```

### 2. Merge Google Trends
Merges weekly Google Trends data into the cleaned Bitcoin market data.

```bash
python src/merge_with_trends.py
```

### 3. Fill Google Trends values
Keeps only the period where Google Trends data exists and forward-fills missing weekly values across daily observations.

```bash
python src/fill_trends.py
```

### 4. Feature engineering
Creates:
- daily return
- 7-day rolling volatility
- price change
- trends change
- next-day binary target

```bash
python src/feature_engineering.py
```

### 5. Exploratory analysis and visualization
```bash
python notebooks/eda.py
python notebooks/plots.py
python notebooks/hypothesis_test.py
```

### 6. Machine learning
Two classification models are used:
- Logistic Regression
- Random Forest

```bash
python notebooks/ml_model.py
python notebooks/ml_compare.py
```

### 7. Export summary results
```bash
python src/results_table.py
python src/results_plot.py
```

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run the pipeline in order:

```bash
python src/prepare_market_data.py
python src/merge_with_trends.py
python src/fill_trends.py
python src/feature_engineering.py
python notebooks/eda.py
python notebooks/plots.py
python notebooks/hypothesis_test.py
python notebooks/ml_model.py
python notebooks/ml_compare.py
python src/results_table.py
python src/results_plot.py
```

---

## Current Milestone Scope
For the current milestone, the repository includes:
- data collection
- data cleaning and preprocessing
- exploratory data analysis
- hypothesis testing
- initial machine learning evaluation

This is consistent with the course timeline for the milestone covering **data collection, EDA, and hypothesis testing**, while also documenting the ongoing machine learning stage already implemented in the repository.

---

## Current Interpretation
The results suggest that predicting next-day Bitcoin direction remains difficult. Market-based variables are more informative than Google Trends variables, and public search interest alone does not appear to provide useful predictive power for short-term price direction.

However, Google Trends does appear to be associated with increased market volatility, which may indicate that public attention is more reflective of market excitement or stress than of directional momentum.

---

## Limitations
- Google Trends measures attention, not true sentiment.
- The project currently uses Google Trends only; no news or social-media sentiment is included in the final modeling.
- Evaluation is based on a single train/test split.
- More advanced time-series validation could improve robustness.

---

## Future Work
- Add GDELT-based news features
- Add lagged versions of Google Trends variables
- Use time-series cross-validation
- Test additional models and evaluation metrics
- Add a summary notebook to the `notebooks/` folder

---

## References
- CoinGecko Bitcoin historical export
- Google Trends search interest data for the keyword **Bitcoin**

---

## AI Usage Disclosure
AI tools were used for limited writing assistance, wording refinement, and README organization. The project idea, coding decisions, analysis flow, and interpretation were carried out by the student. Any AI-assisted edits should be considered editorial support rather than replacement of the actual project work.
