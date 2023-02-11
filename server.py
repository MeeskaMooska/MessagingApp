import socket
import threading

HOST = "0.0.0.0"
PORT = 80

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
            if message.decode('utf-8') == "quit":
                break

            else:
                broadcast(message)

        except:
            client_index = clients.index(client)
            clients.remove(client_index)
            client.close()
            usernames.remove(client_index)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connection from {address}.")

        # change below
        client.send(b"USER")
        username = client.recv(1024)

        clients.append(client)
        usernames.append(username)

        broadcast(f"{username.decode('utf-8')} connected.\n".encode('utf-8'))
        client.send("You are now connected.\n".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Starting server.")
receive()
