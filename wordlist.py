import itertools

def calculatePasswords():
    possibleChars = input("[*] List all characters: ")
    passwordLength = input("[*] Enter length of password: ")
    file = open("wordlists/wordlist_2_all.txt", "a") # appends to the open file

    letters = itertools.product(possibleChars, repeat=int(passwordLength))
    print("[*] Generating passwords, this might take a while...")

    for i in letters:
        file.write("".join(i)+'\n')
    file.close()


calculatePasswords()