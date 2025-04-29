# Loan Prediction ML Project

This project provides a machine learning solution for predicting loan approval based on applicant information. It includes a FastAPI backend for serving predictions and a Streamlit frontend for user interaction.

## Project Structure

```
loan_prediction/
├── data/               # Data storage
├── models/             # Trained model storage
├── src/                # Core ML code
├── api/                # FastAPI application
├── app/                # Streamlit application
├── requirements.txt    # Dependencies
├── README.md           # Documentation
└── setup.py            # Package setup
```

## Features

- **Machine Learning Model**: Random Forest classifier for loan prediction
- **Data Processing**: Preprocessing pipelines for handling categorical and numerical data
- **API**: FastAPI backend for serving predictions
- **Frontend**: Interactive Streamlit application for user input
- **Model Training**: Scripts for training and evaluating the model

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/loan-prediction.git
   cd loan-prediction
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Generate sample data and train the model:
   ```
   python -c "from src.sample_data import create_sample_data; create_sample_data()"
   python -m src.train
   ```

## Usage

1. Start the FastAPI backend:
   ```
   uvicorn api.main:app --reload
   ```

2. In a new terminal, start the Streamlit frontend:
   ```
   streamlit run app/streamlit_app.py
   ```

3. Open your browser and navigate to the Streamlit app (typically http://localhost:8501)

## API Documentation

Once the FastAPI server is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Model Details

The loan prediction model uses a Random Forest classifier with the following features:
- Applicant demographics (Gender, Marital Status, Education, etc.)
- Financial information (Income, Loan Amount, etc.)
- Property information
- Credit history

## License

This project is licensed under the MIT License.