"""

Servidor da aplicação Distriduino, 
desenvolvida na disciplina de Computação Distribuída, 2023.2.
Brenda Silva Machado

"""


import socket
import pika

HOST = "127.0.0.1"  # localhost
PORT = 65432  # Porta para o listen

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind((HOST, PORT))

connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
channel = connection.channel()
channel.queue_declare(queue='fila')

server.listen(1)

print("Calculadora iniciou")
print("Esperando pela operacao..")

clientConnection, clientAddress = server.accept()
print("Cliente conectado :", clientAddress)
msg = ''

def callback(ch, method, properties, body):
    while True:
        if body.decode() == "fim da operação":
            break
    print("Mensagem terminou de ser exibida no mensageiro")
    channel.stop_consuming()
    return 0

# Recebimento da autenticação
token = clientConnection.recv(1024)
if token.decode() == "123456":
    clientConnection.send("1".encode())
    while True:
        data = clientConnection.recv(1024)
        msg = data.decode()
        if msg == 'q':
            print("Conexao encerrada pelo cliente")
            channel.basic_publish(exchange='',
                        routing_key='fila',
                        body='fim')
            break
        
        else:
    
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
            channel.basic_publish(exchange='',
                            routing_key='fila',
                            body=output)
            clientConnection.send(output.encode())
            print("Resultado enviado para o mensageiro")

            # Limitação: esperar a confirmação que o mensageiro exibiu a mensagem antes de uma nova operação
            # Recebimento da confirmação
            channel.basic_consume(queue='fila', on_message_callback=callback, auto_ack=True)

            channel.start_consuming()

            clientConnection.send("Mensageiro finalizou, pode iniciar nova operação".encode())

    clientConnection.close()

    # Destruir a fila
    channel.queue_delete(queue='fila')
else:
    clientConnection.send("0".encode())
    clientConnection.close()
    exit()
