import tkinter as tk
from tkinter.font import Font

""" tButtonImage = self.CreateImage(r'Images\Buttons\tButton.png')
    self.tButton = tk.Button(self.SideFrame, image=tButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.tShape)
    self.tButton.image = tButtonImage
    self.tButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)"""

class SideButton(tk.Button):    
    def __init__(self, master, text):
        super().__init__(master)
        self['text'] = text
        self['bg'] = '#c9c9c9'
        self['activebackground'] = '#c9c9c9'
        self['bd'] = 0
    

class EntryField():
    def __init__(self, master):
        self.entry_font = Font(family='Calibri', size=20)    
        self.entry = tk.Entry(master, font=self.entry_font, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER)
        self.entry.pack()
    