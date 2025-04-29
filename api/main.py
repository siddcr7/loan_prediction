# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.schemas import LoanApplication, PredictionResponse
from src.utils import load_model, make_prediction

# Initialize FastAPI app
app = FastAPI(
    title="Loan Prediction API",
    description="API for predicting loan approval status",
    version="1.0.0"
)

# Add CORS middleware to allow requests from the Streamlit app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model at startup
@app.on_event("startup")
async def startup_event():
    global model
    try:
        model = load_model()
    except Exception as e:
        # Log error but let the application start
        print(f"Error loading model: {e}")
        model = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the Loan Prediction API"}

@app.post("/predict", response_model=PredictionResponse)
def predict(application: LoanApplication):
    """
    Make a prediction based on loan application data
    """
    # if model is None:
    #     raise HTTPException(status_code=503, detail="Model not available")
    
    # Convert pydantic model to dict
    input_data = application.dict()
    
    # Process inputs to match model expectations
    input_data["Dependents"] = str(input_data["Dependents"])
    input_data["Credit_History"] = float(input_data["Credit_History"])
    
    # Make prediction
    result = make_prediction(model, input_data)
    
    return result

# Run with: uvicorn api.main:app --reload

# Update to api/main.py - add health check endpoint

@app.get("/health")
def health_check():
    """Health check endpoint for Docker"""
    if model is None:
        return {"status": "warning", "message": "Service running but model not loaded"}
    return {"status": "healthy", "message": "Service is running with model loaded"}