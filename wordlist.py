import itertools

def calculatePasswords():
    possibleChars = input("[*] List all characters: ")
    passwordLength = input("[*] Enter length of password: ")
    file = open("wordlist5chars.txt", "a") # appends to the open file

    letters = itertools.product(possibleChars, repeat=int(passwordLength))
    print("[*] Generating passwords, this might take a while...")

    for i in letters:
        file.write("".join(i)+'\n')
    file.close()


calculatePasswords()