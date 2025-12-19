import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from encryption.key_generator import generate_keys
from encryption.decrypt_data import decrypt_value
from ml_model.predict import predict_disease
from fuzzy_logic.risk_assessment import assess_risk
from llm_module.explanation_generator import generate_explanation


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Medical Decision Support System",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Medical Decision Support System")
st.markdown("### AI-Driven GDM Risk Prediction & Clinical Assistance")

st.divider()

# --------------------------------------------------
# Load & decrypt data
# --------------------------------------------------
@st.cache_data
def load_patient_data():
    generate_keys()
    encrypted_file_path = "DATA/patient_data.csv"
    private_key_path = "encryption/private_key.pem"
    return decrypt_value(encrypted_file_path, private_key_path)


patient_data = load_patient_data()

# --------------------------------------------------
# Sidebar – Patient Selection
# --------------------------------------------------
st.sidebar.header("🧑‍⚕️ Patient Selection")

patient_index = st.sidebar.number_input(
    "Select Patient Index",
    min_value=0,
    max_value=len(patient_data) - 1,
    value=0
)

selected_patient = patient_data.iloc[[patient_index]]

st.sidebar.subheader("📋 Patient Data")
st.sidebar.dataframe(selected_patient)

# --------------------------------------------------
# Prediction Button
# --------------------------------------------------
if st.button("🔍 Run Clinical Assessment"):

    with st.spinner("Analyzing patient data..."):

        # ML Prediction
        prediction, ml_confidence = predict_disease(selected_patient.values)

        # Similarity score (placeholder)
        similarity_score = 0.7

        # Fuzzy Risk Assessment
        risk_level = assess_risk(ml_confidence, similarity_score)

        # LLM Explanation
        explanation = generate_explanation(
            prediction,
            ml_confidence,
            risk_level
        )

    st.success("Assessment completed successfully!")

    st.divider()

    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------
    st.subheader("📌 Clinical Summary")
    st.write(explanation)

    st.subheader("⚠️ Important Notes")

    col1, col2, col3 = st.columns(3)

    with col1:
        if prediction == 1:
            st.error("🔴 GDM Detected")
        else:
            st.success("🟢 No GDM Detected")

    with col2:
        st.metric("📊 Model Confidence", f"{ml_confidence:.2f}")

    with col3:
        st.metric("🚨 Risk Level", risk_level.upper())

    st.subheader("📋 Recommendation")

    if risk_level.lower() in ["high", "critical"]:
        st.warning("❗ Immediate medical consultation is strongly advised.")
    else:
        st.info("✅ Routine monitoring is recommended.")

    st.caption("👨‍⚕️ This system supports clinical decisions and does not replace professional medical judgment.")
