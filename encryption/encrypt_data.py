# encryption/encrypt_data.py

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# Load public key
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

def encrypt_value(value):
    encrypted = public_key.encrypt(
        str(value).encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(encrypted).decode()

# Example patient data
patient_data = {
    "WEIGHT(Kg)": 45,
    "HEIGHT(cm)": 28.5,
    "BMI": 160,
    "TT(1h)(mg/dL)": 155,
    "TT(2h)(mg/dL)": 110,
    "TT(3h)(mg/dL)": 155,
    "FPG(mg/dL)": 92,
    "HEART RATE(bpm)": 75,
    "HbA1c(%)": 5.8,
    "GDM_TARGET": 1
}

# Encrypt each field
encrypted_data = {
    key: encrypt_value(value)
    for key, value in patient_data.items()
}

print("Encrypted Patient Data:")
print(encrypted_data)
