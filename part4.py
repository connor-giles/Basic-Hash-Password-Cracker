import hashlib

def md5_100times(passedInHash):
    i = 0
    hash = ""
    #print("<==========MD5 Hash==========>")
    while i < 100:
        if i == 0:
            hash = hashlib.md5(passedInHash.encode())
            #print("{} hash: {}".format(i+1, hash.hexdigest()))
        else:
            hash = hashlib.md5(hash.hexdigest().encode())
            #print("{} hashes: {}".format(i+1, hash.hexdigest()))
        i += 1
    #print('\n')
    return hash.hexdigest()

def sha256_100times(passedInHash):
    i = 0
    hash = ""
    #print("<==========SHA256 Hash==========>")
    while i < 100:
        if i == 0:
            hash = hashlib.sha256(passedInHash.encode())
            #print("{} hash: {}".format(i+1, hash.hexdigest()))
        else:
            hash = hashlib.sha256(hash.hexdigest().encode())
            #print("{} hashes: {}".format(i+1, hash.hexdigest()))
        i += 1
    #print('\n')
    return hash.hexdigest()

def sha512_100times(passedInHash):
    i = 0
    hash = ""
    #print("<==========SHA512 Hash==========>")
    while i < 100:
        if i == 0:
            hash = hashlib.sha512(passedInHash.encode())
            #print("{} hash: {}".format(i+1, hash.hexdigest()))
        else:
            hash = hashlib.sha512(hash.hexdigest().encode())
            #print("{} hashes: {}".format(i+1, hash.hexdigest()))
        i += 1 
    #print('\n')
    return hash.hexdigest()

file = open("wordlist5chars.txt", "r")
hashToMatch = "00e2033898f86764dd93117e426b76930c5e8ffa3da7b1e095815a1686a011b991dace2783449273552e1c9dbfdbbd9c8aa9d3ecba73b06861fbd88def11e4f0"

for i in range(pow(26,5)):
    passwordToTry = file.readline()
    passwordToTry = passwordToTry.rstrip()
    temp = passwordToTry

    firstHash = md5_100times(temp)
    secondHash = sha256_100times(firstHash)
    result = sha512_100times(secondHash)
    
    if result == hashToMatch:
        print("########## PASSWORD FOUND ########## ==========> {}".format(temp))
        break

    print("finished: {}".format(temp))



