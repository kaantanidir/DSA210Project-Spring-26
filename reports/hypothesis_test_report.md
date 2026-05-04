# Hypothesis Testing Report

| test                                                    | x                   | y             |    n |   pearson_corr |   pearson_p_value |   spearman_corr |   spearman_p_value |
|:--------------------------------------------------------|:--------------------|:--------------|-----:|---------------:|------------------:|----------------:|-------------------:|
| Attention vs same-day return                            | google_trends_score | daily_return  | 1829 |    -0.0824675  |      0.000414814  |     -0.0265882  |       0.25574      |
| Previous-day attention vs return                        | trends_lag_1        | daily_return  | 1829 |    -0.0759547  |      0.00115075   |     -0.026389   |       0.259321     |
| Previous-week attention vs return                       | trends_lag_7        | daily_return  | 1823 |    -0.02766    |      0.23784      |     -0.0402999  |       0.0853986    |
| Attention vs 7-day volatility                           | google_trends_score | volatility_7d | 1823 |     0.496597   |      4.00075e-114 |      0.492163   |       7.95833e-112 |
| Previous-week attention vs volatility                   | trends_lag_7        | volatility_7d | 1823 |     0.496117   |      7.1241e-114  |      0.462203   |       3.74631e-97  |
| Fear & Greed vs return                                  | fear_greed_value    | daily_return  | 1828 |     0.189373   |      3.21087e-16  |      0.17835    |       1.56861e-14  |
| Fear & Greed vs volatility                              | fear_greed_value    | volatility_7d | 1822 |    -0.228609   |      4.95275e-23  |     -0.16173    |       3.79973e-12  |
| Previous-day Fear & Greed vs return                     | fear_greed_lag_1    | daily_return  | 1828 |     0.00524708 |      0.822611     |     -0.00908343 |       0.697938     |
| Previous-week Fear & Greed vs return                    | fear_greed_lag_7    | daily_return  | 1822 |     0.00912112 |      0.697221     |      0.00357701 |       0.878729     |
| High vs low Google Trends days: daily return difference | high_trend_group    | daily_return  | 1829 |   nan          |    nan            |     -0.580209   |       0.561857     |

## Interpretation

The tests evaluate whether attention-related variables are associated with Bitcoin returns or volatility. The key distinction is between directional predictability and market turbulence: a weak relationship with returns but a stronger relationship with volatility would suggest that public attention reflects market stress rather than providing a stable trading signal.
