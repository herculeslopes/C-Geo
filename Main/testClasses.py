import tkinter as tk
from typing import Text
from widgets import EntryField, SideButton

root = tk.Tk()
root.geometry('300x200')

btn = SideButton(root, text='Primeiro Botão')
btn.pack()

entry1 = EntryField(root)

root.mainloop()
