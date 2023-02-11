import socket
import threading
from tkinter import *


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


def write(message):
    client.sock.send(bytes(message, 'utf-8'))


def receive():
    while client.running:
        print("here")
        try:
            message = client.sock.recv(1024)
            print(message)
            if message.decode('utf-8') == "USER":
                print("the username message got throught")
                client.sock.send(client.username)
            else:
                update_chat_box(message)
        except ConnectionAbortedError:
            break


def prepare_for_send():
    message = client.text_box.get("1.0", END)
    # TODO throw error here
    if message == "":
        pass

    else:
        write(message)
    client.text_box.delete('1.0', END)


def stop():
    client.running = False
    client.sock.close()
    exit(0)


def update_chat_box(message):
    client.chat_box.config(state="normal")
    client.chat_box.insert(END, message)
    client.chat_box.config(state="disabled")


def on_closing():
    stop()
    exit(0)


client = Client()
