# DSA210Project-Spring-26: Can Online Sentiment Predict Daily Bitcoin Returns?

This repository contains the term project for the DSA 210: Introduction to Data Science course at Sabancı University. 

## Motivation
Cryptocurrency markets are highly volatile, operate 24/7, and are heavily influenced by public perception. This project investigates whether public attention and online sentiment (from news headlines and social media) can explain or predict short-term price movements and the volatility of Bitcoin.

## Data Sources
To create a comprehensive dataset, this project enriches historical market data with alternative data sources:
1. **CoinGecko API:** Historical Bitcoin data including daily price, market capitalization, and trading volume.
2. **GDELT DOC 2.0 API:** Global news articles and headlines related to Bitcoin to derive daily sentiment scores.
3. **Google Trends:** Search interest data to approximate public attention and hype.

## Repository Structure
- `data/`: Contains raw and cleaned datasets (e.g., `btc-usd-max.csv`, `bitcoin_market_clean.csv`).
- `requirements.txt`: List of Python dependencies required to run the project.
- `README.md`: Project overview and instructions.
*(Note: Jupyter notebooks for EDA, hypothesis testing, and Machine Learning will be added in future commits according to the project timeline).*

## How to Run
1. Clone this repository to your local machine.
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
