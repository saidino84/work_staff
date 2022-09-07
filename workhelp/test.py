from tkinter import ttk
from customtkinter import *
from tkinter import *


root=Tk()
style=ttk.Style()
style.configure('TFrame',background="#ff01c2")

frm=ttk.Frame(root,style='TFrame')
frm.pack(expand=True,fill='both')



root.geometry("240x350")
root.maxsize(240,320)
root.maxsize(250,350)
root.mainloop()
