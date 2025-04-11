#renamed so due to the fact that python doesn't like files which are starting with a number
import DES

def triple_des_encrypt(plaintext, key1, key2, key3):
    step1 = DES.des_encrypt(plaintext, key1)
    step2 = DES.des_decrypt(step1, key2)
    step3 = DES.des_encrypt(step2, key3)
    return step3

def triple_des_decrypt(ciphertext, key1, key2, key3):
    step1 = DES.des_decrypt(ciphertext, key3)
    step2 = DES.des_encrypt(step1, key2)
    step3 = DES.des_decrypt(step2, key1)
    return step3

# test
plaintext = "12345678"  # oui toujours 8 octets
key1 = "abcdefgh"       # K1
key2 = "ijklmnop"       # K2
key3 = "qrstuvwx"       # K3

ciphertext = triple_des_encrypt(plaintext, key1, key2, key3)
print("Chiffré (3DES) :", ciphertext)

decrypted_text = triple_des_decrypt(ciphertext, key1, key2, key3)
print("Déchiffré :", decrypted_text)
