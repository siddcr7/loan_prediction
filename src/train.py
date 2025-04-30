# src/train.py
import argparse
import pandas as pd
from pathlib import Path
import mlflow

from src.config import DATA_FILE, MODEL_FILE
from src.data_processing import load_data, preprocess_data, split_train_test
from src.model import build_model, evaluate_model
from src.utils import save_model

def train():
    """Train the model and save it"""
    print("Loading data...")
    df = load_data(DATA_FILE)
    
    print("Preprocessing data...")
    data = preprocess_data(df)
    
    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = split_train_test(data)
    with mlflow.start_run():
        mlflow.log_param("data_file", DATA_FILE)
        mlflow.log_param("model_file", MODEL_FILE)
        mlflow.log_param("train_size", len(X_train))
        mlflow.log_param("test_size", len(X_test))
    
        print("Building and training model...")
        model = build_model()
        model.fit(X_train, y_train)
    
        mlflow.log_param("model_type", "RandomForestClassifier")
        mlflow.log_param("n_estimators", model['classifier'].n_estimators)
        mlflow.log_param("max_depth", model['classifier'].max_depth)


        print("Evaluating model...")
        metrics = evaluate_model(model, X_test, y_test)
        print(f"Accuracy: {metrics['accuracy']:.4f}")

        print("Classification Report:")
        print(metrics['report'])
        
        print("Saving model...")
        save_model(model, MODEL_FILE)
        
        mlflow.log_artifact(MODEL_FILE)
        mlflow.log_metric("accuracy", metrics['accuracy'])
        # log model
        mlflow.sklearn.log_model(model['classifier'], "model")
        return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train loan prediction model")
    parser.add_argument("--data", type=str, default=str(DATA_FILE), help="Path to the data file")
    parser.add_argument("--output", type=str, default=str(MODEL_FILE), help="Path to save the model")
    
    args = parser.parse_args()
    
    # Override config if provided
    DATA_FILE = Path(args.data)
    MODEL_FILE = Path(args.output)
    
    train()