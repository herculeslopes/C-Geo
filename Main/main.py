import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

class MainProgram:
    def __init__(self, master):
        self.root = master
        self.root.state('zoomed')

        self.SideFrame = tk.Frame(master, bg='#c9c9c9', width=90, bd=0)
        self.SideFrame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.MainSpace = tk.Frame(master, bg='#dbdbdb', bd=0)
        self.MainSpace.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tButtonImage = self.CreateImage(r'Images\Buttons\tButton.png')
        self.tButton = tk.Button(self.SideFrame, image=tButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.tShape)
        self.tButton.image = tButtonImage
        self.tButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


    def ClearMainSpace(self):
        for widget in self.MainSpace.winfo_children():
            widget.destroy()

    def CreateImage(self, path):
        ImageFile = Image.open(path)
        TkImage = ImageTk.PhotoImage(ImageFile)
        
        return TkImage

    def validate(self, value, action):
        '''if value.isdigit() or value == '':
            
            return True
        else:
            return False'''

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


    def tShape(self):

        self.ClearMainSpace()
        
        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        EntryFont = Font(family='Arial', size=20)

        Register = DataFrame.register(self.validate)

        TopEntry = tk.Entry(DataFrame, font=EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        TopEntry['validatecommand'] = (Register, '%P', '%d')
        TopEntry.pack(side=tk.TOP, pady=(50, 25)) 

        RightEntry = tk.Entry(DataFrame, font=EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        RightEntry['validatecommand'] = (Register, '%P', '%d')
        RightEntry.pack(side=tk.RIGHT, anchor='w', padx=30)

        LeftEntry = tk.Entry(DataFrame, font=EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        LeftEntry['validatecommand'] = (Register, '%P', '%d')
        LeftEntry.pack(side=tk.LEFT, anchor='n', pady=75, padx=30)

        tShapeImage = self.CreateImage('Images/Shapes/tShape.png')
        tShapeLabel = tk.Label(DataFrame, image=tShapeImage, bd=0)
        tShapeLabel.image = tShapeImage
        tShapeLabel.pack()

        BottomEntry = tk.Entry(DataFrame, font=EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        BottomEntry['validatecommand'] = (Register, '%P', '%d')
        BottomEntry.pack(side=tk.BOTTOM, pady=(25, 50))
        
        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        SaveImage = self.CreateImage('Images/Buttons/save.png')
        SaveButton = tk.Button(ButtonsFrame, image=SaveImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0)
        SaveButton.image = SaveImage
        SaveButton.grid(row=0, column=0, padx=5)

        DiscartImage = self.CreateImage('Images/Buttons/discart.png')
        DiscartButton = tk.Button(ButtonsFrame, image=DiscartImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0)
        DiscartButton.image = DiscartImage
        DiscartButton.grid(row=0, column=1, padx=5)


def main():
    root = tk.Tk()
    MainProgram(root)
    root.mainloop()

if __name__ == '__main__':
    main()
