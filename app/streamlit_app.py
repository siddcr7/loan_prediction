# app/streamlit_app.py
import streamlit as st
import pandas as pd
import requests
import json
import os 

# Define the API endpoint
API_URL = os.environ.get("API_URL", "http://localhost:8000/predict")


def main():
    st.title("Loan Approval Prediction System")
    st.write("Enter your details below to check loan eligibility")
    
    # Create a form for user input
    with st.form("loan_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            gender = st.selectbox("Gender", options=["Male", "Female"])
            married = st.selectbox("Marital Status", options=["Yes", "No"])
            dependents = st.selectbox("Number of Dependents", options=["0", "1", "2", "3"])
            education = st.selectbox("Education", options=["Graduate", "Not Graduate"])
            self_employed = st.selectbox("Self Employed", options=["Yes", "No"])
            applicant_income = st.number_input("Monthly Income ($)", min_value=0, value=3000)
            
        with col2:
            coapplicant_income = st.number_input("Co-applicant Income ($)", min_value=0, value=0)
            loan_amount = st.number_input("Loan Amount (in thousands $)", min_value=0, value=120)
            loan_term = st.number_input("Loan Term (months)", min_value=12, max_value=480, value=360, step=12)
            credit_history = st.selectbox("Credit History Meets Guidelines", options=[1, 0], 
                                          format_func=lambda x: "Yes" if x == 1 else "No")
            property_area = st.selectbox("Property Area", options=["Urban", "Semiurban", "Rural"])
        
        submit_button = st.form_submit_button("Check Eligibility")
    
    # When form is submitted
    if submit_button:
        # Create payload for API
        payload = {
            "Gender": gender,
            "Married": married,
            "Dependents": dependents,
            "Education": education,
            "Self_Employed": self_employed,
            "ApplicantIncome": applicant_income,
            "CoapplicantIncome": coapplicant_income,
            "LoanAmount": loan_amount,
            "Loan_Amount_Term": loan_term,
            "Credit_History": credit_history,
            "Property_Area": property_area
        }
        
        # Call API
        try:
            with st.spinner("Calculating eligibility..."):
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Display result with nice formatting
                    if result["prediction"] == "Approved":
                        st.success(f"✅ Loan Approved! (Confidence: {result['probability']:.2%})")
                        st.balloons()
                    else:
                        st.error(f"❌ Loan Rejected. (Confidence: {result['probability']:.2%})")
                        
                    # Show factors that might affect the decision
                    st.subheader("Key Factors Affecting Decision")
                    factors_df = pd.DataFrame({
                        'Factor': ['Income', 'Loan Amount', 'Credit History', 'Property Area'],
                        'Your Value': [
                            f"${applicant_income + coapplicant_income:,}",
                            f"${loan_amount * 1000:,}",
                            "Good" if credit_history == 1 else "Poor",
                            property_area
                        ]
                    })
                    st.table(factors_df)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error connecting to API: {e}")
            st.info("Make sure the FastAPI server is running at http://localhost:8000")

if __name__ == "__main__":
    main()

# Run with: streamlit run app/streamlit_app.py