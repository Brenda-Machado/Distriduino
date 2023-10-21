"""

Cliente da aplicação Distriduino, 
desenvolvida na disciplina de Computação Distribuída, 2023.2.
Brenda Silva Machado

"""


import socket

HOST = "127.0.0.1"  # O hostname ou endereço IP do servidor
PORT = 65432  # A porta usada pelo servidor

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

# Autenticação do cliente

token = input("Insira o token de acesso: ")
client.send(token.encode())
autenticado = client.recv(1024)

if autenticado.decode() == "0":
    print("Token inválido")
    client.close()
    exit()
else:
    print("Token válido")
    while True:
        print("Exemplo de operação : 110 + 101")
        print("Operações disponíveis : + e -")

        inp = input("Insira os números binários e a operação segundo o exemplo ou digite 'q' para sair: ")

        if inp == "q":
            break

        client.send(inp.encode())

        answer = client.recv(1024)

        print("Resultado "+answer.decode())

        print("Aguardando liberação do mensageiro...")

        answer = client.recv(1024)

        print("Pode realizar nova operação")

        print("\n")


    
    client.close()


