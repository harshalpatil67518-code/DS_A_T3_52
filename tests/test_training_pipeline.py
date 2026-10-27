from src.train import load_data, train_model, evaluate_model

def test_training_pipeline():
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    accuracy, report = evaluate_model(model, X_test, y_test)
    assert 0 <= accuracy <= 1
    assert report is not None
    assert len(model.predict(X_test)) == len(y_test)
