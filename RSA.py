import random

#j'aurai pu utiliser math mais vsy pour le PGCD mais j'ai réalisé trop tard
def gcd(a, b):
    while b != 0: a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# On remercie Miller-Rabin de crée les algo de chiffre premier sinon j'aurai galéré
def is_prime(n, k=5):
    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0: return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def generate_prime(bits=1024):
    while True:
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1  # juste il assure que p est impair
        if is_prime(p): return p

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p: q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, phi) != 1: e = random.randint(2, phi - 1)

    d = modinv(e, phi)
    return (e, n), (d, n)

def crypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher])
    return message


def crypt_all(input_file, public_key, private_key, output_file, operation):
    
    if operation == crypt:
        public_key, private_key = generate_keys()
        with open(input_file, 'r') as f:
            data = f.read()
        
        result = operation(data, public_key)
        
        with open(output_file, 'w') as out_f:
            for num in result:
                out_f.write(f"{num}\n")
                
    elif operation == decrypt:
        private_key=tuple(private_key)
        with open(input_file, 'r') as f:
            encrypted_data = [int(line.strip()) for line in f if line.strip()]
        
        result = operation(encrypted_data, private_key)
        
        with open(output_file, 'w') as out_f:
            out_f.write(result)

          
    else:
        raise ValueError("Operation must be the encrypt or decrypt function")

