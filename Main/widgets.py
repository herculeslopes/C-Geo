import tkinter as tk
from tkinter.font import Font

""" tButtonImage = self.CreateImage(r'Images\Buttons\tButton.png')
    self.tButton = tk.Button(self.SideFrame, image=tButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.tShape)
    self.tButton.image = tButtonImage
    self.tButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)"""

def validate(self, value, action):
    if action == '1':
        if value:
            try:
                float(value)
                return True
                
            except ValueError:
                return False
        
        else:
            return False
    else:
        return True


class SideButton(tk.Button):    
    def __init__(self, master, text):
        super().__init__(master)
        self['text'] = text
        self['bg'] = '#c9c9c9'
        self['activebackground'] = '#c9c9c9'
        self['bd'] = 0
    

class EntryField(tk.Entry):
    def __init__(self, master):
        super().__init__(master)
        self.entry_font = Font(family='Calibri', size=20)
        self['bg'] = '#bfbfbf'
        self['fg'] = '#303030'
        self['bd'] = 0
        self['justify'] = tk.CENTER
    