import tkinter as tk
from tkinter.font import Font
from tkinter import ttk

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


# Widgets para main.py
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
        self['validate'] = 'key'
        Register = master.register(validate)
        self['validatecommand'] = (Register, '%P', '%d')
    

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
        self['activebackground'] = '#b0b0b0'
        self['fg'] = '#dbdbdb'
        self['activeforeground'] = '#363636'
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


class DividingLine(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['bg'] = '#8c8c8c'
        self['height'] = 3


class ValueLabel(tk.Label):
    def __init__(self, master, txt):
        super().__init__(master)
        self['text'] = txt
        self['font'] = Font(family='Calibri', size=16)
        self['bg'] = '#dbdbdb'
        self['fg'] = '#303030'


# Widtets para win_info.py
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
        self['validate'] = 'key'
        Register = master.register(validate)
        self['validatecommand'] = (Register, '%P', '%d')


class EntryLine(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self['bg'] = '#8c8c8c'
        self['height'] = 3


class ButtonPos(tk.Button):
    def __init__(self, master, txt, action):
        super().__init__(master)
        self['bg'] = '#8c8c8c'
        self['activebackground'] = '#b0b0b0'
        self['fg'] = '#dbdbdb'
        self['activeforeground'] = '#dbdbdb'
        self['font'] = Font(family='Calibri', size=12, weight='bold')
        self['text'] = txt
        self['relief'] = tk.FLAT
        self['width'] = 20
        self['command'] = action


class FibraResult(tk.Label):
    def __init__(self, master):
        super().__init__(master)
        self['font'] = Font(family='Arial', size=16)
        self['bg'] = '#dbdbdb'
        self['fg'] = '#303030'
        self['width'] = 25
        self['bd'] = 2


# Widgets para win_credits.py
class ProfileTitle(tk.Label):
    def __init__(self, master, txt):
        super().__init__(master)
        self['font'] = Font(family='Arial', size=16)
        self['text'] = txt
        self['bg'] = '#dbdbdb'


class ProfileLink(tk.Label):
    def __init__(self, master, txt, action):
        super().__init__(master)
        self['font'] = Font(family='Arial', size=10, underline=True)
        self['text'] = txt
        self['bg'] = '#dbdbdb'
        self['fg'] = 'blue'

        self.bind('<ButtonRelease-1>', action)
        self.bind('<Enter>', self.onEnter)
        self.bind('<Leave>', self.onLeave)

    def onEnter(self, event):
        self['fg'] = 'red'

    def onLeave(self, event):
        self['fg'] = 'blue'


class ProfileDescription(tk.Text):
    def __init__(self, master, txt):
        super().__init__(master)
        self.insert(tk.INSERT, txt.strip())
        self['state'] = 'disabled',
        self['font'] = 'Arial',
        self['relief'] = tk.FLAT,
        self['width'] = 40,
        self['height'] = 10,
        self['bg'] = '#dbdbdb', # should be #dbdbdb
        self['fg'] = '#303030',
        