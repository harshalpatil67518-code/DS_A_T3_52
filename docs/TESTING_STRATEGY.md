# Testing Strategy

## 1. Objective
The objective is to test the Iris machine learning project and check that its main functions work correctly.

## 2. Testing Tools
- Python
- pytest
- pytest-cov
- scikit-learn

## 3. Types of Testing
- Unit Testing: Tests individual functions.
- Integration Testing: Checks whether training and evaluation work together.
- Model Quality Testing: Checks whether model accuracy is at least 90%.
- Data Validation Testing: Checks valid data and rejects invalid species.

## 4. Test Files
- test_preprocess.py: Tests data preprocessing.
- test_features.py: Tests feature processing.
- test_validate.py: Tests data validation.
- test_training_pipeline.py: Tests the model training and evaluation pipeline.
- test_model_quality.py: Tests model accuracy.

## 5. Test Execution
Command: python -m pytest tests/ --cov=src --cov-report=term-missing --junitxml=test-results.xml

## 6. Test Results
- Total tests: 6
- Passed: 6
- Failed: 0
- Total source code coverage: 22%

## 7. Conclusion
All six tests passed successfully. The testing process checks preprocessing, feature processing, data validation, model training, and model quality.
