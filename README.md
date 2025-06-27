# Predictive Privacy

This repository contains code and data to implement the _Predictive Privacy_ experiment, an end-to-end framework for quantifying informational privacy harm. Our approach combines synthetic data generation, unsupervised clustering, human harm scoring via surveys, and supervised machine learning to predict perceived privacy harm under different disclosure scenarios.

---

## Table of Contents

- [Background](#background)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Workflow](#workflow)
  - [1. Synthetic Data Generation](#1-synthetic-data-generation)
  - [2. Clustering](#2-clustering)
  - [3. Survey Generation & Scoring](#3-survey-generation--scoring)
  - [4. Model Training](#4-model-training)
- [License](#license)

---

## Background

With the rise of data-driven apps that collect and share personal information across corporations, data brokers, and governments, understanding and measuring privacy harm has become critical. _Predictive Privacy_ seeks to create a standardized, objective metric for informational privacy harm, enabling regulators and courts to assess actual injury beyond speculative or legal-only injuries.

This experiment pipeline:
1. Generates realistic synthetic individuals with sensitive attributes (using differential privacy).
2. Clusters these individuals to identify archetypes/patterns.
3. Deploys surveys (via Prolific.com) to collect human harm ratings for disclosure scenarios at varying accuracy levels.
4. Trains a supervised machine-learning model to predict harm scores for new profiles.

---

## Repository Structure

```text
├── analysis/                  # Auxiliary analysis scripts
├── data/                      # Raw and processed data files
├── Clustering.ipynb           # Notebook to preprocess data and perform clustering
├── SyntheticData.ipynb        # Notebook to synthesize privacy‑preserving data
├── Survey_Generation.ipynb    # Notebook to prepare and export survey questions
├── prob_left_join.py          # Utility script for joining probabilistic datasets
└── README.md                  # This file
```

---

## Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Key Python libraries:
  - `pandas`, `numpy`, `scikit-learn`, `scipy`
  - `matplotlib`, `seaborn` (for plotting)
  - `requests` (for survey API interaction)

---

## Workflow

### 1. Synthetic Data Generation

Notebook: `SyntheticData.ipynb`

- **Purpose**: Generate a synthetic dataset of individuals with sensitive attributes using differential privacy techniques.
- **Steps**:
  1. Download Pew Research dataset: https://www.pewresearch.org/methods/2018/01/26/appendix-b-synthetic-population-dataset/
  2. Upload to our synthetic data notebook and run the notebook to add additional attributes.

### 2. Clustering

Notebook: `Clustering.ipynb`

- **Purpose**: Identify clusters of similar individuals based on their sensitive-attribute profiles.
- **Steps**:
  1. Load the synthetic dataset.
  2. Perform standard preprocessing (scaling, encoding).
  3. Run clustering algorithms (e.g., K‑Means, hierarchical clustering).
  4. Analyze cluster characteristics and export `data/clustered_profiles.csv`.

### 3. Survey Generation & Scoring

Notebook: `Survey_Generation.ipynb`

- **Purpose**: Prepare survey questionnaires and collect harm ratings from human participants.
- **Steps**:
  1. Sample representative individuals from each cluster.
  2. Generate survey items describing disclosure scenarios at 100%, 75%, and 50% data accuracy.
  3. Format and export surveys (e.g., CSV, Qualtrics API payload).
  4. After data collection, ingest responses to produce `data/harm_scores.csv`.

### 4. Model Training

Script / Notebook: TBD

- **Purpose**: Train a supervised model to predict harm scores based on profile features and scenario accuracy.
- **Steps**:
  1. Load `clustered_profiles.csv` and `harm_scores.csv`.
  2. Merge datasets using `prob_left_join.py` for probabilistic joins.
  3. Split into training and testing sets.
  4. Train regression models (e.g., Random Forest, XGBoost).
  5. Evaluate performance (MAE, RMSE) and export the trained model.

---

## License

This project is licensed under the [MIT License](LICENSE).
