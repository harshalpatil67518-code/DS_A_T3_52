import pandas as pd
import pytest
from src.pipeline.validate import validate, DataValidationError

def test_valid_data_passes(tmp_path):
    file = tmp_path / "valid.csv"
    df = pd.DataFrame({
        "sepal length (cm)": [5.1],
        "sepal width (cm)": [3.5],
        "petal length (cm)": [1.4],
        "petal width (cm)": [0.2],
        "species": ["setosa"],
        "sepal_area": [17.85],
        "petal_area": [0.28],
        "sepal_to_petal_length_ratio": [3.64],
        "petal_length_bin": ["short"]
    })
    df.to_csv(file, index=False)
    assert len(validate(str(file))) == 1

def test_invalid_species_fails(tmp_path):
    file = tmp_path / "invalid.csv"
    df = pd.DataFrame({
        "sepal length (cm)": [5.1],
        "sepal width (cm)": [3.5],
        "petal length (cm)": [1.4],
        "petal width (cm)": [0.2],
        "species": ["unknown"],
        "sepal_area": [17.85],
        "petal_area": [0.28],
        "sepal_to_petal_length_ratio": [3.64],
        "petal_length_bin": ["short"]
    })
    df.to_csv(file, index=False)
    with pytest.raises(DataValidationError):
        validate(str(file))
