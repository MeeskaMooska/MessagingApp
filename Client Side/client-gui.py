import threading
from tkinter import *
from tkinter import scrolledtext
from tkinter import simpledialog
import client


def on_closing():
    client.client.sock.close()
    root.destroy()


root = Tk()
root.resizable(False, False)

chat_box = scrolledtext.ScrolledText(root, state="disabled", padx=30)
chat_box.tag_config('warning', foreground="red")
text_box = Text(root, height=3)
send_button = Button(root, text="Send", padx=20, pady=16, command=client.prepare_for_send)

chat_box.grid(row=0, column=0, columnspan=4)
text_box.grid(row=1, column=0, columnspan=3)
send_button.grid(row=1, column=3, columnspan=1)

root.protocol("WM_DELETE_WINDOW", client.on_closing)
username = simpledialog.askstring("Username", "What will your temporary username be?")

client.client.config("192.168.1.189", 80, username, text_box, chat_box)
cl = threading.Thread(target=client.receive)
cl.start()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
