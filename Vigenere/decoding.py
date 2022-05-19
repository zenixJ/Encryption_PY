# Decoding - расшифровка 

from colorama import *
from pyfiglet import *
init()

title = figlet_format('Vigenere - Decoding')
print(Fore.WHITE)
print(title)
print(Fore.GREEN)

with open("file/finally.py") as file:

    text = file.read()

    let = str(text)
    key = 'PBEam'
    key *= len(let) // len(key) + 1
    key = key.upper()
    msg = ''

    for i, j in enumerate(let):
        save = j.upper()
        if (ord(j) in range(32, 65)):
            msg += j 
            continue
        x = ((ord(save) - ord(key[i])) % 26) + ord('A')

        if (j.islower()):
            msg += chr(x).lower()
        elif (j.isupper()):
            msg += chr(x).upper()
        else: 
            msg += chr(x)

    final__file = open('file/back.py', mode='w+', encoding='utf-8')
    final__file.write(msg)
    final__file.close()