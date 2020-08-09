import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

class MainProgram:
    def __init__(self, master):
        self.root = master
        self.root.title('Programa do Lecao')
        self.root.state('zoomed')

        self.SideFrame = tk.Frame(master, bg='#c9c9c9', width=90, bd=0)
        self.SideFrame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.MainSpace = tk.Frame(master, bg='#dbdbdb', bd=0)
        self.MainSpace.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.SideFramePacking()     

    def SideFramePacking(self):
        tButtonImage = self.CreateImage(r'Images\Buttons\tButton.png')
        self.tButton = tk.Button(self.SideFrame, image=tButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.tShape)
        self.tButton.image = tButtonImage
        self.tButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        LButtonImage = self.CreateImage(r'Images\Buttons\LButton.png')
        self.LButton = tk.Button(self.SideFrame, image=LButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.LShape)
        self.LButton.image = LButtonImage
        self.LButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        uButtonImage = self.CreateImage(r'Images\Buttons\uButton.png')
        self.uButton = tk.Button(self.SideFrame, image=uButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.uShape)
        self.uButton.image = uButtonImage
        self.uButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        cButtonImage = self.CreateImage(r'Images\Buttons\cButton.png')
        self.cButton = tk.Button(self.SideFrame, image=cButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.cShape)
        self.cButton.image = cButtonImage
        self.cButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        iButtonImage = self.CreateImage(r'Images\Buttons\iButton.png')
        self.iButton = tk.Button(self.SideFrame, image=iButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.iShape)
        self.iButton.image = iButtonImage
        self.iButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


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
        global TopEntry, RightEntry, LeftEntry, BottomEntry

        self.ClearMainSpace()
        
        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        self.EntryFont = Font(family='Arial', size=20)

        Register = DataFrame.register(self.validate)

        TopEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        TopEntry['validatecommand'] = (Register, '%P', '%d')
        TopEntry.pack(side=tk.TOP, pady=(50, 25)) 

        RightEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        RightEntry['validatecommand'] = (Register, '%P', '%d')
        RightEntry.pack(side=tk.RIGHT, anchor='w', padx=30)

        LeftEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        LeftEntry['validatecommand'] = (Register, '%P', '%d')
        LeftEntry.pack(side=tk.LEFT, anchor='n', pady=75, padx=30)

        tShapeImage = self.CreateImage('Images/Shapes/tShape.png')
        tShapeLabel = tk.Label(DataFrame, image=tShapeImage, bd=0)
        tShapeLabel.image = tShapeImage
        tShapeLabel.pack()

        BottomEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        BottomEntry['validatecommand'] = (Register, '%P', '%d')
        BottomEntry.pack(side=tk.BOTTOM, pady=(25, 50))
        
        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=self.Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscartImage = self.CreateImage('Images/Buttons/discart.png')
        DiscartButton = tk.Button(ButtonsFrame, image=DiscartImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=self.Discart)
        DiscartButton.image = DiscartImage
        DiscartButton.grid(row=0, column=1, padx=5)

    def LShape(self):
        pass

    def uShape(self):
        pass

    def cShape(self):
        pass

    def iShape(self):
        pass

    def Discart(self):
        TopEntry.delete(0, tk.END)
        RightEntry.delete(0, tk.END)
        LeftEntry.delete(0, tk.END)
        BottomEntry.delete(0, tk.END)


    def Calculate(self):
        x = float(TopEntry.get())
        b = float(LeftEntry.get())
        y = float(RightEntry.get())
        z = float(BottomEntry.get())

        print(f'x: {x}\ny: {y}\nb: {b}\nz: {z}')

        self.ClearMainSpace()

        LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
        LeftFrame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        RightFrame = tk.Frame(self.MainSpace, bg='green', bd=0)
        RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        Ycg = (z * y * (y / 2) + b * x * (y + (b / 2))) / (z * y + b * x)

        YcgLabel = tk.Label(LeftFrame, text='Ycg', font=self.EntryFont, bg='#dbdbdb', fg='#303030')
        YcgLabel.grid(row=0, column=0, padx=25, pady=10, sticky='w')

        YcgLabelContent = tk.Label(LeftFrame, text=str(f'{Ycg:.2f}'), font=self.EntryFont, bg='#dbdbdb', fg='#303030')
        YcgLabelContent.grid(row=1, column=0, padx=25, pady=10, sticky='w')
        

    
    def Teste(self):

        print(float(LeftEntry.get()))

def main():
    root = tk.Tk()
    MainProgram(root)
    root.mainloop()

if __name__ == '__main__':
    main()
