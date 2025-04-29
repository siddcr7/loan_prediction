# src/config.py
import os
from pathlib import Path

# Project directories
ROOT_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = ROOT_DIR / "data"
MODELS_DIR = ROOT_DIR / "models"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

# Data files
DATA_FILE = DATA_DIR / "loan_prediction.csv"
MODEL_FILE = MODELS_DIR / "loan_model.pkl"

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2

# Features for the model
CATEGORICAL_COLS = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
NUMERICAL_COLS = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
TARGET_COL = 'Loan_Status'