from tkinter import *
import time


class LoginView:
    def __init__(self):
        # GUI variables
        self.self = self
        self.root = None

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

        # <<<<---- Initializing gui objects. ---->>>> #
        # Entries
        self.username_entry = Entry(self.root)
        self.password_entry = Entry(self.root)

        # Buttons
        self.submit_button = Button(self.root, text="Submit", padx=20)
        self.sign_in_button = Button(self.root, text="Sign In")
        self.sign_up_button = Button(self.root, text="Sign Up")

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

    def on_window_close(self):
        pass

    def submit_pressed(self):
        pass


login_view = LoginView()
login_view.start_gui()