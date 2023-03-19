import errno
import socket
from tkinter import *
from cryptography.fernet import Fernet
import json
from tkinter import messagebox

handshake_code = '75RJM202y299U8a34fYGjojPAlP3nfzb'
successful_handshake_code = "o2rWLN8eduep9O6cUfrmBEKF1jh8LOpB"
general_chat_code = "3rIP4sf5VA6QC2oIYFiepjtb7HWp97SK"
personal_chat_code = 'F26RUPmRikmepuz4vdUkaSH4fHgWcMO3'
login_code = 'z7eLQzZ7gmnqx4C6JQML6nMpjP0Nc1Ex'
sign_up_code = 'ClyGibkmr9JBMo8CpFpMyLrfvXTxXbkV'
new_user_id_code = 'gemVWz769eDyy7EBK3MXPePGT3UfCuHZ'


class Client:
    def __init__(self):
        self.self = self
        self.running = True
        self.HOST = None
        self.PORT = None
        self.sock = None
        self.user_data = None
        self.text_box = None
        self.chat_box = None
        self.login_method = None

    def config_socket(self, host, port, main_window, user_data, login_method):
        self.HOST = host
        self.PORT = port
        self.text_box = main_window.text_box
        self.chat_box = main_window.chat_box
        print(type(self.chat_box))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))
        self.user_data = user_data
        self.login_method = login_method


def receive():
    while client.running:
        try:
            # Receives, decrypts, and decodes message.
            message = fernet.decrypt(client.sock.recv(2024)).decode('utf-8')

            if message == handshake_code:
                # Sends data input by user in log in screen.
                client.sock.send(encrypt_outgoing(client.login_method + client.user_data))

            elif message == successful_handshake_code:
                # Not entirely sure if this is necessary.
                print('This worked')

            # Reads first 32 bytes of message.
            elif message[0:32] == new_user_id_code:
                # File data is created and assigned value of last eight bytes of message.
                file_data = {'user_id': message[32:]}

                # File data is written to json file, and read the next time someone tries to sign in.
                with open('client_info.json', 'w') as file:
                    file.write(json.dumps(file_data, separators=(',', ':'), indent=5))

                # Confirmation of successful storage of user id is sent, client joins server as normal.
                client.sock.send(encrypt_outgoing(successful_handshake_code))

            # A regular message has been sent to general chat.
            else:
                update_chat_box(message, 0)

        # Handles user disconnecting on client side.
        except OSError as e:
            if e.errno == errno.ENOTSOCK:
                break

        # Handles the termination of server.(Not well apparently, plan to fix)
        except ConnectionAbortedError:
            update_chat_box("The server has been closed.", 2)


def prepare_for_send():
    message = client.text_box.get("1.0", END)
    if message.strip() == "":
        messagebox.showerror("Error", "You cannot send a blank message.")

    else:
        client.sock.send(encrypt_outgoing(message))
    client.text_box.delete('1.0', END)


def stop():
    client.running = False
    client.sock.close()


def update_chat_box(message, method):
    # Enables the chatbox
    client.chat_box.config(state="normal")

    # This will print a regular message.
    if method == 0:
        client.chat_box.insert(END, message)

    # This will print a client connection message in green.
    elif method == 1:
        client.chat_box.insert(END, message, 'connection')

    # This will print a server or client disconnect message in red.
    elif method == 2:
        print("server killed")
        client.chat_box.insert(END, message, 'disconnection')

    # Disables the chatbox
    client.chat_box.config(state="disabled")


def on_closing():
    stop()
    exit(0)


def configure_json_file(path, structure):
    with open(path, 'w') as file:
        file.write(json.dumps(structure, separators=(',', ':'), indent=5))


def collect_json_from_file(path):
    with open(path, 'r') as file:
        return json.loads(file.read())



def update_json_file(path, location, data):
    updated_file_data = collect_json_from_file(path)[location][data[0]] = data[1]
    with open(path, 'w') as file:
        file.write(json.dumps(updated_file_data, separators=(',', ':'), indent=5))


def encrypt_outgoing(message):
    return fernet.encrypt(message.encode())


def decrypt_incoming(message):
    return fernet.decrypt(message).decode('utf-8')


encryption_key = b'e9iRDX8f-2GiHwWi_toavUnscTwWz6AwVwdAf53y6wY='
fernet = Fernet(encryption_key)
client = Client()
