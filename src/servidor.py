"""

Servidor da aplicação Distriduino, 
desenvolvida na disciplina de Computação Distribuída, 2023.2.
Brenda Silva Machado

"""


import socket

HOST = "127.0.0.1"  # localhost
PORT = 65432  # Porta para o listen

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(1)

print("Calculadora iniciou")
print("Esperando pela operacao..")

clientConnection, clientAddress = server.accept()
print("Cliente conectado :", clientAddress)
msg = ''

while True:
    data = clientConnection.recv(1024)
    msg = data.decode()
    if msg == 'q':
        print("Conexao encerrada pelo cliente")
        break
 
    result = 0
    operation_list = msg.split()
    oprnd1 = operation_list[0]
    operation = operation_list[1]
    oprnd2 = operation_list[2]
 
    # Conversao de string para int
    num1 = (int(oprnd1, 2))
    num2 = (int(oprnd2, 2))

    # Operacoes básicas
    if operation == "+":
        result = bin(num1 + num2)
    elif operation == "-":
        result = bin(num1 - num2)
 
    # Conversao para string
    # Envio para o cliente
    output = str(result[2:])
    clientConnection.send(output.encode())
clientConnection.close()