from ChaCha20 import *

# test
key = bytes([0x00] * 32)  # 256 bits
nonce = bytes([0x00] * 8)  # 64 bits

plaintext = b"Wsh la team benoit c'est mon homme!"
ciphertext = chacha20_encrypt_decrypt(key, nonce, plaintext)

print("Encryp :", ciphertext)

decrypted = chacha20_encrypt_decrypt(key, nonce, ciphertext)
print("Decryp :", decrypted.decode('utf-8'))


crypt_all(key, nonce, "benoit.txt", "benoitout.txt")
crypt_all(key, nonce, "benoitout.txt", "benoitout.txt")
