'''
Crie um código em Python que teste se o site Pudim está acessível
pelo computador usado.
'''

import requests

try:
    r = requests.get('http://pudim.com')
except:
    print('\n\033[1;31mO site pudim não está acessível!\033[m\n')
else:
    print('\n\033[1;32mO site pudim está acessível\033[m\n')
