import pandas as pd
from src.pipeline.preprocess import preprocess

def test_removes_duplicates(tmp_path):
    source = tmp_path / "input.csv"
    output = tmp_path / "output.csv"

    df = pd.DataFrame({
        "sepal length (cm)": [5.1, 5.1],
        "sepal width (cm)": [3.5, 3.5],
        "petal length (cm)": [1.4, 1.4],
        "petal width (cm)": [0.2, 0.2],
        "species": ["setosa", "setosa"]
    })

    df.to_csv(source, index=False)
    result = preprocess(str(source), str(output))

    assert len(result) == 1