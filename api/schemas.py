# api/schemas.py
from pydantic import BaseModel, Field
from typing import Optional, Literal

class LoanApplication(BaseModel):
    Gender: Literal['Male', 'Female'] = Field(description="Gender of the applicant")
    Married: Literal['Yes', 'No'] = Field(description="Marital status of the applicant")
    Dependents: Literal['0', '1', '2', '3'] = Field(description="Number of dependents")
    Education: Literal['Graduate', 'Not Graduate'] = Field(description="Education level")
    Self_Employed: Literal['Yes', 'No'] = Field(description="Self-employment status")
    ApplicantIncome: int = Field(description="Monthly income of the applicant")
    CoapplicantIncome: float = Field(description="Monthly income of the co-applicant")
    LoanAmount: float = Field(description="Loan amount in thousands")
    Loan_Amount_Term: float = Field(description="Term of loan in months")
    Credit_History: Literal[0, 1] = Field(description="Credit history meets guidelines (1: Yes, 0: No)")
    Property_Area: Literal['Rural', 'Semiurban', 'Urban'] = Field(description="Property area")

class PredictionResponse(BaseModel):
    prediction: str = Field(description="Loan approval prediction (Approved/Rejected)")
    probability: float = Field(description="Probability of the prediction")