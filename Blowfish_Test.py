import unittest
from CryptoRigolo.BlowFish import encrypt, decrypt
import os

class TestBlowFish(unittest.TestCase):
    def setUp(self):
        
        self.data = "Données de test pour le chiffrement".encode("utf-8")
        self.password = "motdepassesecure"
        self.salt = os.urandom(16)

    def test_encrypt_decrypt(self):
        # Chiffrer les données
        encrypted_data = encrypt(self.data, self.password, self.salt)
        # Déchiffrer les données
        decrypted_data = decrypt(encrypted_data, self.password, self.salt)
        # Vérifier que les données déchiffrées correspondent aux données originales
        self.assertEqual(decrypted_data, self.data)

    def test_decrypt_with_wrong_password(self):
        
        encrypted_data = encrypt(self.data, self.password, self.salt)
        # là c'est pour Tenter de déchiffrer avec un mot de passe incorrect
        wrong_password = "mauvaismotdepasse"
        with self.assertRaises(ValueError):
            decrypt(encrypted_data, wrong_password, self.salt)

    def test_decrypt_with_invalid_data(self):
        
        invalid_data = b"donnees_invalides"
        with self.assertRaises(ValueError):
            decrypt(invalid_data, self.password, self.salt)

if __name__ == "__main__":
   
    unittest.main()
