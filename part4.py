import hashlib

def md5_100times(passedInHash):
    i = 0
    hash = ""
    print("<==========MD5 Hash==========>")
    while i < 100:
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
    while i < 100:
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
    while i < 100:
        if i == 0:
            hash = hashlib.sha512(passedInHash.encode())
            print("{} hash: {}".format(i+1, hash.hexdigest()))
        else:
            hash = hashlib.sha512(hash.hexdigest().encode())
            print("{} hashes: {}".format(i+1, hash.hexdigest()))
        i += 1 
    print('\n')
    return hash.hexdigest()

def compareResult(result, compared):
    if compared == result:
        print("found password")
    else:
        print("did not find password")

file = open("wordlist5chars.txt", "r")
passwordToTry = file.readline()
passwordToTry = passwordToTry.rstrip()
hashToMatch = "122e6946f7641345e4ca3adab598d5a70284bf7e0065621361a868b18bc8f84d958053f0b59f831d8354539867edafc7ec35b8e6cb4cdfaa67843df0d0c42d50"

firstHash = md5_100times("butler")
secondHash = sha256_100times(firstHash)
result = sha512_100times(secondHash)
compareResult(result, hashToMatch)


