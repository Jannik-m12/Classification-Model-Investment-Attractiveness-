# Classification-Model-Investment-Attractiveness

# Sustainable Energy Investment Attractiveness Prediction

This repository contains a machine learning project aimed at predicting the investment attractiveness of countries for sustainable energy projects using historical data on energy, environment, and socioeconomic indicators.

## Project Overview

The transition to sustainable energy requires strategic investment. This project develops a classification model to identify countries likely to be attractive for sustainable energy investments based on a defined set of criteria related to market dynamics, macroeconomic stability, and structural energy needs.

## Methodology

1.  **Data Loading and Exploration**: Initial examination of the dataset (`global-data-on-sustainable-energy.csv`).
2.  **Target Variable Definition**: Defining 'Investment Attractiveness' based on specific thresholds for renewable capacity growth, GDP growth, and energy access/fossil fuel reliance. Clustering was also explored as an alternative labeling method.
3.  **Feature Engineering**: Creation of new features (e.g., rolling averages, CAGR) to capture trends and patterns.
4.  **Data Preprocessing**: Handling missing values through imputation and scaling features.
5.  **Data Splitting Strategies**: Comparison of random and time-based train-test splits, emphasizing the importance of time-aware evaluation for realistic forecasting.
6.  **Model Training and Evaluation**: Training and evaluation of classification models (Random Forest and Gradient Boosting) using metrics like Accuracy, Precision, Recall, F1-Score, and ROC AUC.
7.  **Feature Importance Analysis**: Identifying the most influential features in predicting investment attractiveness.
8.  **Label Comparison**: Visualizing the agreement and disagreement between rule-based and cluster-based labels.
9.  **Stakeholder Analysis**: Identifying key stakeholders and assessing the potential benefits and harms of the project, including risk scoring and visualization.
10. **Project Framing**: Documenting the problem statement, success metrics, data overview, model scope, ethics, compliance, and deployment context in a Problem Requirement Document (PRD) and related statements.
11. **Data Ingestion Script**: A basic Python script (`src/data_collection.py`) for data download (placeholder) and checksum generation.

## Data

The dataset used is "Global Data on Sustainable Energy" available on Kaggle: [https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy/data](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy/data).

## Results

The models, particularly when evaluated with a time-based split, show promising performance in predicting investment attractiveness. Key drivers identified include renewable capacity growth, GDP growth, and electricity access. The comparison of labeling methods highlights the potential for data-driven approaches to offer alternative perspectives.

## Repository Contents

*   `sustainable_energy_investment_notebook.ipynb`: The main Jupyter notebook containing the analysis pipeline.
*   `prd_template.md`: Problem Requirement Document.
*   `impact_statement.md`: Statement on project impact.
*   `dataset_decision_matrix.md`: Dataset decision matrix.
*   `dataset_alignment_statement.md`: Dataset alignment statement.
*   `src/data_collection.py`: Basic data ingestion script.
*   `global-data-on-sustainable-energy.csv`: The dataset file (assumed to be present or downloaded).

## Getting Started

1.  Clone this repository.
2.  Ensure you have the necessary Python libraries installed (see notebook imports).
3.  Place the `global-data-on-sustainable-energy.csv` file in the appropriate location (or modify the `data_collection.py` script to download it).
4.  Run the Jupyter notebook cells sequentially to reproduce the analysis.

## License

MIT

## Contact

Jannik Melcher
