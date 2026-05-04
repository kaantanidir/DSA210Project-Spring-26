# Machine Learning Detailed Report

Temporal split: first 80% of observations for training, last 20% for testing.

| model                   | feature_set                           |   n_features |   train_rows |   test_rows |   accuracy |   precision |   recall |       f1 |   roc_auc |
|:------------------------|:--------------------------------------|-------------:|-------------:|------------:|-----------:|------------:|---------:|---------:|----------:|
| Random Forest           | Google Trends only                    |            8 |         1464 |         366 |   0.5      |    0.495575 | 0.618785 | 0.550369 |  0.482276 |
| Random Forest           | Fear & Greed only                     |            7 |         1464 |         366 |   0.521858 |    0.514706 | 0.58011  | 0.545455 |  0.509183 |
| Random Forest           | Market + Google Trends                |           18 |         1464 |         366 |   0.538251 |    0.532258 | 0.546961 | 0.53951  |  0.528207 |
| Random Forest           | Market only                           |           10 |         1464 |         366 |   0.546448 |    0.543353 | 0.519337 | 0.531073 |  0.544662 |
| Logistic Regression     | Market only                           |           10 |         1464 |         366 |   0.497268 |    0.492891 | 0.574586 | 0.530612 |  0.503509 |
| Random Forest           | Market + Fear & Greed                 |           17 |         1464 |         366 |   0.538251 |    0.533708 | 0.524862 | 0.529248 |  0.540212 |
| Logistic Regression     | Market + Google Trends                |           18 |         1464 |         366 |   0.486339 |    0.483721 | 0.574586 | 0.525253 |  0.500433 |
| Random Forest           | Market + Google Trends + Fear & Greed |           25 |         1464 |         366 |   0.521858 |    0.516304 | 0.524862 | 0.520548 |  0.523996 |
| Logistic Regression     | Market + Fear & Greed                 |           17 |         1464 |         366 |   0.494536 |    0.49     | 0.541436 | 0.514436 |  0.488129 |
| Logistic Regression     | Fear & Greed only                     |            7 |         1464 |         366 |   0.491803 |    0.486486 | 0.497238 | 0.491803 |  0.489921 |
| Logistic Regression     | Google Trends only                    |            8 |         1464 |         366 |   0.459016 |    0.458937 | 0.524862 | 0.489691 |  0.458354 |
| Logistic Regression     | Market + Google Trends + Fear & Greed |           25 |         1464 |         366 |   0.467213 |    0.464646 | 0.508287 | 0.485488 |  0.482813 |
| Majority Class Baseline | Market only                           |           10 |         1464 |         366 |   0.505464 |    0        | 0        | 0        |  0.5      |

## Majority Class Baseline — Market only

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30

Confusion matrix:

[[185   0]
 [181   0]]

Classification report:

              precision    recall  f1-score   support

           0       0.51      1.00      0.67       185
           1       0.00      0.00      0.00       181

    accuracy                           0.51       366
   macro avg       0.25      0.50      0.34       366
weighted avg       0.26      0.51      0.34       366


---
## Logistic Regression — Market only

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30

Confusion matrix:

[[ 78 107]
 [ 77 104]]

Classification report:

              precision    recall  f1-score   support

           0       0.50      0.42      0.46       185
           1       0.49      0.57      0.53       181

    accuracy                           0.50       366
   macro avg       0.50      0.50      0.49       366
weighted avg       0.50      0.50      0.49       366


---
## Random Forest — Market only

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30

Confusion matrix:

[[106  79]
 [ 87  94]]

Classification report:

              precision    recall  f1-score   support

           0       0.55      0.57      0.56       185
           1       0.54      0.52      0.53       181

    accuracy                           0.55       366
   macro avg       0.55      0.55      0.55       366
weighted avg       0.55      0.55      0.55       366


---
## Logistic Regression — Google Trends only

Features: google_trends_score, trends_change, trends_pct_change, trends_lag_1, trends_lag_7, trends_change_lag_1, trends_rolling_mean_7d, trends_rolling_std_7d

Confusion matrix:

[[ 73 112]
 [ 86  95]]

Classification report:

              precision    recall  f1-score   support

           0       0.46      0.39      0.42       185
           1       0.46      0.52      0.49       181

    accuracy                           0.46       366
   macro avg       0.46      0.46      0.46       366
weighted avg       0.46      0.46      0.46       366


---
## Random Forest — Google Trends only

Features: google_trends_score, trends_change, trends_pct_change, trends_lag_1, trends_lag_7, trends_change_lag_1, trends_rolling_mean_7d, trends_rolling_std_7d

Confusion matrix:

[[ 71 114]
 [ 69 112]]

Classification report:

              precision    recall  f1-score   support

           0       0.51      0.38      0.44       185
           1       0.50      0.62      0.55       181

    accuracy                           0.50       366
   macro avg       0.50      0.50      0.49       366
weighted avg       0.50      0.50      0.49       366


---
## Logistic Regression — Market + Google Trends

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30, google_trends_score, trends_change, trends_pct_change, trends_lag_1, trends_lag_7, trends_change_lag_1, trends_rolling_mean_7d, trends_rolling_std_7d

