
import os
import mlflow
from mlflow.tracking import MlflowClient

# Connect to MLflow server
mlflow.set_tracking_uri(
    os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
)

client = MlflowClient()

# Best model run ID
best_run_id = "8da63a9423a841899cf45b1dc66933b4"

# Registered model name
model_name = "iris-classifier-prod"

# Model URI
model_uri = f"runs:/{best_run_id}/model"

print("Registering model...")
print("Run ID:", best_run_id)
print("Model URI:", model_uri)

# Register the model
registered_model = mlflow.register_model(
    model_uri=model_uri,
    name=model_name
)

print("\nModel registered successfully!")
print("Model name:", registered_model.name)
print("Version:", registered_model.version)

# Move model to Staging
version = registered_model.version

client.transition_model_version_stage(
    name=model_name,
    version=version,
    stage="Staging"
)

print("\nModel moved to Staging successfully!")
print("Model:", model_name)
print("Version:", version)
print("Stage: Staging")

