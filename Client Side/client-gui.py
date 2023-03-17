import threading
import time
from tkinter import *
from tkinter import scrolledtext
from tkinter import simpledialog
from client import client, prepare_for_send, receive


def padded_text(text, length):
    padding_amount = length - len(text)
    text = text + ('/' * padding_amount)
    return text



class MainWindow:
    def __init__(self):
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
        self.root.mainloop()

    def on_close(self):
        #TODO create init class the clear everything and then call here.
        self.root.destroy()
        client.sock.close()

class LoginWindow(str):
    def __init__(self):
        # GUI variables
        self.self = self
        self.root = None
        self.signed_in = None
        # Default method is sign in
        self.selected_method = 0

        # Entries
        self.username_entry = None
        self.password_entry = None

        # Buttons
        self.submit_button = None
        self.sign_in_button = None
        self.sign_up_button = None
        self.start_gui()

    def start_gui(self):
        # GUI variables
        self.root = Tk()
        self.root.title("Sign In / Sign Up")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        # <<<<---- Initializing gui objects. ---->>>> #
        # Entries
        self.username_entry = Entry(self.root)
        self.password_entry = Entry(self.root)

        # Buttonsb
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

    def close(self):
        self.root.destroy()

    def submit_pressed(self):
        user_id = 12345678
        username = self.username_entry.get()
        password = self.password_entry.get()
        client.config_socket("192.168.1.189", 80, str(user_id) + padded_text(username, 24) + padded_text(password, 32))
        cl = threading.Thread(target=receive)
        cl.start()
        self.signed_in = True

    def method_button_pressed(self, selected):
        self.selected_method = selected
        if selected == 0:
            self.sign_in_button.config(relief=SUNKEN)
            self.sign_up_button.config(relief=RAISED)
        else:
            self.sign_in_button.config(relief=RAISED)
            self.sign_up_button.config(relief=SUNKEN)


login_window = LoginWindow()


if login_window.signed_in:
    main_window = MainWindow()
    client.config_main_gui(main_window.text_box, main_window.chat_box)
