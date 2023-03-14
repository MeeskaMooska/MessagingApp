import errno
import socket
from tkinter import *
from cryptography.fernet import Fernet
from tkinter import messagebox


class Client():
    def __init__(self):
        self.self = self
        self.running = True
        self.HOST = None
        self.PORT = None
        self.sock = None
        self.username = None
        self.text_box = None
        self.chat_box = None

    def config(self, host, port, username, text_box, chat_box):
        self.HOST = host
        self.PORT = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))
        self.username = bytes(username, 'utf-8')
        self.text_box = text_box
        self.chat_box = chat_box


def receive():
    while client.running:
        try:

            message = client.sock.recv(2024)
            if fernet.decrypt(message).decode('utf-8') == "75RJM202y299U8a34fYGjojPAlP3nfzb":
                print("handshake recieved")
                # TODO setup userdata file, that contains username, password, and user_id to automatically sign in
                client.sock.send(client.username)

            elif fernet.decrypt(message).decode('utf-8') == "o2rWLN8eduep9O6cUfrmBEKF1jh8LOpB":
                messagebox.showinfo("Connected.", "Successfully connected to target machine.")

            else:
                update_chat_box(fernet.decrypt(message).decode('utf-8'), 0)

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
        client.chat_box.insert(END, message, 'disconnection')

    # Disables the chatbox
    client.chat_box.config(state="disabled")


def on_closing():
    stop()
    exit(0)


def decrypt_incoming(message):
    fernet.decrypt(message).decode('utf-8')


def encrypt_outgoing(message):
    pass


encryption_key = b'e9iRDX8f-2GiHwWi_toavUnscTwWz6AwVwdAf53y6wY='
fernet = Fernet(encryption_key)
client = Client()
