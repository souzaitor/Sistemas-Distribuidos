"""Servidor Zero MQ 

Script criam um contexto ZeroMQ para trabalhar e um soquete.
O servidor vincula seu soquete REP (resposta) à porta 5555. 
O servidor aguarda uma solicitação em um loop e responde 
a cada vez com uma resposta. O script temina ao ler a string 
fechar, fechando o servidor e o cliente.
"""
import time
import zmq

#  Socket para se comunicar com o cliente
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Espera pela próxima requisição do cliente
    mensagem = socket.recv_string()
    print("Requisição recebida: %s" % mensagem)

    # Encera os programas se lê a string fechar
    if mensagem.lower().strip() == "fechar":
        socket.send_string("Servidor fechado")
        break

    
    time.sleep(1)
    
    #  Envia reposta para o cliente
    socket.send_string("Mensagem recebida")

print("Servidor fechado")
