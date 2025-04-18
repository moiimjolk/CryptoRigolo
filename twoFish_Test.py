import unittest
from CryptoRigolo.TwoFish import encrypt, decrypt
import os

class TestTwoFish(unittest.TestCase):
    def setUp(self):
        
        self.data = "Données de test pour le chiffrement".encode("utf-8")
        self.password = "motdepassesecure"
        self.salt = os.urandom(16)

    def test_encrypt_decrypt(self):
      
        encrypted_data = encrypt(self.data, self.password, self.salt)
       
        decrypted_data = decrypt(encrypted_data, self.password, self.salt)
        
        self.assertEqual(decrypted_data, self.data)

    def test_decrypt_with_wrong_password(self):
       
        encrypted_data = encrypt(self.data, self.password, self.salt)
        
        wrong_password = "mauvaismotdepasse"
        with self.assertRaises(ValueError):
            decrypt(encrypted_data, wrong_password, self.salt)

    def test_decrypt_with_invalid_data(self):
        
        invalid_data = b"donnees_invalides"
        with self.assertRaises(ValueError):
            decrypt(invalid_data, self.password, self.salt)

if __name__ == "__main__":
    # Exécuter les tests
    unittest.main()