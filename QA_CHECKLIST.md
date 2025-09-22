# QA_CHECKLIST.md

## Data Quality Checks
- [x] No missing values in final modeling datasets
- [x] No duplicated rows
- [x] All feature columns have correct types (numeric/categorical)
- [x] Target variable is correctly defined and aligned
- [x] No data leakage between train/val/test splits
- [x] Outliers handled or documented
- [x] Feature scaling applied only to training data

## Code & Modeling Checks
- [x] All preprocessing steps are reproducible
- [x] Pipelines are robust to missing/infinite values
- [x] Model evaluation uses only validation/test data
- [x] Random seeds set for reproducibility
- [x] All visualizations have clear titles and labels
- [x] Results are interpretable and documented

## Documentation
- [x] EDA report and reflection saved
- [x] Variable types documented
- [x] Preprocessing pipeline exported
- [x] All code cells commented

*Check off each item as you verify it in your workflow.*
