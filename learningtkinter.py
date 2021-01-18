import tkinter as tk
from tkinter import StringVar, ttk


root = tk.Tk()
uiLabelFrame = ttk.LabelFrame(master=root, text='Learning TKinter')

name = StringVar()
name_label = ttk.Label(uiLabelFrame, text='name')
name_entry = ttk.Entry(uiLabelFrame, textvariable=name)


def add():
    global name    
    userName = name_label.config(text=f'Your name is {name.get().strip()}')
    name_entry.delete(0, 'end')


btn = ttk.Button(uiLabelFrame, text='Submit', command=add)

list(map(lambda x: x.pack(padx=5, pady=5), [uiLabelFrame, name_label, name_entry, btn]))[:]

root.minsize(400, 400)
root.mainloop()

# This comment was edited by Omkar
