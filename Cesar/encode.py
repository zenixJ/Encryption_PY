# Encode - шифровка 

from colorama import *
from pyfiglet import *
init()

title = figlet_format('Cesar - Encode')
print(Fore.WHITE)
print(title)
print(Fore.GREEN)

step = 7

with open("file/origin.py") as file:

    text = file.read()

    ALPHA = "".join(map(chr, range(ord(" "), ord("я") + 1)))

    result_ = text.translate(str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))

    final__file = open('file/finally.py', mode='w+', encoding='utf-8')
    final__file.write(result_)
    final__file.close()