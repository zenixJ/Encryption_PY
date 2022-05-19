# Decoding - расшифровка 

import rsa
(pubkey, privkey) = rsa.newkeys(512)

from colorama import *
from pyfiglet import *
init()

title = figlet_format('RSA - Decoding')
print(Fore.WHITE)
print(title)
print(Fore.GREEN)

with open("file/origin.py") as file:

    text = file.read()

    message = bytes(text, encoding='utf8')

    crypto = rsa.encrypt(message, pubkey)

with open("file/finally.xml", "r", encoding='latin-1') as file:

    text = file.read()

    message = bytes(text, encoding='utf8')

    crypto = rsa.decrypt(crypto, privkey)

    final__file = open('file/back.py', mode='wb')
    final__file.write(crypto)
    final__file.close()