1. 1. Three classification models were trained and evaluated on the transformed sample data:
2. 2. - Logistic Regression: Accuracy = 0.7694, F1-score = 0.6278
3. 3. - Random Forest: Accuracy = 0.7750, F1-score = 0.6721
4. 4. - Gradient Boosting: Accuracy = 0.7694, F1-score = 0.6468
5. 5. Random Forest achieved the highest accuracy and F1-score.
6. 6. Model selection results saved to 'model_selection_results.json'.
7. 7. Next step: Train the final model (Random Forest) on the full 'train.csv' dataset using the same feature engineering pipeline, then predict on 'test.csv'.
