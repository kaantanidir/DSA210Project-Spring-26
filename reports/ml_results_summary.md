# Machine Learning Results Summary

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
