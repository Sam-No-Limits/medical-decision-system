import pandas as pd
from cryptography.hazmat.primitives import serialization

def decrypt_value(encrypted_file_path, private_key_path):
    """
    Dummy decryption: loads private key but just returns CSV as-is.
    """
    # Load private key
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # For now, just read CSV (replace with real decryption later)
    decrypted_data = pd.read_csv(encrypted_file_path)
    return decrypted_data
