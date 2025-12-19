import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from encryption.key_generator import generate_keys
from encryption.decrypt_data import decrypt_value
from ml_model.predict import predict_disease
from fuzzy_logic.risk_assessment import assess_risk
from llm_module.explanation_generator import generate_explanation


def main():
    # --------------------------------------------------
    # 1. Generate encryption keys (if not exist)
    # --------------------------------------------------
    public_key_path, private_key_path = generate_keys()

    # --------------------------------------------------
    # 2. Decrypt patient data
    # --------------------------------------------------
    encrypted_file_path = "/Volumes/1-TB-SSD/MEDICAL-DECISION-SYSTEM/DATA/patient_data.csv"
    patient_data = decrypt_value(encrypted_file_path, private_key_path)

    # --------------------------------------------------
    # 3. Select one patient (first row)
    # --------------------------------------------------
    new_patient = patient_data.iloc[[0]].values

    # --------------------------------------------------
    # 4. ML prediction
    # --------------------------------------------------
    prediction, ml_confidence = predict_disease(new_patient)

    # --------------------------------------------------
    # 5. Similarity score (placeholder)
    # --------------------------------------------------
    similarity_score = 0.7

    # --------------------------------------------------
    # 6. Fuzzy risk assessment
    # --------------------------------------------------
    risk_level = assess_risk(ml_confidence, similarity_score)

    # --------------------------------------------------
    # 7. LLM explanation
    # --------------------------------------------------
    llm_output = generate_explanation(
        prediction,
        ml_confidence,
        risk_level
    )

    # --------------------------------------------------
    # 8. FINAL OUTPUT
    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("🩺 FINAL CLINICAL ASSESSMENT")
    print("=" * 60)

    print("\n📌 SUMMARY")
    print(llm_output)

    print("\n⚠️ IMPORTANT NOTES")
    print("-" * 60)

    if prediction == 1:
        print("🔴 Disease Status      : GDM Detected")
    else:
        print("🟢 Disease Status      : No GDM Detected")

    print(f"📊 Model Confidence    : {ml_confidence:.2f}")
    print(f"🚨 Risk Classification : {risk_level.upper()}")

    if risk_level.lower() in ["high", "critical"]:
        print("❗ Immediate medical consultation is strongly advised.")
    else:
        print("✅ Routine monitoring is recommended.")

    print("\n📋 RECOMMENDATION")
    print("-" * 60)
    print("👨‍⚕️ Please consult a qualified healthcare professional for clinical validation and next steps.")

    print("\n" + "=" * 60)


# --------------------------------------------------
# Entry point
# --------------------------------------------------
if __name__ == "__main__":
    main()
