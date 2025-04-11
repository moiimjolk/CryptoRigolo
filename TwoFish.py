from Crypto.Cipher import AES  # Note: PyCryptodome doesn't have native Twofish
from Crypto.Util.Padding import pad, unpad
import hashlib
import os

# Note: Since PyCryptodome doesn't include Twofish natively,
# we're using AES-256 as a substitute for demonstration purposes.
# In a production environment, you would use a proper Twofish implementation.

def encrypt(data, password, salt):
    """
    Encrypt using "Twofish" (simulated with AES-256)
    """
    # Create a 32-byte key (256 bits) from password using SHA-256
    key = hashlib.sha256(password.encode() + salt).digest()
    
    # Create cipher
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Get IV
    iv = cipher.iv
    
    # Encrypt data
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    
    # Return IV + encrypted data
    return iv + encrypted_data

def decrypt(data, password, salt):
    """
    Decrypt using "Twofish" (simulated with AES-256)
    """
    # Recreate key from password
    key = hashlib.sha256(password.encode() + salt).digest()
    
    # Extract IV (first 16 bytes for AES) and ciphertext
    iv = data[:16]
    ciphertext = data[16:]
    
    # Create cipher with extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    
    # Decrypt data
    padded_data = cipher.decrypt(ciphertext)
    
    # Remove padding
    try:
        original_data = unpad(padded_data, AES.block_size)
        return original_data
    except ValueError as e:
        raise ValueError(f"Decryption failed: {str(e)}")