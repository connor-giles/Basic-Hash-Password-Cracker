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

file = open("wordlists/wordlist_1_lower.txt", "r")
hashToMatch = "26dc10ac450277126e64aca39c6e7f300f37b0b18693b49a3b648b801287e9a08f483ff9130e7157ccf2220047254130ebf4155f0e5e4248ef7a3eb528f69bb5"

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



