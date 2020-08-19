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

        self.EntryFont = Font(family='Arial', size=20)
        self.ResultFont = Font(family='Arial', size=45)

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

        RomanIButtonImage = self.CreateImage(r'Images\Buttons\RomanIButton.png')
        self.RomanIButton = tk.Button(self.SideFrame, image=RomanIButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0, command=self.RomanIShape)
        self.RomanIButton.image = RomanIButtonImage
        self.RomanIButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


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

        def Calculate(event=None):
            x = float(TopEntry.get())
            b = float(LeftEntry.get())
            y = float(RightEntry.get())
            z = float(BottomEntry.get())

            print(f'x: {x}\ny: {y}\nb: {b}\nz: {z}')

            self.ClearMainSpace()

            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)

            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            Ycg = (z * y * (y / 2) + b * x * (y + (b / 2))) / (z * y + b * x)

            Iz = (((x * (b ** 3)) / (12) ) + (b * x * ((y + (b / 2) - Ycg)) ** 2)) + (((z * (y ** 3)) / (12)) + (y * z * ((Ycg - (y / 2)) ** 2)))

            if Ycg < y or Ycg == y:
                Scg = (Ycg * z * (Ycg / 2))
            
            else:
                Scg = x * (y + b - Ycg) * ((y + b - Ycg) / 2)

            print(f'Scg: {Scg}')

            '''Yz = 
            (((x * (b ** 3)) / (12)) + (x * b * ((y + (b / 2)) - Ycg))) 
            + 
            (((z * (y ** 3)) / (12)) + ((y * z) * (Ycg - (y / 2))))'''

            print(f'Ycg = {Ycg}')
            print(f'Iz = {Iz}')

            YcgLabel = tk.Label(LeftFrame, text='Ycg =', anchor='e', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=50, sticky='w')

            YcgLabelContent = tk.Label(LeftFrame, text=str(f'{Ycg:.2f}'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=50, sticky='w')

            IzLabel = tk.Label(LeftFrame, text='Iz =', anchor='e', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=50, sticky='w')

            IzLabelContent = tk.Label(LeftFrame, text=str(f'{Iz:.2f}'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=50, sticky='w')

            ScgLabel = tk.Label(LeftFrame, text='Scg =', anchor='e', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabel.grid(row=2, column=0, padx=10, pady=50, sticky='w')

            ScgLabelContent = tk.Label(LeftFrame, text=str(f'{Scg:.2f}'), font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=50, sticky='w')

            width = 900
            height = 900

            ShapeCanvas = tk.Canvas(RightFrame, width=width, height=height, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack(expand=True)

            '''
            ShapeCanvas.create_rectangle(0, 0, width, 100, fill='#707070', width=0)
            ShapeCanvas.create_rectangle(176, 5, 294, height, fill='#707070', width=0)

            DotImage = self.CreateImage('Images/Shapes/dot.png')

            # xPosition

            ShapeCanvas.create_image(25, 25, image=DotImage)

            ShapeCanvas.image = DotImage'''

            '''width = tShapeCanvas.winfo_width()
            height = tShapeCanvas.winfo_height() '''

            self.ImageList = []

            justTImage = self.CreateImage('Images/Shapes/justT2.png')
            ShapeCanvas.create_image(width/2, height/2, anchor=tk.CENTER, image=justTImage)
            self.ImageList.append(justTImage)

            # DotHeight = ((height-100) / y - 1) * 100
            DotHeight = Ycg * height  / (y + b)
            print(f'DotHeight: {DotHeight}')

            DotImage = self.CreateImage('Images/Shapes/dot2.png')

            if Ycg < y:
                ShapeCanvas.create_image(width/2, height - 650, anchor=tk.CENTER, image=DotImage)

            elif Ycg > y:
                ShapeCanvas.create_image(width/2, height - 550, anchor=tk.CENTER, image=DotImage)

            elif Ycg == y:
                ShapeCanvas.create_image(width/2, height - 496, anchor=tk.CENTER, image=DotImage)

            ShapeCanvas.image = DotImage
            self.ImageList.append(DotImage)


        def Discard():
            TopEntry.delete(0, tk.END)
            RightEntry.delete(0, tk.END)
            LeftEntry.delete(0, tk.END)
            BottomEntry.delete(0, tk.END)


        self.ClearMainSpace()
        
        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

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

        self.tShapeImage = self.CreateImage('Images/Shapes/tShape.png')
        tShapeLabel = tk.Label(DataFrame, image=self.tShapeImage, bd=0)
        tShapeLabel.image = self.tShapeImage
        tShapeLabel.pack()

        BottomEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        BottomEntry['validatecommand'] = (Register, '%P', '%d')
        BottomEntry.pack(side=tk.BOTTOM, pady=(25, 50))
        
        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage
        DiscardButton.grid(row=0, column=1, padx=5)

        self.root.bind('<Return>', Calculate)


    def LShape(self):
        pass


    def uShape(self):
        def Calculate():
            x = float(xEntry.get())  
            y = float(yEntry.get())
            a = float(aEntry.get())
            h = float(hEntry.get())

            Ycg = ((2 * (a * y * (y / 2))) + (h * x * (x / 2))) / ((2 * (a * y)) + (x * h))
            Iz = (2 * ((a * y ** 3) / (12)) + ((((x / 2) + (y - x)) - (y - Ycg)) ** 2)) + ((((a + h + a) * (x ** 3)) / (12)) + ((a + h + a) * x * ((Ycg - (x / 2)) ** 2)))
            Iz1 = (2 * ((a * y ** 3) / (12)) + ((((x / 2) + (y - x)) - (y - Ycg)) ** 2))
            Scg = (((y - Ycg) * (a + h + a)) - ((y - Ycg) * (h))) * ((y - Ycg) / 2)

            print(f'x: {x}')
            print(f'y: {y}')
            print(f'a: {a}')
            print(f'h: {h}')
            print(f'Ycg: {Ycg}')
            print(f'Iz: {Iz}')
            print(f'Iz1: {Iz1}')
            print(f'Scg: {Scg}')

        def Discard():
            aEntry.delete(0, tk.END)
            hEntry.delete(0, tk.END)
            xEntry.delete(0, tk.END)
            yEntry.delete(0, tk.END)


        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        TopEntryFrame = tk.Frame(DataFrame, bg='#dbdbdb')
        TopEntryFrame.pack(side=tk.TOP, pady=(50, 25))

        aEntry = tk.Entry(TopEntryFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        aEntry.pack(side=tk.LEFT, padx=(0, 25))

        hEntry = tk.Entry(TopEntryFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        hEntry.pack(side=tk.LEFT, padx=(0, 230))

        xEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        xEntry.pack(side=tk.LEFT, anchor='s', pady=50, padx=30)

        yEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        yEntry.pack(side=tk.RIGHT, anchor='w', padx=30)


        self.uShapeImage = self.CreateImage('Images/Shapes/uShape.png')
        uShapeLabel = tk.Label(DataFrame, image=self.uShapeImage, bd=0)
        uShapeLabel.image = self.uShapeImage
        uShapeLabel.pack()

        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage
        DiscardButton.grid(row=0, column=1, padx=5)


    def cShape(self):
        pass


    def iShape(self):
        def Calculate():
            h = float(HeightEntry.get())
            w = float(WidthEntry.get())

            Ycg = h / 2
            Iz = (w * (h ** 3)) / 12
            Scg = (w * Ycg * (Ycg / 2))

            print(f'Height {str(h)}')
            print(f'Width {str(w)}')
            print(f'Ycg {str(Ycg)}')
            print(f'Iz {str(Iz)}')
            print(f'Scg {str(Scg)}')
            
        
        def Discard():
            WidthEntry.delete(0, tk.END)
            HeightEntry.delete(0, tk.END)


        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        WidthEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        WidthEntry.pack(side=tk.TOP, pady=(50, 25))

        HeightEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        HeightEntry.pack(side=tk.RIGHT, anchor='n', pady=300, padx=30)

        self.iShapeImage = self.CreateImage('Images/Shapes/iShape.png')
        iShapeLabel = tk.Label(DataFrame, image=self.iShapeImage, bd=0)
        iShapeLabel.image = self.iShapeImage
        iShapeLabel.pack(padx=(360, 0))

        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage
        DiscardButton.grid(row=0, column=1, padx=5)


    def RomanIShape(self):
        def Calculate():
            x = float(xEntry.get())
            y = float(yEntry.get())
            a = float(aEntry.get())
            d = float(dEntry.get())
            h = float(hEntry.get())
            x = float(xEntry.get())

        
        def Discard():
            xEntry.delete(0, tk.END)
            yEntry.delete(0, tk.END)
            aEntry.delete(0, tk.END)
            dEntry.delete(0, tk.END)
            hEntry.delete(0, tk.END)
            rEntry.delete(0, tk.END)

        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        xEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        xEntry.pack(side=tk.TOP, pady=(50, 25))

        LeftFrame = tk.Frame(DataFrame, bg='#dbdbdb')
        LeftFrame.pack(side=tk.LEFT, anchor='s', pady=50, padx=30)

        yEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        yEntry.pack(side=tk.TOP, pady=(0, 245))

        aEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        aEntry.pack(pady=(0, 160))

        dEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        dEntry.pack(side=tk.BOTTOM, pady=(0, 100))

        hEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        hEntry.pack(side=tk.RIGHT, anchor='n', pady=325, padx=30)

        self.RomanIShapeImage = self.CreateImage('Images/Shapes/RomanIShape.png')
        RomanIShapeLabel = tk.Label(DataFrame, image=self.RomanIShapeImage, bd=0)
        RomanIShapeLabel.image = self.RomanIShapeImage
        RomanIShapeLabel.pack()

        rEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        rEntry.pack(pady=(20, 0))

        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        CalculateButton.grid(row=0, column=0, padx=5)

        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage
        DiscardButton.grid(row=0, column=1, padx=5)


def main():
    root = tk.Tk()
    MainProgram(root)
    root.mainloop()


if __name__ == '__main__':
    main()
