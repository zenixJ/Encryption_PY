# Decoding - расшифровка 

from colorama import *
from pyfiglet import *
init()

title = figlet_format('Cesar - Decoding')
print(Fore.WHITE)
print(title)
print(Fore.GREEN)

step = 7

with open("file/finally.py") as file:

    text = file.read()

    ALPHA = "".join(map(chr, range(ord(" "), ord("я") + 1)))
    
    result_ = text.translate(str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))

    final__file = open('file/back.py', mode='w+', encoding='utf-8')
    final__file.write(result_)
    final__file.close()
