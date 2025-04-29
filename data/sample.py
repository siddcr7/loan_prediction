# script to create sample loan data
import pandas as pd
import numpy as np
import os
from src.config import DATA_DIR

# Create sample loan prediction data
def create_sample_data():
    np.random.seed(42)
    n_samples = 500
    
    data = {
        'Loan_ID': [f'LOAN{i:05d}' for i in range(1, n_samples + 1)],
        'Gender': np.random.choice(['Male', 'Female'], size=n_samples, p=[0.7, 0.3]),
        'Married': np.random.choice(['Yes', 'No'], size=n_samples, p=[0.65, 0.35]),
        'Dependents': np.random.choice(['0', '1', '2', '3'], size=n_samples, p=[0.5, 0.2, 0.2, 0.1]),
        'Education': np.random.choice(['Graduate', 'Not Graduate'], size=n_samples, p=[0.75, 0.25]),
        'Self_Employed': np.random.choice(['Yes', 'No'], size=n_samples, p=[0.15, 0.85]),
        'ApplicantIncome': np.random.normal(5000, 2000, n_samples).astype(int),
        'CoapplicantIncome': np.random.choice([0, n_samples], p=[0.4, 0.6]),
        'LoanAmount': np.random.normal(150, 70, n_samples).astype(int),
        'Loan_Amount_Term': np.random.choice([360, 180, 240, 120, 480, 300, 60], size=n_samples, p=[0.7, 0.1, 0.1, 0.03, 0.03, 0.02, 0.02]),
        'Credit_History': np.random.choice([1.0, 0.0], size=n_samples, p=[0.8, 0.2]),
        'Property_Area': np.random.choice(['Urban', 'Semiurban', 'Rural'], size=n_samples, p=[0.4, 0.4, 0.2])
    }
    
    # Make ApplicantIncome all positive
    data['ApplicantIncome'] = np.abs(data['ApplicantIncome'])
    data['ApplicantIncome'] = np.maximum(data['ApplicantIncome'], 1000)
    
    # Make CoapplicantIncome all positive
    data['CoapplicantIncome'] = np.abs(data['CoapplicantIncome'])
    
    # Make LoanAmount all positive and reasonable
    data['LoanAmount'] = np.abs(data['LoanAmount'])
    data['LoanAmount'] = np.maximum(data['LoanAmount'], 10)
    
    # Define a function for loan approval with some realistic rules
    def predict_loan(row):
        # Base approval chance
        approval_chance = 0.5
        
        # Credit history is very important
        if row['Credit_History'] == 1.0:
            approval_chance += 0.3
        else:
            approval_chance -= 0.3
            
        # Income to loan ratio
        total_income = row['ApplicantIncome'] + row['CoapplicantIncome']
        loan_amount = row['LoanAmount'] * 1000  # Convert to actual amount
        income_loan_ratio = total_income / loan_amount if loan_amount > 0 else 10
        
        if income_loan_ratio > 3:
            approval_chance += 0.2
        elif income_loan_ratio > 2:
            approval_chance += 0.1
        elif income_loan_ratio < 1:
            approval_chance -= 0.2
            
        # Property area impact
        if row['Property_Area'] == 'Urban':
            approval_chance += 0.05
        elif row['Property_Area'] == 'Semiurban':
            approval_chance += 0.03
            
        # Education impact
        if row['Education'] == 'Graduate':
            approval_chance += 0.05
            
        # Married with dependents shows stability
        if row['Married'] == 'Yes' and row['Dependents'] != '0':
            approval_chance += 0.05
            
        # Add randomness
        approval_chance += np.random.normal(0, 0.1)
        
        # Return result with some randomness
        return 'Y' if np.random.random() < approval_chance else 'N'
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Generate target variable based on features
    df['Loan_Status'] = df.apply(predict_loan, axis=1)
    
    # Save to CSV
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(DATA_DIR / 'loan_prediction.csv', index=False)
    print(f"Sample data saved to {DATA_DIR / 'loan_prediction.csv'}")
    
    return df

if __name__ == "__main__":
    create_sample_data()