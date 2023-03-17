import sys
import os
import errno
import socket
from tkinter import *
from cryptography.fernet import Fernet
from tkinter import messagebox
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import configure_json_file, collect_json_from_file, update_json_file



handshake_code = '75RJM202y299U8a34fYGjojPAlP3nfzb'
successful_handshake_code = "o2rWLN8eduep9O6cUfrmBEKF1jh8LOpB"
general_chat_code = "3rIP4sf5VA6QC2oIYFiepjtb7HWp97SK"
personal_chat_code = 'F26RUPmRikmepuz4vdUkaSH4fHgWcMO3'
login_code = 'z7eLQzZ7gmnqx4C6JQML6nMpjP0Nc1Ex'
sign_up_code = 'ClyGibkmr9JBMo8CpFpMyLrfvXTxXbkV'
new_user_id_code = 'gemVWz769eDyy7EBK3MXPePGT3UfCuHZ'


# test user login info: z7eLQzZ7gmnqx4C6JQML6nMpjP0Nc1Ex12345678MeeskaMooska////////////testpassword////////////


class Client:
    def __init__(self):
        self.self = self
        self.running = True
        self.HOST = None
        self.PORT = None
        self.sock = None
        self.username = None
        self.text_box = None
        self.chat_box = None
        self.login_method = None

    def config_socket(self, host, port, main_window, username, login_method):
        self.HOST = host
        self.PORT = port
        self.text_box = main_window.text_box
        self.chat_box = main_window.chat_box
        print(type(self.chat_box))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))
        self.username = username
        self.login_method = login_method


def receive():
    while client.running:
        try:
            # Receives, decrypts, and decodes message.
            message = fernet.decrypt(client.sock.recv(2024)).decode('utf-8')

            if message == handshake_code:
                print("handshake recieved")
                # TODO setup userdata file, that contains username, password, and user_id to automatically sign in
                client.sock.send(fernet.encrypt(bytes(client.login_method + client.username, 'utf-8')))

            elif message == successful_handshake_code:
                print('This worked.')

            elif message == new_user_id_code:
                print(message[32:-1])
                configure_json_file('client_info.json', {"user_id": message[32:-1]})

            else:
                update_chat_box(message, 0)

        # Handles user disconnecting on client side.
        except OSError as e:
            if e.errno == errno.ENOTSOCK:
                break

        except ConnectionAbortedError:
            update_chat_box("The server has been closed.", 2)


def prepare_for_send():
    message = client.text_box.get("1.0", END)
    if message.strip() == "":
        messagebox.showerror("Error", "You cannot send a blank message.")

    else:
        client.sock.send(fernet.encrypt(message.encode()))
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


def encrypt_outgoing():
    pass


def decrypt_incoming():
    pass


encryption_key = b'e9iRDX8f-2GiHwWi_toavUnscTwWz6AwVwdAf53y6wY='
fernet = Fernet(encryption_key)
client = Client()
