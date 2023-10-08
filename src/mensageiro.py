import pika, sys, os
from time import sleep

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila')

    def callback(ch, method, properties, body):
        # Simulação do arduíno
        resultado = body.decode()
        for i in range(0, len(resultado)):
            if resultado[i] == '1':
                print('Ligando LED')
                sleep(0.5)
            else:
                print('Desligando LED')
                sleep(0.5)

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