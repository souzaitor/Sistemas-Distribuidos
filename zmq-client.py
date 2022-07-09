"""Cliente Zero MQ 

Script criam um contexto ZeroMQ para trabalhar e um soquete.
O cliente se conecta com o servidor 
O servidor vincula seu soquete REP (resposta) à porta 5555. 
O cliente lê em um loop várias strings e envia requisições
com os dados para o servidorl, lê também as respostas
do servidor. O script temina ao ler a string fechar,
fechando o servidor e o cliente.
"""
import zmq
context = zmq.Context()

#  Socket para se comunicar com o servidor
print("Conectando com o servidor ZMQ…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Ler mensagem de entrada
msg = input("-> ")

while msg.lower().strip() != 'fechar':
    print("Enviando requisição ao servidor")
    socket.send_string(msg)

    # Recebe resposta do servidor
    dados = socket.recv_string()  

    print('Recebido do servidor: ' + dados)  # Mostra no terminal

    msg = input("-> ")
        
print("Requisitando fechamento do servidor e fechando cliente")
socket.send_string(msg)