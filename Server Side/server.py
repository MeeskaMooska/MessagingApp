import errno
import socket
import threading
from cryptography.fernet import Fernet
import json

# Using these variables makes the program much more understandable and easier to write.
handshake_code = '75RJM202y299U8a34fYGjojPAlP3nfzb'
successful_handshake_code = "o2rWLN8eduep9O6cUfrmBEKF1jh8LOpB"
general_chat_code = "3rIP4sf5VA6QC2oIYFiepjtb7HWp97SK"
personal_chat_code = 'F26RUPmRikmepuz4vdUkaSH4fHgWcMO3'
login_code = 'z7eLQzZ7gmnqx4C6JQML6nMpjP0Nc1Ex'
sign_up_code = 'ClyGibkmr9JBMo8CpFpMyLrfvXTxXbkV'

# Sign In/Up communication structure:
#   32b(communication id code) + 32b(user_id(8b), username(24b)) + 32b(password)

# Message communication structure:
#   Direct:
#   32b(communication id code) + 40b(recipient_uid(8b) + (sender_uid(8b) + sender_username(24b)) + 1000b(message)
#   Global
#   32b(communication id code) + 8b(sender_uid) + 1000b(message)


class ServerData:
    def __init__(self):
        self.self = self
        self.running = True


HOST = "0.0.0.0"
PORT = 80
# This is not very secure but as this is simply to prevent other devices on the network from sniffing packets,
#   it doesn't need to be extremely secure
# as I've expanded my horizons to have this use port forwarding in the future security will be paramount
encryption_key = b'e9iRDX8f-2GiHwWi_toavUnscTwWz6AwVwdAf53y6wY='

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
user_ids = []
usernames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(2024)
            if fernet.decrypt(message).decode('utf-8') == 'quit':
                break

            else:
                print(len(message))
                broadcast(message)

        except ConnectionResetError:
            client_index = clients.index(client)
            user_ids.pop(client_index)
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
            print(f"Connection attempt from {address}.")

            client.send(fernet.encrypt(handshake_code.encode()))
            communication = fernet.decrypt(client.recv(2024)).decode('utf-8')
            communication_identifier = communication[0:32]
            received_user_id, received_username, received_password = \
                communication[32:40], communication[40:64].strip('/'), communication[64:-1].strip('/')

            if communication_identifier == login_code:
                stored_user_info = collect_json_from_file('userdata.json')['users'][received_user_id]
                stored_username, stored_password = stored_user_info[0], stored_user_info[1]
                if (stored_username == received_username) & (stored_password == received_password):
                    clients.append(client)
                    # TODO change  to store user_ids to prevent multiple users getting confused.
                    user_ids.append(received_user_id)
                    usernames.append(received_username)

                    broadcast(fernet.encrypt(f"{received_username} connected.\n".encode()))
                    client.send(fernet.encrypt((successful_handshake_code.encode())))

                    thread = threading.Thread(target=handle, args=(client,))
                    thread.start()
                    
                else:
                    pass

            elif communication_identifier == sign_up_code:
                pass

            else:
                # I plan to handle this differently in the future but this is it for now.
                print('Possible security thread: terminating')
                break

        except OSError as e:
            if e.errno == errno.ENOTSOCK:
                break


def terminate_connections():
    for client in clients:
        client.close()

    clients.clear()
    user_ids.clear()
    usernames.clear()


def server_control_terminal():
    command = input()
    if command == 'terminate':
        print('Closing Server...')
        server.close()
        terminate_connections()

    elif command == 'list':
        print('%-12s %-28s %s' % ('User ID', 'Username', 'Address'))
        for i in range(len(clients)):
            print('%-12s %-28s %s' % (user_ids[i], usernames[i], clients[i]))
        server_control_terminal()

    else:
        print("Unknown command.")
        server_control_terminal()

    # TODO add command to kick & or ban user by UID
    #  use complex commands by using .split on input to take in multiple commands at once EX: list uid(lists all uids)
    #  pretty print using print("{: >20} {: >20} {: >20}".format(*row))


def configure_json_file(path, structure):
    with open(path, 'w') as file:
        file.write(json.dumps(structure, separators=(',', ':'), indent=5))


def collect_json_from_file(path):
    with open(path, 'rt') as file:
        return json.loads(file.read())


def update_json_file(path, location, data):
    updated_file_data = collect_json_from_file(path)[location][data[0]] = data[1]
    with open(path, 'w') as file:
        file.write(json.dumps(updated_file_data, separators=(',', ':'), indent=5))


print("Starting server...")
t1 = threading.Thread(target=server_control_terminal)
t1.start()
server_data = ServerData()
fernet = Fernet(encryption_key)
receive()
