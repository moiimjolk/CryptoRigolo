from Salsa20 import *

# test 
key = bytes([0x00] * 32)  # 256 bits
nonce = bytes([0x00] * 8)  # 64 bits

plaintext = b"test test test avec benoit mon homme"
ciphertext = salsa20_encrypt_decrypt(key, nonce, plaintext)

print("Encryp :", ciphertext)

decrypted = salsa20_encrypt_decrypt(key, nonce, ciphertext)
print("Decryp :", decrypted.decode('utf-8'))

crypt_all(key, nonce, "benoit.txt", "benoitout.txt")
crypt_all(key, nonce, "benoitout.txt", "benoitout.txt")

