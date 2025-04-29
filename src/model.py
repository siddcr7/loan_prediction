# src/model.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from src.data_processing import create_preprocessing_pipeline

def build_model():
    """Build the machine learning pipeline with preprocessing and model"""
    preprocessor = create_preprocessing_pipeline()
    
    # Full pipeline with preprocessing and model
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model and return metrics"""
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    return {
        'accuracy': accuracy,
        'report': report,
        'confusion_matrix': conf_matrix
    }