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

Funcionamento geral:

+ O cliente conecta-se com a calculadora, o servidor, por um token;
+ Uma vez autenticado, o cliente pode realizar a operação desejada e a calculadora enviará a resposta pelo terminal;
+ Mensageiro também recebe a resposta através de uma fila de mensagens e exibirá os LEDs correspondentes, nesse caso com prints;
+ Caso o Arduíno esteja conectado, ele exibirá a resposta recebida do mensageiro em seus LEDs.

## Referências e/ou Materiais de apoio

+ [Real Python](https://realpython.com/python-sockets/);
+ [Docs Python](https://docs.python.org/3/library/socket.html);
+ [GeeksforGeeks](https://www.geeksforgeeks.org/simple-calculator-in-python-socket-programming/);
+ [RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-one-python.html);
+ [Padrão Limitação](https://learn.microsoft.com/pt-br/azure/architecture/patterns/throttling);
+ [Padrão Valet Key](https://learn.microsoft.com/pt-br/azure/architecture/patterns/valet-key).