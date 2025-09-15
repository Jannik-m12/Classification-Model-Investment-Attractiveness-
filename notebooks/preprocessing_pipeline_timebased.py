import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
import joblib

# Load data
# df = pd.read_csv('../Data/Raw/global-data-on-sustainable-energy.csv')
# For pipeline export, you should fit only on training data (e.g. 2000-2014)
def create_preprocessing_pipeline(df, year_col='Year', entity_col='Entity', train_start=2000, train_end=2014):
    # Filter training data
    train_df = df[(df[year_col] >= train_start) & (df[year_col] <= train_end)].copy()

    # Drop target columns if present
    target_columns = ['Investment Attractiveness', 'Investment Attractiveness_clustered', 'Cluster']
    feature_cols = [col for col in train_df.columns if col not in target_columns + [year_col, entity_col]]

    # Replace inf/-inf with NaN
    for col in feature_cols:
        train_df[col] = train_df[col].replace([np.inf, -np.inf], np.nan)

    # KNN Imputation for columns with missing values
    cols_with_missing = train_df[feature_cols].isnull().sum()[train_df[feature_cols].isnull().sum() > 0].index.tolist()
    if cols_with_missing:
        knn_imputer = KNNImputer(n_neighbors=5)
        knn_imputer.fit(train_df[cols_with_missing])
    else:
        knn_imputer = None

    # StandardScaler for numeric columns
    scaler = StandardScaler()
    scaler.fit(train_df[feature_cols])

    # Save pipeline steps
    pipeline = {
        'feature_cols': feature_cols,
        'knn_imputer': knn_imputer,
        'knn_cols': cols_with_missing,
        'scaler': scaler
    }
    return pipeline

# Example usage:
# df = pd.read_csv('../Data/Raw/global-data-on-sustainable-energy.csv')
# pipeline = create_preprocessing_pipeline(df)
# joblib.dump(pipeline, 'preprocessing_pipeline_timebased.joblib')

# To transform new data:
def transform_with_pipeline(df, pipeline, year_col='Year', entity_col='Entity'):
    X = df[pipeline['feature_cols']].copy()
    # Replace inf/-inf with NaN
    for col in pipeline['feature_cols']:
        X[col] = X[col].replace([np.inf, -np.inf], np.nan)
    # Impute missing values
    if pipeline['knn_imputer'] and pipeline['knn_cols']:
        X[pipeline['knn_cols']] = pipeline['knn_imputer'].transform(X[pipeline['knn_cols']])
    # Scale features
    X[pipeline['feature_cols']] = pipeline['scaler'].transform(X[pipeline['feature_cols']])
    return X

print('Time-based preprocessing pipeline code created. Fit only on training data to avoid data leakage.')
