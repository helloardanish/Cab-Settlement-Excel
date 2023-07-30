import SettView as sv
from pynput.keyboard import Controller
import tkinter as tk
import Validate as vl



class Main:
    def __init__(self):
        print("Object created")

vlObj = vl.Validate()

deviceList = ["Darwin-B2:1D:94:38:3D:A1","Darwin-B2:1D:94:38:3D:A2","Darwin-B2:1D:94:38:3D:A3"]


device_id = vlObj.get_device_id()


print("Device Id : "+device_id)


if device_id in deviceList:
    print("User verified.")
    keyboardController = Controller()
    root = tk.Tk()
    root.title("Easy Settlement")
    app = sv.SettView(root)
    root.mainloop()
    #op = Op.Operation()
    #op.autoType("hello check",keyboard)
else:
    print("Register the app.")

