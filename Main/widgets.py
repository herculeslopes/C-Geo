import tkinter as tk
from tkinter.font import Font
from tkinter import ttk

# combo_style = ttk.Style()

fibra_options = (
    'ACIMA',
    'ABAIXO'
)

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

class OpenFibraButton(tk.Button):
    def __init__(self, master, action):
        super().__init__(master)
        self['text'] = 'Abrir cálculo da fibra'
        self['font'] = Font(family='Arial', size=12, weight='bold')
        self['bg'] = '#8c8c8c'
        self['activebackground'] = '#dbdbdb'
        self['fg'] = '#dbdbdb'
        self['activeforeground'] = '#242424'
        self['bd'] = 0
        self['command'] = action


class ResultLabel(tk.Label):
    def __init__(self, master, txt):
        super().__init__(master)
        self['text'] = txt
        self['font'] = Font(family='Calibri', size=16)
        self['bg'] = '#d1d1d1' #b0b0b0
        self['fg'] = '#303030'


class ResultValue(tk.Label):
    def __init__(self, master, txt):
        super().__init__(master)
        self['text'] = txt
        self['font'] = Font(family='Calibri', size=16)
        self['bg'] = '#d1d1d1' #b0b0b0
        self['fg'] = '#303030'


class ValueLabel(tk.Label):
    def __init__(self, master, txt):
        super().__init__(master)
        self['text'] = txt
        self['font'] = Font(family='Calibri', size=16)
        self['bg'] = '#dbdbdb'
        self['fg'] = '#303030'


class WinFibraLabel(tk.Label):
    def __init__(self, master, txt):
        super().__init__(master)
        self['text'] = txt
        self['font'] = Font(family='Arial', size=16)
        self['bg'] = '#dbdbdb'
        self['fg'] = '#303030'


class WinFibraEntry(tk.Entry):
    def __init__(self, master):
        super().__init__(master)
        self['font'] = Font(family='Calibri', size=20)
        self['bg'] = '#bfbfbf'
        self['fg'] = '#303030'
        self['bd'] = 0
        self['justify'] = tk.CENTER


class FibraCombo(ttk.Combobox):
    def __init__(self, master):
        super().__init__(master)

        self['font'] = Font(family='Calibri', size=16)
        self['values'] = fibra_options
        self['state'] = 'readonly'
        self['width'] = 10
        self.current(0)

"""class FibraRadio(tk.Radiobutton):
    def __init__(self, master, txt):
        super().__init__(master)"""



class FibraResult(tk.Label):
    def __init__(self, master):
        super().__init__(master)
        self['font'] = Font(family='Arial', size=16)
        self['bg'] = '#dbdbdb'
        self['fg'] = '#303030'
        self['width'] = 25
        self['bd'] = 2
