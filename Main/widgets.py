import tkinter as tk
from tkinter.font import Font

def validate(value, action):
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
    def __init__(self, master, img, action):
        super().__init__(master)
        self['image'] = img
        self['bg'] = '#c9c9c9'
        self['activebackground'] = '#c9c9c9'
        self['bd'] = 0
        self['command'] = action
    

# Caixa de Entrada Para Medidas
class EntryField(tk.Entry):
    def __init__(self, master):
        super().__init__(master)
        self['font'] = Font(family='Calibri', size=20)
        self['bg'] = '#bfbfbf'
        self['fg'] = '#303030'
        self['bd'] = 0
        self['justify'] = tk.CENTER


class ShapeImage(tk.Label):
    def __init__(self, master, img):
        super().__init__(master)
        self['image'] = img
        self['bd'] = 0


class MenuButton(tk.Button):
    def __init__(self, master, img, action):
        super().__init__(master)
        self['image'] = img
        self.image = img
        self['bg'] = '#dbdbdb'
        self['activebackground'] = '#dbdbdb'
        self['bd'] = 0
        self['command'] = action
