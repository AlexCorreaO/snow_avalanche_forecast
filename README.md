# Snow avalanche danger level forecast

Based on:

Pérez-Guillén, C., Techel, F., Hendrick, M., Volpi, M., van Herwijnen, A.,
Olevski, T., Obozinski, G., P ́erez-Cruz, F., and Schweizer, J.: Data-driven
automated predictions of the avalanche danger level for dry-snow conditions
in Switzerland, Nat. Hazards Earth Syst. Sci., 22, 2031–2056, https://nhess.copernicus.org/articles/22/2031/2022/, 2022.

Download RF1 and RF2 datasets from https://renkulab.io/gitlab/deapsnow/predictions_avalanche_danger-level_switzerland/-/tree/main/data

Main script:
(Run script and SHAP part run it in the console)
- get data
- data analysis
- feature selection
- split in train, validation and test
- train Random Forest (can choose xgboost, adaboost, svm, perceptron, decision tree or mlp network)
- predict on validation and on test
- show metrics on both
- show feature importance (from native RF option)
- show feature importanc/contribution with SHAP (this part is commented due to computational complexity)
