import hashlib

def sha1_hash(data):
    return hashlib.sha1(data.encode('utf-8')).hexdigest()

def sha256_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def sha512_hash(data):
    return hashlib.sha512(data.encode('utf-8')).hexdigest()

def crypt_all(operation, input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()
    
    result = operation(data)
    
    with open(output_file, 'w') as f:
        f.write(result)

# test
data = "Benito mon gros homme"
print("SHA-1 :", sha1_hash(data))
print("SHA-256 :", sha256_hash(data))
print("SHA-512 :", sha512_hash(data))

#crypt_all(sha512_hash, "benoit.txt", "benoitout.txt")
