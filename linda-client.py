"""Cliente Linda

Comunicação entre cliente e servidor utilizando métodos 
do Linda e sockets. O cliente envia requisições em loop para o
servidor e recebe respostas. O loop se encerra como comando
fechar. Realiza os comandos de operação Linda.
"""
import socket

def client_program():
    host = "192.168.15.7"  
    porta = 5000  

    client_socket = socket.socket()  
    # Se conecta ao servidor
    client_socket.connect((host, porta))  

    # Leitura de dados de entrada
    message = input(" -> ")  

    while message.lower().strip() != 'fechar':
        # Envia uma mensagem
        client_socket.send(message.encode())  

        # Recebe a resposta do servidor
        dados= client_socket.recv(1024).decode()  

        # Exibe no terminal
        print('Recebido do servidor: ' + dados)

        # Nova leitura de dados
        message = input(" -> ")  
    
    # Fecha a conexão
    client_socket.close()  


if __name__ == '__main__':
    client_program()