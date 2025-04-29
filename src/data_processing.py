# src/data_processing.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.config import CATEGORICAL_COLS, NUMERICAL_COLS, TARGET_COL, RANDOM_STATE, TEST_SIZE

def load_data(filepath):
    """Load data from CSV file"""
    return pd.read_csv(filepath)

def preprocess_data(df):
    """Preprocess the data"""
    # Make a copy to avoid modifying the original
    data = df.copy()
    
    # Replace loan status values
    data[TARGET_COL] = data[TARGET_COL].map({'Y': 'Y', 'N': 'N'})
    
    # Replace categorical values with more descriptive ones
    data['Dependents'] = data['Dependents'].replace('3+', '3')
    
    # Convert numeric columns
    for col in ['Dependents', 'Credit_History']:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    
    return data

def create_preprocessing_pipeline():
    """Create a preprocessing pipeline for categorical and numerical data"""
    # Define categorical preprocessing
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # Define numerical preprocessing
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    # Combine preprocessors
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, NUMERICAL_COLS),
            ('cat', categorical_transformer, CATEGORICAL_COLS)
        ])
    
    return preprocessor

def split_train_test(df, target_col=TARGET_COL, test_size=TEST_SIZE, random_state=RANDOM_STATE):
    """Split data into training and testing sets"""
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)