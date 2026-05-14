import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('loan_model.pkl')

st.title("🏦 Loan Approval Prediction App")
st.write("Predict if a loan will be approved based on applicant details.")

# User inputs
gender = st.selectbox("Gender", ['Male', 'Female'])
married = st.selectbox("Married", ['Yes', 'No'])
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
self_emp = st.selectbox("Self Employed", ['Yes', 'No'])
app_income = st.number_input("Applicant Income", min_value=0)
coapp_income = st.number_input("Coapplicant Income", min_value=0)
loan_amt = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Term", [360, 180, 120, 480])
credit_hist = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ['Urban', 'Semiurban', 'Rural'])

# Prepare input data
input_data = pd.DataFrame({
    'Gender': [0 if gender == 'Male' else 1],
    'Married': [0 if married == 'No' else 1],
    'Dependents': [dependents],
    'Education': [0 if education == 'Graduate' else 1],
    'Self_Employed': [0 if self_emp == 'No' else 1],
    'ApplicantIncome': [app_income],
    'CoapplicantIncome': [coapp_income],
    'LoanAmount': [loan_amt],
    'Loan_Amount_Term': [loan_term],
    'Credit_History': [credit_hist],
    'Property_Area': [0 if property_area == 'Rural' else (1 if property_area == 'Semiurban' else 2)]
})

if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)
    result = "✅ Loan Approved" if prediction[0] == 1 else "❌ Loan Not Approved"
    st.success(result)
