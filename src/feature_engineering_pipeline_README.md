# PIPELINE_README.md

## Feature Engineering Pipeline Overview

This module defines a robust, reproducible feature engineering pipeline for the Investment Attractiveness Classification project using scikit-learn's `Pipeline` and `ColumnTransformer`.

### Key Steps
- **Fit transformers only on training data** to prevent data leakage.
- **Numerical features:** KNN imputation (k=5) and standard scaling.
- **Categorical features:** Most frequent imputation and one-hot encoding (`handle_unknown='ignore'`).
- **ColumnTransformer** applies the correct steps to each feature type.
- **Assertions** ensure the same number of columns across train/val/test splits.
- **Raw data** is always kept untouched in `data/raw/`.

### Usage
1. Update `NUMERIC_FEATURES` and `CATEGORICAL_FEATURES` in `src/pipeline.py` with your selected columns.
2. Import and use the pipeline in your notebooks:
   ```python
   from src.pipeline import build_pipeline, fit_transform_pipeline, NUMERIC_FEATURES, CATEGORICAL_FEATURES
   pipe = build_pipeline(NUMERIC_FEATURES, CATEGORICAL_FEATURES)
   X_train_t, X_val_t, X_test_t = fit_transform_pipeline(pipe, X_train, X_val, X_test)
   ```
3. The pipeline ensures consistent, leakage-free preprocessing for all splits.

### Rationale
- **Reproducibility:** All steps are defined in code and can be reused.
- **Robustness:** Handles missing values and unknown categories gracefully.
- **Transparency:** Output shapes and assertions are logged for QA.

---

Commit this file and `src/pipeline.py` together to document and preserve your pipeline logic.
