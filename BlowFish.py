from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from fileHandler import *
import hashlib
import fileHandler

def crypt(data, password, salt):
    """
    Encrypt using Blowfish algorithm
    Blowfish uses variable length keys, we'll use up to 56 bytes
    """
    # Create a key from password and salt (Blowfish can use up to 56 bytes)
    key = hashlib.sha256(password.encode() + salt).digest()[:56]  # Ensure key is up to 56 bytes
    
    # Create cipher
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    
    # Get IV
    iv = cipher.iv
    
    # Encrypt data
    padded_data = pad(data, Blowfish.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    
    # Return IV + encrypted data
    return iv + encrypted_data

def decrypt(data, password, salt):
    """
    Decrypt using Blowfish algorithm
    """
    # Create a key from password and salt
    key = hashlib.sha256(password.encode() + salt).digest()[:56]  # Ensure key is up to 56 bytes
    
    # Extract IV (first 8 bytes for Blowfish) and ciphertext
    iv = data[:8]
    ciphertext = data[8:]
    
    # Create cipher with extracted IV
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv=iv)
    
    # Decrypt data
    padded_data = cipher.decrypt(ciphertext)
    
    # Remove padding
    try:
        original_data = unpad(padded_data, Blowfish.block_size)
        return original_data
    except ValueError as e:
        raise ValueError(f"Decryption failed: {str(e)}")

#wrappers for the interface   


def crypt_all(text, keyword, salt, target, function):
    reader=FileHandler()
    data=reader.read_file(text)
    message=function(data, keyword, bytes(salt,  encoding='UTF-8'))
    reader.save_file(message, target)