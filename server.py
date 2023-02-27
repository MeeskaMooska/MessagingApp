import errno
import socket
import threading
from cryptography.fernet import Fernet
# Handshake code = 75RJM202y299U8a34fYGjojPAlP3nfzb

class ServerData:
    def __init__(self):
        self.self = self
        self.running = True

HOST = "0.0.0.0"
PORT = 80
# This is not very secure but as this is simply to prevent other devices on the network from sniffing packets,
#   it doesn't need to be extremely secure
encryption_key = b'e9iRDX8f-2GiHwWi_toavUnscTwWz6AwVwdAf53y6wY='

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
usernames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if fernet.decrypt(message).decode('utf-8') == 'quit':
                break

            else:
                broadcast(message)

        except ConnectionResetError:
            client_index = clients.index(client)
            usernames.pop(client_index)
            clients.pop(client_index)
            client.close()
            break

        except ConnectionAbortedError:
            break






def receive():
    while True:
        try:
            client, address = server.accept()
            print(f"Connection from {address}.")

            # change below
            client.send(fernet.encrypt('75RJM202y299U8a34fYGjojPAlP3nfzb'.encode()))
            username = client.recv(1024)

            clients.append(client)
            usernames.append(username)

            broadcast(fernet.encrypt(f"{username.decode('utf-8')} connected.\n".encode()))
            client.send(fernet.encrypt(('o2rWLN8eduep9O6cUfrmBEKF1jh8LOpB'.encode())))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

        except OSError as e:
            if e.errno == errno.ENOTSOCK:
                break


def terminate_connections():
    for client in clients:
        client.close()

    clients.clear()
    usernames.clear()


def server_control_terminal():
    command = input()
    if command == 'terminate':
        print('Closing Server...')
        server.close()
        terminate_connections()

    elif command == 'list':
        print(f"Usernames: {usernames}\nConnected Clients: {clients}")
        server_control_terminal()

    else:
        print("Unknown command.")
        server_control_terminal()


print("Starting server.")
t1 = threading.Thread(target=server_control_terminal)
t1.start()
server_data = ServerData()
fernet = Fernet(encryption_key)
receive()
