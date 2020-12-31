import tkinter
from tkinter import StringVar, ttk
from typing import Text

root = tkinter.Tk()

name = tkinter.StringVar()
name_entry = ttk.Entry(textvariable=name)

display_name = StringVar()
display_name.set('your name is')

label = ttk.Label(root, textvariable=name)


def add():
    global name    
    name = display_name.set(f'Your name is {name_entry.get()}')
btn = ttk.Button(text='Submit', command=add)
label.pack()



name_entry.pack()
btn.pack()
root.minsize(400, 400)
root.mainloop()

