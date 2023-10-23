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

## Funcionamento geral

+ O cliente conecta-se com a calculadora, o servidor, por um token;
+ Uma vez autenticado, o cliente pode realizar a operação desejada e a calculadora enviará a resposta pelo terminal;
+ Mensageiro também recebe a resposta através de uma fila de mensagens e exibirá os LEDs correspondentes, nesse caso com prints;
+ Caso o Arduíno esteja conectado, ele exibirá a resposta recebida do mensageiro em seus LEDs;
+ Enquanto a mensagem não terminar de ser exibida, o cliente não poderá fazer novas operações.

## Como rodar

### Para rodar com o mensageiro (sem arduíno)

Primeiro deve-se rodar o servidor, o mensageiro e o cliente em terminais (ou máquinas) separados. No caso de máquinas, 
deve-se especificar no código o adress e o host correspondente.

Abra a pasta do projeto e em seguida a pasta src para todos:

`$ cd Distriduino/src`

Em seguida, rode em cada um dos terminais/máquinas o código correspondente, como a seguir:

`$ python3 servidor.py`

`$ python3 mensageiro.py`

`$ python3 cliente.py`

O servidor solicitará um token do cliente para a autenticação, o qual é '123456' e pode ser facilmente alterado no servidor, caso haja necessidade. 
O cliente deve inserir esse token no input solicitado pelo terminal. 

Uma vez validado, o cliente pode realizar suas operações, de acordo com o que a calculadora disponibilizou e com o exemplo printado. 

`101011 + 101100`

O resultado será calculado e enviado via socket para ser printado no terminal do cliente, mas também será enviado para o mensageiro para o print via "LEDs".
O mensageiro receberá pela fila de mensagens "fila", feita com RabbitMQ, e printará os LEDs como um arduíno o faria. 

Enquanto o mensageiro não termina de exibir a mensagem, nenhuma operação poderá ser feita pelo cliente. Quando terminar, o servidor receberá o aviso 
via fila de mensagens e liberará o cliente para novas operações.

Caso não haja novas operações, é só escrever um "q" no terminal ou fechar com Ctrl+C.

### Para rodar com o arduíno

Primeiro conecta-se o arduíno no computador como o daria normalmente pela ide do arduíno e especificar a porta na linha 13 do código arduino.py.
Caso o arduíno não seja do tipo UNO, deve-se especificar isso também pela classe. Exemplo:

`board = pyfirmata.ArduinoMega('/dev/ttyACM0')`

Assim como no tópico anterior, deve-se rodar o servidor, o arduíno e o cliente em terminais (ou máquinas) separados. No caso de máquinas, 
deve-se especificar no código o adress e o host correspondente.

Abra a pasta do projeto e em seguida a pasta src para todos:

`$ cd Distriduino/src`

Em seguida, rode em cada um dos terminais/máquinas o código correspondente, como a seguir:

`$ python3 servidor.py`

`$ python3 arduino.py`

`$ python3 cliente.py`

O servidor solicitará um token do cliente para a autenticação, o qual é '123456' e pode ser facilmente alterado no servidor, caso haja necessidade. 
O cliente deve inserir esse token no input solicitado pelo terminal. 

Uma vez validado, o cliente pode realizar suas operações, de acordo com o que a calculadora disponibilizou e com o exemplo printado. 

`101011 + 101100`

O resultado será calculado e enviado via socket para ser printado no terminal do cliente, mas também será enviado para o arduino para o print via LED.
O arduino receberá pela fila de mensagens "fila", feita com RabbitMQ, e piscará os LEDs de acordo com o resultado binário.

Enquanto o arduino não termina de exibir a mensagem, nenhuma operação poderá ser feita pelo cliente. Quando terminar, o servidor receberá o aviso 
via fila de mensagens e liberará o cliente para novas operações.

Caso não haja novas operações, é só escrever um "q" no terminal ou fechar com Ctrl+C.

## Referências e/ou Materiais de apoio

+ [Real Python - Sockets](https://realpython.com/python-sockets/);
+ [Docs Python - Socket](https://docs.python.org/3/library/socket.html);
+ [GeeksforGeeks - Simple calculator in python socket programming](https://www.geeksforgeeks.org/simple-calculator-in-python-socket-programming/);
+ [RabbitMQ - Tutorial one Python](https://www.rabbitmq.com/tutorials/tutorial-one-python.html);
+ [Microsoft Azure - Throttling](https://learn.microsoft.com/pt-br/azure/architecture/patterns/throttling);
+ [Microsoft Azure - Valet Key](https://learn.microsoft.com/pt-br/azure/architecture/patterns/valet-key);
+ [EE-Diary - LED blink with arduino using pyfirmata](https://www.ee-diary.com/2023/05/led-blink-with-arduino-using-pyfirmata.html).