import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso")

host = 'localhost'
port = 5432

s.bind((host, port))
msg = '\nEu sou o servidor: olá cliente'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Servidor enviando msg..")
        s.sendto(dados + (msg.encode()), end)