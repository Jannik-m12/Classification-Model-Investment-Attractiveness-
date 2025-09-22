# Feature Engineering Reflection

## Which engineered feature added the greatest predictive value, and why?
The feature with the greatest predictive value was the rolling mean of the target variable per country. This feature captured temporal trends and smoothed out short-term fluctuations, allowing the model to leverage historical context and country-specific patterns, which are highly relevant for investment attractiveness.

## What transformation had the most surprising impact?
The use of mutual information (MI) scores for feature selection was most surprising. Features with moderate correlation but high MI scores (e.g., certain interaction terms) proved more predictive than expected, highlighting the value of non-linear relationships in the data.

## Which step in your pipeline took the longest to debug, and what was the challenge?
The most time-consuming step was ensuring leakage-free imputation and feature engineering. The challenge was to apply imputation and scaling only on the training set, then transform validation/test sets without introducing information from the future or other splits. Debugging required careful pipeline design and validation of data flow.

## How will your feature engineering choices affect model interpretability?
By documenting all feature transformations and using tree-based models, interpretability is preserved. However, automated features and interaction terms can make interpretation less intuitive. Saving feature definitions and selection rationale helps maintain transparency for stakeholders.

## What would you do differently next time?
Next time, I would:
- Automate more of the feature selection and documentation process.
- Experiment with additional domain-driven features.
- Incorporate robust outlier handling earlier in the pipeline.
- Use SHAP or similar tools for deeper interpretability analysis.

---
This reflection summarizes key lessons and outcomes from the feature engineering process for the investment attractiveness classification project.
