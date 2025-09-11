---
# Course: Classification
# Milestone: 1
# Stage: Idea only
# Title: Predicting Investment Attractiveness in Sustainable Energy


## 🧱 PRD Sections at the “Idea Only” Stage

### 🧩 Problem Statement

The decision being automated is whether a country is attractive for investing in renewable energy projects. The unit of prediction is "investment attractiveness" for a country in a given year. The outcome event being forecasted is a country being classified as "attractive" based on defined criteria (renewable energy capacity growth > 10%, GDP growth >= 2%, and either < 95% electricity access or > 50% fossil fuel share). The prediction horizon is typically 1 to 5 years into the future from the latest data used for training.

### 📈 Success Metrics

We aim to accurately identify countries that are attractive for sustainable energy investment to guide resource allocation.

| Metric         | Baseline Target | Aspirational Target |
| :------------- | :-------------- | :------------------ |
| Accuracy       | 0.70            | 0.90                |
| Precision (of predicting attractive) | 0.60            | 0.85                |
| Recall (of predicting attractive) | 0.60            | 0.85                |
| ROC AUC        | 0.75            | 0.95                |

*(Note: Baselines are initial estimates; these will be replaced with data-driven metrics in Milestone 3)*

### 👥 Stakeholders & Impact

Investing in sustainable energy has varied impacts. Direct beneficiaries include investors and project developers through financial returns, and host governments through economic development. Local communities may see benefits from improved infrastructure and job creation, but also potential harms like land displacement. Indirect benefits extend to citizens globally through a cleaner environment. A key indirect harm is to fossil fuel industry workers facing job losses. The environment itself is a major beneficiary if projects are successful, but faces risks if not executed sustainably.

### 🗃️ Data Overview

The primary anticipated data source is historical country-level data on energy, environment, and socioeconomic indicators (e.g., from World Bank, IEA, IRENA).
- **Volume:** Moderate (country-year observations over two decades, ~3600 rows).
- **Variety:** High (numerical indicators, geographical data, country/year identifiers).
- **Velocity:** Low (annual data updates).
- **Veracity:** Medium to High (official statistics, but potential for inconsistencies or reporting gaps).
- **Value:** High (essential for identifying drivers of investment attractiveness).
Uncertainties include data completeness and consistency across all countries and years.

### 🧠 Model Scope

**Baseline Model:** Logistic Regression - A simple, interpretable model to provide a performance benchmark.
**Stretch Model:** Gradient Boosting Classifier (e.g., LightGBM or XGBoost) - Expected to capture complex non-linear relationships and interactions for higher predictive performance.

### ⚖️ Ethics & Compliance

Sensitive attributes are not directly involved as the data is aggregated at the country level and does not contain personal information. The primary ethical consideration is ensuring fairness in predictions across different country income levels or regions, and transparency in how "attractiveness" is defined and predicted. Based on the EU AI Act, this system would likely fall under **low-risk AI systems** as it provides recommendations for investment and does not directly impact fundamental rights or safety.

### 🚀 Deployment Context

The model will likely operate in a **batch processing** mode, generating predictions annually or quarterly. Latency is not a critical concern; predictions do not need to be real-time. Predictions could be **human-reviewed** by investment analysts or policymakers before informing final decisions, allowing for expert judgment to complement the model's output.
