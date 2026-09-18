# DVC Workflow

## Remote Configuration

DVC remote is configured as myremote and uses local storage for DVC tracked data.

## DVC + Git Workflow

The workflow for dataset versioning is:

1. Add the dataset using:
   dvc add data/raw/iris_v1.csv

2. Track the generated DVC metadata file using Git:
   git add data/raw/iris_v1.csv.dvc

3. Commit the dataset version:
   git commit -m "data: track Iris dataset v1 with DVC"

4. Push DVC tracked data to the configured remote:
   dvc push

## Dataset Version Comparison

The dataset versions can be compared using:

dvc diff

## Dataset Version Switching

To restore a previous dataset version:

1. Checkout the required historical .dvc file using Git.
2. Run:
   dvc checkout

This restores the dataset corresponding to that DVC version.

## Reproducibility

DVC stores dataset metadata and hashes, while Git tracks the .dvc files. This allows different dataset versions to be restored and reproduced using Git and DVC.