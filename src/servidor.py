"""

Servidor da aplicação Distriduino, 
desenvolvida na disciplina de Computação Distribuída, 2023.2.
Brenda Silva Machado

"""


import socket

HOST = "127.0.0.1"  # localhost
PORT = 65432  # Porta para o listen

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)