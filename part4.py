import hashlib

def md5_100times(passedInHash):
    i = 0
    hash = ""
    print("<==========MD5 Hash==========>")
    while i < 5:
        if i == 0:
            hash = hashlib.md5(passedInHash.encode())
            print("{} hash: {}".format(i+1, hash.hexdigest()))
        else:
            hash = hashlib.md5(hash.hexdigest().encode())
            print("{} hashes: {}".format(i+1, hash.hexdigest()))
        i += 1
    print('\n')
    return hash.hexdigest()

def sha256_100times(passedInHash):
    i = 0
    hash = ""
    print("<==========SHA256 Hash==========>")
    while i < 5:
        if i == 0:
            hash = hashlib.sha256(passedInHash.encode())
            print("{} hash: {}".format(i+1, hash.hexdigest()))
        else:
            hash = hashlib.sha256(hash.hexdigest().encode())
            print("{} hashes: {}".format(i+1, hash.hexdigest()))
        i += 1
    print('\n')
    return hash.hexdigest()

def sha512_100times(passedInHash):
    i = 0
    hash = ""
    print("<==========SHA512 Hash==========>")
    while i < 5:
        if i == 0:
            hash = hashlib.sha512(passedInHash.encode())
            print("{} hash: {}".format(i+1, hash.hexdigest()))
        else:
            hash = hashlib.sha512(hash.hexdigest().encode())
            print("{} hashes: {}".format(i+1, hash.hexdigest()))
        i += 1 
    print('\n')
    return hash.hexdigest()

# test = open("wordlist5chars.txt", "r")
# passwordToTry = test.readline()
# passwordToTry = passwordToTry.rstrip()


myHash = md5_100times("aaaaa")
myHash = sha256_100times(myHash)
myHash = sha512_100times(myHash)
# myHash = myHash.decode()
print("Result: {}".format(myHash))

