import pandas as pd
from src.pipeline.features import engineer_features


def test_engineer_features_adds_columns(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "features.csv"

    df = pd.DataFrame({
        "sepal length (cm)": [5.1],
        "sepal width (cm)": [3.5],
        "petal length (cm)": [1.4],
        "petal width (cm)": [0.2],
        "species": ["setosa"]
    })

    df.to_csv(input_file, index=False)

    engineer_features(str(input_file), str(output_file))

    result = pd.read_csv(output_file)

    assert "sepal_area" in result.columns
    assert "petal_area" in result.columns
    assert "petal_length_bin" in result.columns