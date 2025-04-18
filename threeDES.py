#renamed so due to the fact that python doesn't like files which are starting with a number
#scuse nous doria l'américaine
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

def triple_des_encrypt_full(plaintext, key1, key2, key3):
    padded_data = DES.pad_data(plaintext)
    
    result = ""
    for i in range(0, len(padded_data), 8):
        block = padded_data[i:i+8]
        if isinstance(block, bytes):
            block = block.decode('latin-1')
        
        step1 = DES.des_encrypt(block, key1)
        step2 = DES.des_decrypt(step1, key2)
        step3 = DES.des_encrypt(step2, key3)
        
        result += step3
    
    return result

def triple_des_decrypt_full(ciphertext, key1, key2, key3):
    result = b""
    for i in range(0, len(ciphertext), 64):
        block = ciphertext[i:i+64]
        
        step1 = DES.des_decrypt(block, key3)
        step2 = DES.des_encrypt(step1, key2)
        step3 = DES.des_decrypt(step2, key1)
        
        result += step3.encode('latin-1')
    
    unpadded_data = DES.unpad_data(result)
    
    try:
        return unpadded_data.decode('latin-1')
    except:
        return unpadded_data

def crypt_all(operation, key1, key2, key3, input_file, output_file):
    if operation == triple_des_encrypt_full:
        try:
            with open(input_file, 'r') as f:
                data = f.read()
        except UnicodeDecodeError:
            with open(input_file, 'rb') as f:
                data = f.read()
        
        result = operation(data, key1, key2, key3)
        
        with open(output_file, 'w') as f:
            f.write(result)
    
    elif operation == triple_des_decrypt_full:
        with open(input_file, 'r') as f:
            cipher_bits = f.read()
        
        result = operation(cipher_bits, key1, key2, key3)
        
        if isinstance(result, str):
            with open(output_file, 'w') as f:
                f.write(result)
        else:
            with open(output_file, 'wb') as f:
                f.write(result)


# test
#plaintext = "12345678"  # oui toujours 8 octets
#key1 = "abcdefgh"       # K1
#key2 = "ijklmnop"       # K2
#key3 = "qrstuvwx"       # K3
#
#ciphertext = triple_des_encrypt(plaintext, key1, key2, key3)
#print("Chiffré (3DES) :", ciphertext)
#
#decrypted_text = triple_des_decrypt(ciphertext, key1, key2, key3)
#print("Déchiffré :", decrypted_text)

#crypt_all(triple_des_encrypt_full, key1, key2, key3, "benoit.txt", "benoitout.txt")
#crypt_all(triple_des_decrypt_full, key1, key2, key3, "benoitout.txt", "benoitout.txt")
