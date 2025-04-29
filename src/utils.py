# src/utils.py
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Dict, Any
from src.config import MODEL_FILE

def save_model(model, filepath: Union[str, Path] = MODEL_FILE):
    """Save a trained model to disk"""
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")

def load_model(filepath: Union[str, Path] = MODEL_FILE):
    """Load a trained model from disk"""
    return joblib.load(filepath)

def make_prediction(model, input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Make a prediction using the trained model"""
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    model= load_model()
    # Make prediction
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0]
    
    # Format the output
    result = {
        'prediction': 'Approved' if prediction == 'Y' else 'Rejected',
        'probability': float(prediction_proba[1]) if prediction == 'Y' else float(prediction_proba[0])
    }
    
    return result