# DSA210 Project: Can Public Attention Help Predict Daily Bitcoin Direction?

This repository contains a data science project that investigates whether Bitcoin market data combined with Google Trends attention data can improve short-term price direction prediction.

## Project Question
Can public search interest in Bitcoin, measured using Google Trends, improve the prediction of next-day Bitcoin price direction beyond standard market-based variables?

## Current Status
The project currently includes:
- market data cleaning from CoinGecko-exported historical Bitcoin data
- Google Trends integration
- feature engineering for returns, volatility, and attention changes
- baseline machine learning models
- comparison of models with and without Google Trends features

## Data Sources
1. **CoinGecko historical export**  
   Provides Bitcoin price, market capitalization, and total trading volume.
2. **Google Trends**  
   Provides search-interest data for the keyword `Bitcoin` as a proxy for public attention.
3. **GDELT news data (optional / future work)**  
   Planned for richer sentiment-based features from news headlines.

## Repository Structure
```text
DSA210Project-Spring-26/
├── Data/                      # existing data folder in the public repo
├── data/                      # local working folder used during analysis
├── src/                       # Python scripts for preprocessing and modeling
├── README.md
└── requirements.txt
```

If you keep both `Data/` and `data/`, use one consistently in scripts to avoid path issues.

## Working Files Produced So Far
- `data/btc-usd-max.csv`
- `data/bitcoin_market_clean.csv`
- `data/google_trends_bitcoin.csv`
- `data/bitcoin_with_trends.csv`
- `data/bitcoin_with_trends_filled.csv`
- `data/bitcoin_features.csv`
- `data/ml_results_summary.csv` *(recommended to add)*

## Scripts Used So Far
- `src/prepare_market_data.py`
- `src/merge_with_trends.py`
- `src/fill_trends.py`
- `src/feature_engineering.py`
- `src/ml_model.py`
- `src/ml_compare.py`

## Setup
Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Order
1. Prepare market data:

```bash
python src/prepare_market_data.py
```

2. Export Google Trends CSV manually for the keyword `Bitcoin` and save it as:

```text
data/google_trends_bitcoin.csv
```

3. Merge market data with Google Trends:

```bash
python src/merge_with_trends.py
```

4. Fill missing trend values:

```bash
python src/fill_trends.py
```

5. Create model features:

```bash
python src/feature_engineering.py
```

6. Train initial models:

```bash
python src/ml_model.py
python src/ml_compare.py
```

## Features Used in Modeling
### Baseline market features
- `price`
- `market_cap`
- `total_volume`
- `daily_return`
- `volatility_7d`
- `price_change`

### Additional attention features
- `google_trends_score`
- `trends_change`

### Target
- `target_up_next_day`  
  Binary target indicating whether Bitcoin price increased the following day.

## Results So Far
### Logistic Regression
- Baseline accuracy: **0.4872**
- With Google Trends: **0.4872**

### Random Forest
- Baseline accuracy: **0.5074**
- With Google Trends: **0.5085**

## Interpretation
The addition of Google Trends features did **not** produce a meaningful improvement in next-day Bitcoin direction prediction. Logistic Regression showed no improvement, while Random Forest showed only a negligible increase in accuracy.

### Random Forest feature importance
The most important variables were market-based features such as:
- market capitalization
- recent return
- price change
- price
- volatility
- total volume

Google Trends variables contributed much less:
- `google_trends_score`: low contribution
- `trends_change`: very low contribution

## Main Conclusion
Public search attention alone does not appear to meaningfully improve short-term Bitcoin direction prediction in the current feature setup. Market-based variables remain substantially more informative than Google Trends variables.

## Limitations
- Google Trends data was weekly in the downloaded export and had to be aligned with higher-frequency market data.
- Only one external attention source was used in the current model.
- No rich text sentiment source has yet been integrated.
- Short-term Bitcoin direction is inherently noisy and difficult to predict.

## Recommended Next Steps
- Add GDELT-based news sentiment features
- Try lagged versions of Google Trends variables
- Test rolling averages of attention signals
- Evaluate regression on returns instead of only classification
- Add EDA and final notebook files to the repository

## Public Repo Gaps to Fill
The public repository currently shows `Data`, `README.md`, and `requirements.txt`. The following items should be added for completeness:
- `src/` scripts
- analysis notebooks
- cleaned output files or clear instructions to reproduce them
- finalized `requirements.txt`

## References
- CoinGecko historical market data documentation. citeturn470542view0
- Public GitHub repository contents showing current top-level files and README summary. citeturn470542view0turn855776view1