Confusion matrix:

[[ 74 111]
 [ 77 104]]

Classification report:

              precision    recall  f1-score   support

           0       0.49      0.40      0.44       185
           1       0.48      0.57      0.53       181

    accuracy                           0.49       366
   macro avg       0.49      0.49      0.48       366
weighted avg       0.49      0.49      0.48       366


---
## Random Forest — Market + Google Trends

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30, google_trends_score, trends_change, trends_pct_change, trends_lag_1, trends_lag_7, trends_change_lag_1, trends_rolling_mean_7d, trends_rolling_std_7d

Confusion matrix:

[[98 87]
 [82 99]]

Classification report:

              precision    recall  f1-score   support

           0       0.54      0.53      0.54       185
           1       0.53      0.55      0.54       181

    accuracy                           0.54       366
   macro avg       0.54      0.54      0.54       366
weighted avg       0.54      0.54      0.54       366


---
## Logistic Regression — Fear & Greed only

Features: fear_greed_value, fear_greed_change, fear_greed_rolling_mean_7d, fear_greed_rolling_std_7d, fear_greed_lag_1, fear_greed_lag_7, fear_greed_change_lag_1

Confusion matrix:

[[90 95]
 [91 90]]

Classification report:

              precision    recall  f1-score   support

           0       0.50      0.49      0.49       185
           1       0.49      0.50      0.49       181

    accuracy                           0.49       366
   macro avg       0.49      0.49      0.49       366
weighted avg       0.49      0.49      0.49       366


---
## Random Forest — Fear & Greed only

Features: fear_greed_value, fear_greed_change, fear_greed_rolling_mean_7d, fear_greed_rolling_std_7d, fear_greed_lag_1, fear_greed_lag_7, fear_greed_change_lag_1

Confusion matrix:

[[ 86  99]
 [ 76 105]]

Classification report:

              precision    recall  f1-score   support

           0       0.53      0.46      0.50       185
           1       0.51      0.58      0.55       181

    accuracy                           0.52       366
   macro avg       0.52      0.52      0.52       366
weighted avg       0.52      0.52      0.52       366


---
## Logistic Regression — Market + Fear & Greed

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30, fear_greed_value, fear_greed_change, fear_greed_rolling_mean_7d, fear_greed_rolling_std_7d, fear_greed_lag_1, fear_greed_lag_7, fear_greed_change_lag_1

Confusion matrix:

[[ 83 102]
 [ 83  98]]

Classification report:

              precision    recall  f1-score   support

           0       0.50      0.45      0.47       185
           1       0.49      0.54      0.51       181

    accuracy                           0.49       366
   macro avg       0.49      0.50      0.49       366
weighted avg       0.50      0.49      0.49       366


---
## Random Forest — Market + Fear & Greed

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30, fear_greed_value, fear_greed_change, fear_greed_rolling_mean_7d, fear_greed_rolling_std_7d, fear_greed_lag_1, fear_greed_lag_7, fear_greed_change_lag_1

Confusion matrix:

[[102  83]
 [ 86  95]]

Classification report:

              precision    recall  f1-score   support

           0       0.54      0.55      0.55       185
           1       0.53      0.52      0.53       181

    accuracy                           0.54       366
   macro avg       0.54      0.54      0.54       366
weighted avg       0.54      0.54      0.54       366


---
## Logistic Regression — Market + Google Trends + Fear & Greed

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30, google_trends_score, trends_change, trends_pct_change, trends_lag_1, trends_lag_7, trends_change_lag_1, trends_rolling_mean_7d, trends_rolling_std_7d, fear_greed_value, fear_greed_change, fear_greed_rolling_mean_7d, fear_greed_rolling_std_7d, fear_greed_lag_1, fear_greed_lag_7, fear_greed_change_lag_1

Confusion matrix:

[[ 79 106]
 [ 89  92]]

Classification report:

              precision    recall  f1-score   support

           0       0.47      0.43      0.45       185
           1       0.46      0.51      0.49       181

    accuracy                           0.47       366
   macro avg       0.47      0.47      0.47       366
weighted avg       0.47      0.47      0.47       366


---
## Random Forest — Market + Google Trends + Fear & Greed

Features: return_lag_1, return_lag_3, return_lag_7, log_return_lag_1, volatility_7d_lag_1, volatility_7d_lag_7, volume_change_lag_1, volume_change_lag_7, price_to_ma7, price_to_ma30, google_trends_score, trends_change, trends_pct_change, trends_lag_1, trends_lag_7, trends_change_lag_1, trends_rolling_mean_7d, trends_rolling_std_7d, fear_greed_value, fear_greed_change, fear_greed_rolling_mean_7d, fear_greed_rolling_std_7d, fear_greed_lag_1, fear_greed_lag_7, fear_greed_change_lag_1

Confusion matrix:

[[96 89]
 [86 95]]

Classification report:

              precision    recall  f1-score   support

           0       0.53      0.52      0.52       185
           1       0.52      0.52      0.52       181

    accuracy                           0.52       366
   macro avg       0.52      0.52      0.52       366
weighted avg       0.52      0.52      0.52       366

