import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessing files
model = joblib.load("KNNheart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# App title
st.title("❤️ Heart Disease Prediction App")
st.markdown("Provide the following details to predict heart disease.")

# User inputs
age = st.slider("Age", 18, 100, 40)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "ASY", "TA"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=200,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dl)",
    min_value=100,
    max_value=600,
    value=200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    ["Yes", "No"]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVM"]
)

max_hr = st.slider(
    "Maximum Heart Rate",
    60,
    220,
    150
)

exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)

oldpeak = st.number_input(
    "Oldpeak (ST Depression)",
    min_value=0.0,
    max_value=6.0,
    value=1.0,
    step=0.1
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)


# Prediction
if st.button("Predict"):

    # Convert Yes/No to 1/0
    fasting_bs_value = 1 if fasting_bs == "Yes" else 0

    # Create input dictionary
    input_data = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs_value,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,

        # One-hot encoded features
        "Sex_" + sex: 1,
        "ChestPainType_" + chest_pain: 1,
        "RestingECG_" + resting_ecg: 1,
        "ExerciseAngina_" + exercise_angina: 1,
        "ST_Slope_" + st_slope: 1
    }

    # Convert dictionary to DataFrame
    input_df = pd.DataFrame([input_data])

    # Add missing columns
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Keep exactly the same column order as training
    input_df = input_df[expected_columns]

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_input)[0]

    # Result
    if prediction == 1:
        st.error(
            "⚠️ The model predicts a higher likelihood of heart disease."
        )

    else:
        st.success(
            "✅ The model predicts a lower likelihood of heart disease."
        )