from DES import *

plaintext = "et le text"
key = "abcdefgh"
cipher = des_encrypt(plaintext, key)
print("Texte clair :", plaintext)
print("Chiffré     :", cipher)

decrypted = des_decrypt(cipher, key)
print("Déchiffré   :", decrypted)

crypt_all("benoit.txt", "bennnnnn", "benoitout.txt", crypt)
crypt_all("benoitout.txt", "bennnnnn", "benoitout.txt", decrypt)
