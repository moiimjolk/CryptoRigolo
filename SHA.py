import hashlib

def sha1_hash(data):
    return hashlib.sha1(data.encode('utf-8')).hexdigest()

def sha256_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def sha512_hash(data):
    return hashlib.sha512(data.encode('utf-8')).hexdigest()



def hashing(text, algo):
    return algo(text)
# test
#data = "Benito mon gros homme"
#print("SHA-1 :", sha1_hash(data))
#print("SHA-256 :", sha256_hash(data))
#print("SHA-512 :", sha512_hash(data))
#
#crypt_all(sha512_hash, "benoit.txt", "benoitout.txt")
