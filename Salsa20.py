def left_rotate(x, n):
    return ((x << n) & 0xFFFFFFFF) | (x >> (32 - n))

def salsa20_quarter_round(a, b, c, d):
    a = (a + b) & 0xFFFFFFFF
    d = left_rotate(d ^ a, 16)
    c = (c + d) & 0xFFFFFFFF
    b = left_rotate(b ^ c, 12)
    a = (a + b) & 0xFFFFFFFF
    d = left_rotate(d ^ a, 8)
    c = (c + d) & 0xFFFFFFFF
    b = left_rotate(b ^ c, 7)
    return a, b, c, d

def salsa20_block(key, nonce, counter=0):
    state = [
        0x61707865, 0x3320646E, 0x79622D32, 0x6B206574,
        int.from_bytes(key[0:4], byteorder='little'),
        int.from_bytes(key[4:8], byteorder='little'),
        int.from_bytes(key[8:12], byteorder='little'),
        int.from_bytes(key[12:16], byteorder='little'),
        int.from_bytes(key[16:20], byteorder='little'),
        int.from_bytes(key[20:24], byteorder='little'),
        int.from_bytes(key[24:28], byteorder='little'),
        int.from_bytes(key[28:32], byteorder='little'),
        int.from_bytes(nonce[0:4], byteorder='little'),
        int.from_bytes(nonce[4:8], byteorder='little'),
        counter, 0
    ]


    state = salsa20_round(state)

    keystream = []
    for i in range(16):
        keystream.extend(state[i].to_bytes(4, byteorder='little'))

    return keystream

def salsa20_round(state):
    for _ in range(20):
        for i in 0, 4, 8, 12:
            a, b, c, d = i, i + 1, i + 2, i + 3
            state[a], state[b], state[c], state[d] = salsa20_quarter_round(state[a], state[b], state[c], state[d])

        for i in 0, 1, 2, 3:
            a, b, c, d = i, (i+1)%4+4, (i+2)%4+8, (i+3)%4+12
            state[a], state[b], state[c], state[d] = salsa20_quarter_round(state[a], state[b], state[c], state[d])

    return state

def salsa20_encrypt_decrypt(key, nonce, data):
    keystream = salsa20_block(key, nonce)
    return bytes([data[i] ^ keystream[i] for i in range(len(data))])

def crypt_all(key, nonce, input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    result = salsa20_encrypt_decrypt(key, nonce, data)
    
    with open(output_file, 'wb') as f:
        f.write(result)

# test 
key = bytes([0x00] * 32)  # 256 bits
nonce = bytes([0x00] * 8)  # 64 bits

plaintext = b"test test test avec benoit mon homme"
ciphertext = salsa20_encrypt_decrypt(key, nonce, plaintext)

print("Encryp :", ciphertext)

decrypted = salsa20_encrypt_decrypt(key, nonce, ciphertext)
print("Decryp :", decrypted.decode('utf-8'))

#crypt_all(key, nonce, "benoit.txt", "benoitout.txt")
#crypt_all(key, nonce, "benoitout.txt", "benoitout.txt")
