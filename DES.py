# j'ai choisis les tables officielle du DES du coup le début est un peu long...

IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

IP_INV = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

P = [
    16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25
]

PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

SHIFT_SCHEDULE = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

S_BOX = [
    # S1 à S8
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]


def str_to_bitlist(data):
    bitlist = []
    for byte in data.encode('latin-1'):  # ça convertis chaque cara dans sa version binaire
        for bit in f"{byte:08b}": bitlist.append(int(bit))
    return bitlist

def bitlist_to_str(bits):
    result = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        result.append(chr(int(''.join(map(str, byte)), 2)))
    return ''.join(result)

def permute(block, table):
    print(block)
    permuted_block = []
    for i in table:
        permuted_block.append(block[i-1])
    return permuted_block

def shift_left(key, shifts):
    return key[shifts:] + key[:shifts]

def xor(bits1, bits2):
    result = []
    for b1, b2 in zip(bits1, bits2):
        result.append(b1 ^ b2)
    return result

def sbox_substitution(bits):
    result = []
    for i in range(8):
        block = bits[i * 6:(i + 1) * 6]
        row = (block[0] << 1) | block[5]
        col = (block[1] << 3) | (block[2] << 2) | (block[3] << 1) | block[4]
        val = S_BOX[i][row][col]
        result += [int(b) for b in format(val, '04b')]
    return result

def generate_keys(key_64bits):
    key = permute(key_64bits, PC1)
    C, D = key[:28], key[28:]
    keys = []

    for shift in SHIFT_SCHEDULE:
        C, D = shift_left(C, shift), shift_left(D, shift)
        combined = C + D
        keys.append(permute(combined, PC2))

    return keys


def feistel(right, subkey):
    expanded = permute(right, E)
    xored = xor(expanded, subkey)
    sboxed = sbox_substitution(xored)
    return permute(sboxed, P)


def des_block(block_64bits, keys, decrypt=False):
    block = permute(block_64bits, IP)
    L, R = block[:32], block[32:]

    for i in range(16):
        round_key = keys[15 - i] if decrypt else keys[i]
        L, R = R, xor(L, feistel(R, round_key))

    return permute(R + L, IP_INV)


def des_encrypt(text8, key8):
    block_bits = str_to_bitlist(text8)
    key_bits = str_to_bitlist(key8)
    subkeys = generate_keys(key_bits)
    encrypted_bits = des_block(block_bits, subkeys)
    return ''.join(format(b, '01b') for b in encrypted_bits)

def des_decrypt(cipher_bits, key8):
    key_bits = str_to_bitlist(key8)
    subkeys = generate_keys(key_bits)
    cipher_bits = [int(b) for b in cipher_bits]
    decrypted_bits = des_block(cipher_bits, subkeys, decrypt=True)
    return bitlist_to_str(decrypted_bits)

# pour montrer comment il fonctionne, les inputs doivent respecter une taille
# oui les inputs doivent être parfaitement 8 octets, ou 64 bits pour être précis (8 caractères)
# si on utilise les algo de base, voici une version amélioré pour n'importe quel taille :

def pad_data(data):
    pad_length = 8 - (len(data) % 8)
    padding = bytes([pad_length]) * pad_length
    return data.encode('latin-1') + padding if isinstance(data, str) else data + padding

def unpad_data(data):
    if not data:
        return data
    
    pad_length = data[-1]
    
    if pad_length > 8:
        return data
    
    for i in range(1, pad_length + 1):
        if data[-i] != pad_length:
            return data
    
    return data[:-pad_length]

def crypt(plaintext, key):
    padded_data = pad_data(plaintext)
    
    result = ""
    for i in range(0, len(padded_data), 8):
        block = padded_data[i:i+8]
        if isinstance(block, bytes):
            block = block.decode('latin-1')
        encrypted_block = des_encrypt(block, key)
        result += encrypted_block
    
    return result

def decrypt(ciphertext, key):
    result = b""
    for i in range(0, len(ciphertext), 64):
        block = ciphertext[i:i+64]
        decrypted_block = des_decrypt(block, key)
        result += decrypted_block.encode('latin-1')
    
    unpadded_data = unpad_data(result)
    
    try:
        return unpadded_data.decode('latin-1')
    except:
        return unpadded_data

def crypt_all(input_file, key, output_file, operation):
    if operation == crypt:
        try:
            with open(input_file, 'r') as f:
                data = f.read()
                print(data)
        except UnicodeDecodeError:
            with open(input_file, 'rb') as f:
                data = f.read()

        result = operation(data, key)
        
        with open(output_file, 'w') as f:
            f.write(result)
    
    elif operation == decrypt:
        with open(input_file, 'r') as f:
            cipher_bits = f.read()
        
        result = operation(cipher_bits, key)
        
        if isinstance(result, str):
            with open(output_file, 'w') as f:
                f.write(result)
        else:
            with open(output_file, 'wb') as f:
                f.write(result)

