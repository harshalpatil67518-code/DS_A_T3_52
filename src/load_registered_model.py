import os
import mlflow
import pandas as pd


# Connect to MLflow server
mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
)

# Registered model URI
model_uri = "models:/iris-classifier-prod/Staging"

print("Loading registered model...")
print("Model URI:", model_uri)

# Load model
model = mlflow.sklearn.load_model(model_uri)

print("\nModel loaded successfully!")
print("Model type:", type(model))

# Load test data
df = pd.read_csv("data/processed/iris_features.csv")

features = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "sepal_area",
    "petal_area",
    "sepal_to_petal_length_ratio"
]

X = df[features].copy()
X = X.fillna(X.median())

# Make predictions
predictions = model.predict(X.head(5))

print("\nPredictions for first 5 samples:")
print(predictions)