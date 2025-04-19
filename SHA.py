import hashlib

def sha1_hash(data):
    return hashlib.sha1(data.encode('utf-8')).hexdigest()

def sha256_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def sha512_hash(data):
    return hashlib.sha512(data.encode('utf-8')).hexdigest()



def hashing(text, algo):
    return algo(text)
