"""

Cliente da aplicação Distriduino, 
desenvolvida na disciplina de Computação Distribuída, 2023.2.
Brenda Silva Machado

"""


import socket

HOST = "127.0.0.1"  # O hostname ou endereço IP do servidor
PORT = 65432  # A porta usada pelo servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Testando a conexao")
    data = s.recv(1024)

print(f"Received {data!r}")


