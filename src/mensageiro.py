"""

Mensageiro da aplicação Distriduino, 
desenvolvida na disciplina de Computação Distribuída, 2023.2.
Brenda Silva Machado

"""


import pika, sys, os
from time import sleep

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
                    sleep(0.5)
                elif resultado[i] == '0':
                    print('Desligando LED')
                    sleep(0.5)
            print('Fim da operação \n')
            channel.basic_publish(exchange='',
                            routing_key='fila',
                            body='fim da operação')
        
    channel.basic_consume(queue='fila', on_message_callback=callback, auto_ack=True)

    print('Esperando resultado da operação...')
    channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrompido')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)