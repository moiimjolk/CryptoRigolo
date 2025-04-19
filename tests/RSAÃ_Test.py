from CryptoRigolo.RSA import *


#Comment ça devrait fonctionner... ;_;
public_key, private_key = generate_keys()
print("Clé pub :", public_key)
print("Clé pri :", private_key)

message = "Benoit mon homme"
encrypted = crypt(message, public_key)
print("Encryp :", encrypted)

decrypted = decrypt(encrypted, private_key)
print("Decryp :", decrypted)

crypt_all("benoit.txt", "a", "benoitout.txt", crypt)
crypt_all("benoitout.txt", "a", "benoitout.txt", decrypt)

