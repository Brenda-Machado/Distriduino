"""

Arduino da aplicação Distriduino, 
desenvolvida na disciplina de Computação Distribuída, 2023.2.
Brenda Silva Machado

"""

import pyfirmata
import time
import pika, sys, os

board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[0].enable_reporting()

board.digital[13].mode = pyfirmata.OUTPUT

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila')

    def callback(ch, method, properties, body):
        if body.decode() == "fim":
            channel.stop_consuming()
            return 0
        else:
            # Simulação do arduíno
            resultado = body.decode()
            for i in range(0, len(resultado)):
                if resultado[i] == '1':
                    print('Ligando LED')
                    board.digital[13].write(1)
                elif resultado[i] == '0':
                    print('Desligando LED')
                    board.digital[13].write(0)
                time.sleep(5)
            print('Fim da operação\n')
            channel.basic_publish(exchange='',
                            routing_key='fila',
                            body='fim da operação')
        
    channel.basic_consume(queue='fila', on_message_callback=callback, auto_ack=True)

    print('Esperando resultado da operação...\n')
    channel.start_consuming()

while True:
    board.digital[13].write(0)
    time.sleep(3)
    board.digital[13].write(1)
    main()
