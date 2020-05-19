from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

HOST = '127.0.0.1'
PORT = 12000
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def send(event=None):
    check = 0;
    print ("Start commanding the terminal, \n[ENTER ls TO START SENDING, shutup TO STOP]")
    while (check == 0):
        command = input()
        client_socket.send(bytes(command,"utf8"))
        if (command == "shutup"):
            check = 1

send()
