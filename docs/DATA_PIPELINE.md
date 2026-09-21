# Data Pipeline Documentation

## Pipeline Stages

| Stage | Input | Output | Purpose |
|---|---|---|---|
| Collect | Iris dataset | data/raw/iris_raw.csv | Collect raw Iris data |
| Preprocess | Raw CSV | data/processed/iris_preprocessed.csv | Remove duplicates and handle missing values |
| Features | Preprocessed CSV | data/processed/iris_features.csv | Create additional features |
| Validate | Feature CSV | Validation result | Check data quality and value ranges |

## Pipeline Flow

Collect
   ↓
Preprocess
   ↓
Feature Engineering
   ↓
Validation

## DVC Automation

The complete pipeline is automated using DVC.

The command:

dvc repro

runs the required stages automatically based on dependencies and cached outputs.

If there are no changes, DVC skips the stages that are already up to date.