from RC4 import *

# test comme d'hab
key = b"Benoit"
plaintext = b"Mon amour"

ciphertext = rc4_encrypt_decrypt(key, plaintext)
print("Encryp :", ciphertext)

decrypted = rc4_encrypt_decrypt(key, ciphertext)
print("Decryp :", decrypted.decode())


crypt_all(key, "benoit.txt", "benoitout.txt", crypt)
crypt_all(key, "benoitout.txt", "benoitout.txt", decrypt)

