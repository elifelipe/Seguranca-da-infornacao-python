#  este codigo verifica o ip ou host de um determinado site da web

import os

print('#' * 40)

ip_ou_host = input("Digite o Ip ou Host a ser verificado: ")

print('-' * 40)

os.system('ping -n 6 {}'.format(ip_ou_host))

print('-' * 40)