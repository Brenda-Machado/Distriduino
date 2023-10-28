"""

Arduino da aplicação Distriduino, 
desenvolvida na disciplina de Computação Distribuída, 2023.2.
Brenda Silva Machado

"""

import pyfirmata
import time
import pika, sys, os

board = pyfirmata.Arduino('/dev/ttyACM0')

led = board.get_pin('d:13:o')

# Inicializa o LED
board.digital[13].mode = pyfirmata.OUTPUT

led.write(0)

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
                    led.write(1)
                elif resultado[i] == '0':
                    print('Desligando LED')
                    led.write(0)
                time.sleep(3)
            print('Fim da operação\n')
            channel.basic_publish(exchange='',
                            routing_key='fila',
                            body='fim da operação')
            led.write(0)
        
    channel.basic_consume(queue='fila', on_message_callback=callback, auto_ack=True)

    print('Esperando resultado da operação...\n')
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