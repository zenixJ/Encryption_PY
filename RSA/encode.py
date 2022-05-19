# Encode - шифровка 

import rsa
(pubkey, privkey) = rsa.newkeys(512)

from colorama import *
from pyfiglet import *
init()

title = figlet_format('RSA - Encode')
print(Fore.WHITE)
print(title)
print(Fore.GREEN)

with open("file/origin.py") as file:

    text = file.read()

    message = bytes(text, encoding='utf8')

    crypto = rsa.encrypt(message, pubkey)

    final__file = open('file/finally.xml', mode='wb')
    final__file.write(crypto)
    final__file.close()



