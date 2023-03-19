import threading
from tkinter import *
from tkinter import scrolledtext
from client import client, prepare_for_send, receive
import json

login_code = 'z7eLQzZ7gmnqx4C6JQML6nMpjP0Nc1Ex'
sign_up_code = 'ClyGibkmr9JBMo8CpFpMyLrfvXTxXbkV'


def padded_text(text, length):
    padding_amount = length - len(text)
    text = text + ('/' * padding_amount)
    return text


class MainWindow:
    def __init__(self):
        self.root = None
        self.chat_box = None
        self.text_box = None
        self.send_button = None

    def config_gui(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.chat_box = scrolledtext.ScrolledText(self.root, state="disabled", padx=30)
        self.chat_box.tag_config('warning', foreground="red")
        self.text_box = Text(self.root, height=3)
        self.send_button = Button(self.root, text="Send", padx=20, pady=16, command=prepare_for_send)
        self.chat_box.grid(row=0, column=0, columnspan=4)
        self.text_box.grid(row=1, column=0, columnspan=3)
        self.send_button.grid(row=1, column=3, columnspan=1)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        #TODO create init class the clear everything and then call here.
        self.root.destroy()
        client.sock.close()


main_window = MainWindow()


class LoginWindow(str):
    def __init__(self):
        # GUI variables
        self.self = self
        self.root = None
        # Default method is sign in
        self.selected_method = 0

        # Entries
        self.username_entry = None
        self.password_entry = None

        # Buttons
        self.submit_button = None
        self.sign_in_button = None
        self.sign_up_button = None

    def start_gui(self):
        # GUI variables
        self.root = Tk()
        self.root.title("Sign In / Sign Up")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        # <<<<---- Initializing gui objects. ---->>>> #
        # Entries
        self.username_entry = Entry(self.root)
        self.password_entry = Entry(self.root)

        # Buttons
        self.submit_button = Button(self.root, text="Submit", padx=20, command=self.submit_pressed)
        self.sign_in_button = Button(self.root, relief=SUNKEN, text="Sign In",
                                     command=lambda: self.method_button_pressed(0))
        self.sign_up_button = Button(self.root, text="Sign Up",
                                     command=lambda: self.method_button_pressed(1))

        # <<<<---- Packing gui objects. ---->>>> #
        # Entries
        self.username_entry.grid(row=0, column=0, columnspan=2)
        self.password_entry.grid(row=1, column=0, columnspan=2)

        # Buttons
        self.submit_button.grid(row=2, column=0, columnspan=2)
        self.sign_in_button.grid(row=3, column=0)
        self.sign_up_button.grid(row=3, column=1)

        # Start the mainloop
        self.root.mainloop()

    def exit(self):
        self.root.destroy()
        self.__init__()

    def submit_pressed(self):
        if self.selected_method == 0:
            user_id = collect_json_from_file('client_info.json')['user_id']
            username = self.username_entry.get()
            password = self.password_entry.get()
            main_window.config_gui()
            client.config_socket("192.168.1.189", 80, main_window,
                                 str(user_id) + padded_text(username, 24) + padded_text(password, 32), login_code)
            cl = threading.Thread(target=receive)
            cl.start()
            self.exit()
            main_window.root.mainloop()

        else:
            username = self.username_entry.get()
            password = self.password_entry.get()
            main_window.config_gui()
            client.config_socket("192.168.1.189", 80, main_window,
                                 padded_text(username, 24) + padded_text(password, 32), sign_up_code)
            cl = threading.Thread(target=receive)
            cl.start()
            self.exit()
            main_window.root.mainloop()

    def method_button_pressed(self, selected):
        self.selected_method = selected
        if selected == 0:
            self.sign_in_button.config(relief=SUNKEN)
            self.sign_up_button.config(relief=RAISED)
        else:
            self.sign_in_button.config(relief=RAISED)
            self.sign_up_button.config(relief=SUNKEN)


def collect_json_from_file(path):
    with open(path, 'r') as file:
        return json.loads(file.read())


login_window = LoginWindow()
login_window.start_gui()
