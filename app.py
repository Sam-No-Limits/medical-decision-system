import streamlit as st
import numpy as np
import pandas as pd
from encryption.key_generator import generate_keys
from encryption.decrypt_data import decrypt_value
from ml_model.predict import predict_disease
from fuzzy_logic.risk_assessment import assess_risk
from llm_module.explanation_generator import generate_explanation

st.set_page_config(page_title="Medical Decision Support System")
st.title("🩺 Privacy-Preserving Medical Decision Support System")

st.sidebar.header("Enter Patient Details")

# ---------------------------
# 1. User Input Form
# ---------------------------
weight = st.sidebar.number_input("Weight (Kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input("Height (cm)", min_value=100.0, max_value=220.0, value=170.0)
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=24.0)
ogtt_1h = st.sidebar.number_input("OGTT 1h (mg/dL)", min_value=50, max_value=300, value=120)
ogtt_2h = st.sidebar.number_input("OGTT 2h (mg/dL)", min_value=50, max_value=300, value=140)
ogtt_3h = st.sidebar.number_input("OGTT 3h (mg/dL)", min_value=50, max_value=300, value=160)
fpg = st.sidebar.number_input("FPG (mg/dL)", min_value=50, max_value=200, value=95)
heart_rate = st.sidebar.number_input("Heart Rate (bpm)", min_value=40, max_value=180, value=80)
hba1c = st.sidebar.number_input("HbA1c (%)", min_value=3.0, max_value=15.0, value=5.5)

if st.button("Run Clinical Assessment"):

    # ---------------------------
    # 2. Prepare Input
    # ---------------------------
    new_patient = np.array([[weight, height, bmi, ogtt_1h, ogtt_2h, ogtt_3h, fpg, heart_rate, hba1c]])

    # ---------------------------
    # 3. ML Prediction
    # ---------------------------
    prediction, ml_confidence = predict_disease(new_patient)

    # ---------------------------
    # 4. Fuzzy Risk Assessment
    # ---------------------------
    similarity_score = 0.7  # dummy, can implement similarity search later
    risk_level = assess_risk(ml_confidence, similarity_score)

    # ---------------------------
    # 5. LLM Explanation
    # ---------------------------
    llm_output = generate_explanation(prediction, ml_confidence, risk_level)

    # ---------------------------
    # 6. Display Results
    # ---------------------------
    st.markdown("### 📌 Clinical Assessment Results")

    status_text = "GDM Detected 🔴" if prediction == 1 else "No GDM Detected 🟢"
    st.write(f"**Disease Status:** {status_text}")
    st.write(f"**ML Confidence:** {ml_confidence:.2f}")
    st.write(f"**Risk Level:** {risk_level.upper()}")

    if risk_level.lower() in ["high", "critical"]:
        st.warning("❗ Immediate medical consultation is strongly advised.")
    else:
        st.success("✅ Routine monitoring is recommended.")

    st.markdown("### 🧠 LLM Explanation")
    st.write(f"**Explanation:** {llm_output['explanation']}")
    st.write(f"**Recommendation:** {llm_output['recommendation']}")
