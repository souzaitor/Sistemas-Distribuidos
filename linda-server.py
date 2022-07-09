"""Servidor Linda

Comunicação entre cliente e servidor utilizando métodos 
do Linda e sockets. O servidor aguarda uma solicitação
de um cliente em um loop e responde a cada vez com uma resposta. 
Realiza os comandos de operação Linda.
"""

import socket
import linda
from _thread import *
import threading

print_lock = threading.Lock()

space = linda.Linda()

def threaded(c):
    while True:

        # Dados recebidos do cliente
        dados = c.recv(1024).decode()
        dados = dados.split()

        # Realiza as operações Linda
        if (dados[0] == "rd"):
            mensagem = space._rd(dados[1])
            
        elif (dados[0] == "in"):
            s = ' '
            mensagem = space._in(dados[1], dados[2], s.join(dados[3:dados.__len__()]))

        elif (dados[0] == "out"):
            s = ' '
            mensagem = space._out(dados[1], dados[2], s.join(dados[3:dados.__len__()]))

        # Envia a mensagem de volta
        c.send(mensagem.encode())
        
    # Fecha a conexão
    c.close()

def server_program():
    host = "192.168.15.7"
    porta = 5000 
    print("Servidor aberto em %s:%d" % (host, porta))

    server_socket = socket.socket() 

    # Realiza um bind do endereço ip e portaa
    server_socket.bind((host, porta)) 

    # Aceita nova conexão 
    server_socket.listen(5)  
    while True:

        # Recebe fluxo de dados. Não aceitar pacotes de dados maiores que 1024 bytes
        conn, endereco = server_socket.accept()
        print("Connection from: " + str(endereco))

        # Cria uma thread
        start_new_thread(threaded, (conn,))

    # Fecha a conexão
    conn.close()  


if __name__ == '__main__':
    server_program()