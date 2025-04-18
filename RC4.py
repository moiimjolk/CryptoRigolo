def rc4_key_schedule(key):
    state = list(range(256))
    j = 0
    for i in range(256):
        j = (j + state[i] + key[i % len(key)]) % 256
        state[i], state[j] = state[j], state[i]
    return state

def rc4_prga(state):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        k = state[(state[i] + state[j]) % 256]
        yield k

def rc4_encrypt_decrypt(key, data):
    if isinstance(key, str):
        key = key.encode()
    
    state = rc4_key_schedule(key)
    
    keystream = rc4_prga(state)
    
    return bytes([byte ^ next(keystream) for byte in data])

#theses functions are here to allow the interface to work
def crypt(data, key):
    return

def decrypt(data, key):
    return

def crypt_all(input_file, key, output_file, function): 
    with open(input_file, 'rb') as f:
        data = f.read()
    
    result = rc4_encrypt_decrypt(key, data)
    
    with open(output_file, 'wb') as f:
        f.write(result)



# test comme d'hab
#key = b"Benoit"
#plaintext = b"Mon amour"
#
#ciphertext = rc4_encrypt_decrypt(key, plaintext)
#print("Encryp :", ciphertext)
#
#decrypted = rc4_encrypt_decrypt(key, ciphertext)
#print("Decryp :", decrypted.decode())


#crypt_all(key, "benoit.txt", "benoitout.txt")
#crypt_all(key, "benoitout.txt", "benoitout.txt")
