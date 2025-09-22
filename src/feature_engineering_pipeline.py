"""
Feature Engineering Pipeline for Investment Attractiveness Classification

- Uses scikit-learn's Pipeline and ColumnTransformer
- Fit transformers only on training data
- Handles categorical and numerical features
- OneHotEncoder uses handle_unknown='ignore'
- Keeps raw data untouched in data/raw/
"""

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from typing import List, Tuple, Dict
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="feature_engineering.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Example: update these with your actual selected features
NUMERIC_FEATURES = [
    # 'feature1', 'feature2', ...
]
CATEGORICAL_FEATURES = [
    # 'cat_feature1', 'cat_feature2', ...
]

def build_pipeline(numeric_features: List[str], categorical_features: List[str]) -> Pipeline:
    """
    Build a scikit-learn pipeline for feature engineering.
    """
    logging.info("Building feature engineering pipeline.")
    numeric_transformer = Pipeline([
        ("imputer", KNNImputer(n_neighbors=5)),
        ("scaler", StandardScaler()),
    ])
    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse=False)),
    ])
    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ])
    pipe = Pipeline([
        ("preprocessor", preprocessor)
    ])
    logging.info(f"Pipeline built with {len(numeric_features)} numeric and {len(categorical_features)} categorical features.")
    return pipe

def fit_transform_pipeline(
    pipe: Pipeline, X_train: pd.DataFrame, X_val: pd.DataFrame, X_test: pd.DataFrame
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Fit pipeline on train, transform val and test. Log output shapes and assert column consistency.
    """
    logging.info("Fitting pipeline on training data.")
    X_train_t = pipe.fit_transform(X_train)
    logging.info(f"Transforming validation and test data.")
    X_val_t = pipe.transform(X_val)
    X_test_t = pipe.transform(X_test)
    logging.info(f"Output shapes - Train: {X_train_t.shape}, Val: {X_val_t.shape}, Test: {X_test_t.shape}")
    assert X_train_t.shape[1] == X_val_t.shape[1] == X_test_t.shape[1], "Mismatch in feature columns across splits!"
    logging.info("Assertion passed: Same number of columns across splits.")
    return X_train_t, X_val_t, X_test_t
