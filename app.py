import streamlit as st

import numpy as np

import pandas as pd

from datetime import datetime

from typing import Dict



# Placeholder functions for risk algorithms

def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):

  # Simplified example calculation for cardiovascular risk

  risk_score = (age * 0.1) + (systolic_bp * 0.05) + (10 if smoker else 0) + (cholesterol * 0.02)

  if risk_score > 15:

    return "High"

  elif risk_score > 10:

    return "Moderate"

  else:

    return "Low"



def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose):

  # Simplified example calculation for diabetes risk

  risk_score = (bmi * 0.3) + (age * 0.1) + (10 if family_history else 0) + (fasting_glucose * 0.02)

  if risk_score > 20:

    return "High"

  elif risk_score > 15:

    return "Moderate"

  else:

    return "Low"



def calculate_copd_risk(smoking_years, age, fev1):

  # Simplified example calculation for COPD risk

  risk_score = (smoking_years * 0.5) + (age * 0.2) - (fev1 * 0.1)

  if risk_score > 25:

    return "High"

  elif risk_score > 15:

    return "Moderate"

  else:

    return "Low"



# Streamlit App Layout

st.title("Chronic Condition Risk Stratification")

st.write("This application helps stratify risk for chronic conditions according to evidence-based guidelines.")



# Input: Patient Demographics

st.header("Patient Information")

age = st.number_input("Age", min_value=18, max_value=100, value=30)

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)

sex = st.selectbox("Sex", options=["Male", "Female"])

smoker = st.radio("Smoking Status", options=["Non-smoker", "Current smoker", "Former smoker"])



# Input: Cardiovascular Risk Factors

st.header("Cardiovascular Risk Factors")

systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 90, 200, 120)

cholesterol = st.slider("Total Cholesterol (mg/dL)", 100, 300, 180)



# Input: Diabetes Risk Factors

st.header("Diabetes Risk Factors")

fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=90)

family_history = st.radio("Family History of Diabetes", options=["Yes", "No"])



# Input: COPD Risk Factors

st.header("COPD Risk Factors")

smoking_years = st.number_input("Years of Smoking (if applicable)", min_value=0, max_value=60, value=0)

fev1 = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=80)



# Risk Calculation

st.header("Risk Stratification Results")

results = {}



# Cardiovascular Risk Calculation

cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker == "Current smoker", cholesterol)

st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")

results["Cardiovascular"] = cardio_risk



# Diabetes Risk Calculation

diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose)

st.write(f"**Diabetes Risk Level**: {diabetes_risk}")

results["Diabetes"] = diabetes_risk



# COPD Risk Calculation

copd_risk = calculate_copd_risk(smoking_years, age, fev1)

st.write(f"**COPD Risk Level**: {copd_risk}")

results["COPD"] = copd_risk



# Recommendations based on risk levels

st.header("Personalized Recommendations")

for condition, risk in results.items():

  if risk == "High":

    st.error(f"{condition} Risk is High. Immediate lifestyle modification and medical consultation recommended.")

  elif risk == "Moderate":

    st.warning(f"{condition} Risk is Moderate. Consider lifestyle changes and regular monitoring.")

  else:

    st.success(f"{condition} Risk is Low. Maintain a healthy lifestyle and regular check-ups.")



# Display Date and Time of Assessment

st.write("Assessment Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

