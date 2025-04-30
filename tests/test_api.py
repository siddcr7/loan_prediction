import json
from fastapi.testclient import TestClient
import joblib
from api.main import app  # adjust path to your FastAPI app
import joblib
client = TestClient(app)

model=joblib.load('models/loan_model.pkl')
def test_predict_valid_input():
    payload = {
        "Loan_ID": "LP001002",
        "Gender": "Male",
        "Married": "Yes",
        "Dependents": "0",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 5849,
        "CoapplicantIncome": 0.0,
        "LoanAmount": 128.0,
        "Loan_Amount_Term": 360.0,
        "Credit_History": 1.0,
        "Property_Area": "Urban",
        "Loan_Status": "Y"  # Optional — remove if you're predicting this
    }

    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    assert "prediction" in response.json()