# -*- coding: utf-8 -*-
import pandas as pd
import joblib
import os
import numpy as np

# Absolute-safe paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml_model", "gdm_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "ml_model", "scaler.pkl")
FEATURE_PATH = os.path.join(BASE_DIR, "ml_model", "feature_names.pkl")
def predict_disease(patient_data):
    import numpy as np
    import pandas as pd
    import joblib

    feature_names = joblib.load(FEATURE_PATH)

    # 🔥 CASE 1: NumPy array input
    if isinstance(patient_data, np.ndarray):
        # If 10 features, assume last is GDM_target → remove it
        if patient_data.shape[1] == len(feature_names) + 1:
            patient_data = patient_data[:, :-1]

        patient_data = pd.DataFrame(patient_data, columns=feature_names)

    # 🔥 CASE 2: DataFrame input
    elif isinstance(patient_data, pd.DataFrame):
        if 'GDM_target' in patient_data.columns:
            patient_data = patient_data.drop(columns=['GDM_target'])

        patient_data = patient_data[feature_names]

    else:
        raise TypeError("patient_data must be NumPy array or Pandas DataFrame")

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    patient_scaled = scaler.transform(patient_data)

    prediction = model.predict(patient_scaled)[0]
    confidence = model.predict_proba(patient_scaled).max()

    return prediction, confidence

