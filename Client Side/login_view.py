from tkinter import *
import time


class LoginView(str):
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
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        # <<<<---- Initializing gui objects. ---->>>> #
        # Entries
        self.username_entry = Entry(self.root)
        self.password_entry = Entry(self.root)

        # Buttonsb
        self.submit_button = Button(self.root, text="Submit", padx=20)
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
        self.__init__()

    def submit_pressed(self):
        return [self.username_entry.get(), self.password_entry.get()]

    def method_button_pressed(self, selected):
        self.selected_method = selected
        if selected == 0:
            self.sign_in_button.config(relief=SUNKEN)
            self.sign_up_button.config(relief=RAISED)
        else:
            self.sign_in_button.config(relief=RAISED)
            self.sign_up_button.config(relief=SUNKEN)

