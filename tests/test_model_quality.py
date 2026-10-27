from src.train import load_data, train_model, evaluate_model

def test_model_accuracy():
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    accuracy, report = evaluate_model(model, X_test, y_test)
    assert accuracy >= 0.90
    assert report is not None
