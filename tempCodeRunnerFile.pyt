import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
mb = tk.Menubutton(top, text="condiments", relief=tk.RAISED)
mb.grid()
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mayoVar = tk.IntVar()
ketchVar = tk.IntVar()
mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

mb.pack()
top.mainloop()