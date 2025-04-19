from SHA import *

# test
data = "Benito mon gros homme"
print("SHA-1 :", sha1_hash(data))
print("SHA-256 :", sha256_hash(data))
print("SHA-512 :", sha512_hash(data))

hashing(sha512_hash, data)
