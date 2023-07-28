import SettView as sv
from pynput.keyboard import Controller
import tkinter as tk

class Main:
    def __init__(self):
        print("Object created")


keyboardController = Controller()
root = tk.Tk()
root.title("Beautify XML/JSON")
app = sv.SettView(root)
root.mainloop()
#op = Op.Operation()
#op.autoType("hello check",keyboard)


