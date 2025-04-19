from threeDES import *

#test
plaintext = "12345678"
key1 = "abcdefgh"       # K1
key2 = "ijklmnop"       # K2
key3 = "qrstuvwx"       # K3

ciphertext = triple_des_encrypt(plaintext, key1, key2, key3)
print("Chiffré (3DES) :", ciphertext)

decrypted_text = triple_des_decrypt(ciphertext, key1, key2, key3)
print("Déchiffré :", decrypted_text)

crypt_all(triple_des_encrypt_full, key1, key2, key3, "benoit.txt", "benoitout.txt")
crypt_all(triple_des_decrypt_full, key1, key2, key3, "benoitout.txt", "benoitout.txt")
