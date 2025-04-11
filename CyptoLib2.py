from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import importlib

# Import algorithm modules
from Algos import BlowFish, DES, TwoFish

class Cryptolib:
    ALGORITHMS = {
        "Fernet": "fernet",
        "Blowfish": "blowfish",
        "DES": "des",
        "Twofish": "twofish"
    }
    
    def __init__(self, filecontent=None):
        self.filecontent = filecontent
        self.key = None
        
    def generate_key_from_password(self, password, salt=None):
        """Generate a key from password using PBKDF2"""
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key, salt
    
    def encrypt_data(self, data, password, algorithm="Fernet"):
        """Encrypt data using selected encryption algorithm"""
        # Generate salt
        salt = os.urandom(16)
        
        # Store algorithm identifier (first byte)
        algorithm_id = bytes([list(self.ALGORITHMS.keys()).index(algorithm)])
        
        # Encrypt based on algorithm
        if algorithm == "Fernet":
            key, _ = self.generate_key_from_password(password, salt)
            cipher = Fernet(key)
            encrypted_data = cipher.encrypt(data)
            # Format: algorithm_id + salt + encrypted_data
            return algorithm_id + salt + encrypted_data
            
        elif algorithm == "Blowfish":
            encrypted_data = BlowFish.encrypt(data, password, salt)
            # Format: algorithm_id + salt + encrypted_data
            return algorithm_id + salt + encrypted_data
            
        elif algorithm == "DES":
            encrypted_data = DES.encrypt(data, password, salt)
            # Format: algorithm_id + salt + encrypted_data
            return algorithm_id + salt + encrypted_data
            
        elif algorithm == "Twofish":
            encrypted_data = TwoFish.encrypt(data, password, salt)
            # Format: algorithm_id + salt + encrypted_data
            return algorithm_id + salt + encrypted_data
            
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    def decrypt_data(self, encrypted_data, password):
        """Decrypt data using the algorithm identified in the encrypted data"""
        try:
            # Extract algorithm identifier (first byte)
            algorithm_id = encrypted_data[0]
            algorithm = list(self.ALGORITHMS.keys())[algorithm_id]
            
            # Extract salt (next 16 bytes)
            salt = encrypted_data[1:17]
            
            # Extract ciphertext (rest of the data)
            ciphertext = encrypted_data[17:]
            
            # Decrypt based on algorithm
            if algorithm == "Fernet":
                key, _ = self.generate_key_from_password(password, salt)
                cipher = Fernet(key)
                decrypted_data = cipher.decrypt(ciphertext)
                
            elif algorithm == "Blowfish":
                decrypted_data = BlowFish.decrypt(ciphertext, password, salt)
                
            elif algorithm == "DES":
                decrypted_data = DES.decrypt(ciphertext, password, salt)
                
            elif algorithm == "Twofish":
                decrypted_data = TwoFish.decrypt(ciphertext, password, salt)
                
            else:
                return f"Unsupported algorithm: {algorithm}"
                
            return decrypted_data
            
        except Exception as e:
            return f"Decryption failed: {e}"