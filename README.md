# Distriduino

Trabalho da disciplina de Computação Distribuída (INE5418).

## Objetivo

Criar uma aplicação distribuída que utilize pelo menos dois dos padrões de projeto definidos por [Microsoft Azure](https://learn.microsoft.com/pt-br/azure/architecture/patterns/).

Além disso, deve conter um dos seguintes conteúdos da disciplina: 

+ RMI/RPC; 
+ Web services; 
+ Serviços de fila de mensagens;
+ Espaço de tuplas.

## Ideia

Calculadora binária com sinalização da resposta através dos LEDs de um arduíno. 

## Funcionamento geral:

+ O cliente conecta-se com a calculadora, o servidor, por um token;
+ Uma vez autenticado, o cliente pode realizar a operação desejada e a calculadora enviará a resposta pelo terminal;
+ Mensageiro também recebe a resposta através de uma fila de mensagens e exibirá os LEDs correspondentes, nesse caso com prints;
+ Caso o Arduíno esteja conectado, ele exibirá a resposta recebida do mensageiro em seus LEDs;
+ Enquanto a mensagem não terminar de ser exibida, o cliente não poderá fazer novas operações.

## Referências e/ou Materiais de apoio

+ [Real Python - Sockets](https://realpython.com/python-sockets/);
+ [Docs Python - Socket](https://docs.python.org/3/library/socket.html);
+ [GeeksforGeeks - Simple calculator in python socket programming](https://www.geeksforgeeks.org/simple-calculator-in-python-socket-programming/);
+ [RabbitMQ - Tutorial one Python](https://www.rabbitmq.com/tutorials/tutorial-one-python.html);
+ [Microsoft Azure - Throttling](https://learn.microsoft.com/pt-br/azure/architecture/patterns/throttling);
+ [Microsoft Azure - Valet Key](https://learn.microsoft.com/pt-br/azure/architecture/patterns/valet-key);
+ [EE-Diary - LED blink with arduino using pyfirmata](https://www.ee-diary.com/2023/05/led-blink-with-arduino-using-pyfirmata.html).