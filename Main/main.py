import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
import ctypes
import screeninfo

class MainProgram:
    def __init__(self, master):
        self.root = master
        self.root.title('C-Geo')
        self.root.iconbitmap('Images/c-geo.ico')
        self.root.state('zoomed')

        self.SideFrame = tk.Frame(master, bg='#c9c9c9', width=90, bd=0)
        self.SideFrame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.MainSpace = tk.Frame(master, bg='#dbdbdb', bd=0)
        self.MainSpace.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.EntryFont = Font(family='Arial', size=20)
        self.ResultFont = Font(family='Arial', size=16)
        self.WarningFont = Font(size=50)

        self.ScreenInfo = self.GetScreenInfo()
        self.ScreenResolution = self.ScreenInfo[0]
        self.WindowsZoom = self.ScreenInfo[1]

        self.FibraOptions = (
            "ACIMA",
            "ABAIXO"
        )

        self.OptionSelected = tk.StringVar()
        self.OptionSelected.set(self.FibraOptions[0])

        print(f'\nScreen Info: {self.ScreenInfo}')
        print(f'Zoom Ration: {self.WindowsZoom}')
        print(f'Screen Resolution {self.ScreenResolution}\n')

        self.Register = self.MainSpace.register(self.validate)

        self.root.bind('<Control-Key-1>', self.tShape)
        self.root.bind('<Control-Key-2>', self.LShape)
        self.root.bind('<Control-Key-3>', self.uShape)
        self.root.bind('<Control-Key-4>', self.cShape)
        self.root.bind('<Control-Key-5>', self.iShape)
        self.root.bind('<Control-Key-6>', self.RomanIShape)

        self.SideFramePacking()     


    def GetScreenInfo(self):
        # Pega A Quantidade De Pixels Da Tela (Windows)
        user32 = ctypes.windll.user32
        ScreenRelativeResolution = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

        print(ScreenRelativeResolution)
        print()

        # Pega A Resolução Real Da Tela (Monitor)
        ScreenResolution = screeninfo.get_monitors()[0].width, screeninfo.get_monitors()[0].height

        if ScreenResolution == (1920, 1080):
            if ScreenRelativeResolution == ScreenResolution:
                ZoomRatio = 100

            elif ScreenRelativeResolution == (1536, 864):
                ZoomRatio = 125

            elif ScreenRelativeResolution == (1280, 720):
                ZoomRatio = 150

            else:
                ZoomRatio = 0

        elif ScreenResolution == (1280, 720):
            if ScreenRelativeResolution == ScreenRelativeResolution:
                ZoomRatio = 150

            else:
                ZoomRatio = 100

        return ScreenResolution, ZoomRatio


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
        ImageWidth, ImageHeight = ImageFile.size
        
        if self.WindowsZoom == 100:
            xSize = ImageWidth
            ySize = ImageHeight

        elif self.WindowsZoom == 125:
            xSize = ImageWidth - (ImageWidth * 0.25)
            ySize = ImageHeight - (ImageHeight * 0.25)

        elif self.WindowsZoom == 150:
            xSize = ImageWidth - (ImageWidth * 0.50)
            ySize = ImageHeight - (ImageHeight * 0.50)

        elif self.WindowsZoom == 175:
            xSize = ImageWidth - (ImageWidth * 0.75)
            ySize = ImageHeight - (ImageHeight * 0.75)

        TkImage = ImageTk.PhotoImage(ImageFile.resize((int(xSize), int(ySize)), Image.ANTIALIAS))
        
        return TkImage


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


    def tShape(self, event=None):
        def Calculate(event=None):
            def get_fibra():
                fibra = float(FibraEntry.get())
                option = self.OptionSelected.get()    

                sLabel['fg'] = '#404040'

                if ((option == 'ACIMA') and (Ycg + fibra <= y + b)) or ((option == 'ABAIXO') and (Ycg - fibra >= 0)):
                    if Ycg > y:
                        if option == 'ABAIXO':
                            if Ycg - fibra < y:
                                h = Ycg - fibra
                                S = h * z * ((h / 2) + fibra)
                                print('1')
                            
                            elif Ycg - fibra > y:
                                d = Ycg - fibra - y
                                S = (d * x * ((d / 2) + fibra)) + (y * z * ((y / 2) + d + fibra))
                                print('2')

                            elif Ycg - fibra == y:
                                S = y * z * (y / 2) + fibra
                                print('3')

                        elif option == 'ACIMA':
                            if Ycg + fibra < ( y + b):
                                i = y + b  - (Ycg + fibra)
                                S = i * x * ((i / 2) + fibra)
                                    
                            print('4')

                    elif Ycg < y:
                        if option == 'ACIMA':
                            if (Ycg + fibra) == y:
                                S = b * x * ((b / 2) + fibra)

                            elif (Ycg + fibra) < y:
                                i = y - (Ycg + fibra)
                                S = (b * x * ((b / 2 )+ (fibra + i))) + (i * z * ((i/2) + fibra))

                            elif (Ycg + fibra) > y: 
                                a = (y + b) - (Ycg + fibra)
                                S = a * x * ((a/2) + fibra)        

                         
                        elif option == 'ABAIXO':
                            if (Ycg - fibra < y):
                                d = Ycg - fibra
                                S = d * z * ((d / 2 ) + fibra)
                                print('5')
                        
                    elif Ycg == y:
                        if option == 'ACIMA':
                            if (Ycg + fibra) > y:
                                a = b - fibra
                                S = a * x * ((a / 2) + fibra)
                        
                            print('6')
                        
                        elif option == 'ABAIXO':
                            if (Ycg - fibra) < y:
                                a = Ycg - fibra
                                S = a * z * ((a / 2) + fibra) 

                        print('7')

                    sLabel['text'] = S

                else:
                    sLabel['fg'] = '#eb4034'
                    sLabel['text'] = 'NÃO É POSSÍVEL CALCULAR'
                    print('8')


            # Converte Os Valores Das Caixas De Entrada
            x = float(TopEntry.get())
            b = float(LeftEntry.get())
            y = float(RightEntry.get())
            z = float(BottomEntry.get())

            self.ClearMainSpace()

            # Fórmulas
            Ycg = (z * y * (y / 2) + b * x * (y + (b / 2))) / (z * y + b * x)
            Iz = (((x * (b ** 3)) / (12) ) + (b * x * ((y + (b / 2) - Ycg)) ** 2)) + (((z * (y ** 3)) / (12)) + (y * z * ((Ycg - (y / 2)) ** 2)))
            
            if Ycg < y or Ycg == y:
                Scg = (Ycg * z * (Ycg / 2))
            
            else:
                Scg = x * (y + b - Ycg) * ((y + b - Ycg) / 2)
                
            # Cria Os Frames Principais
            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)

            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=0)
            FibraFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=0, padx=20, pady=20)
            
            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            ResultFrame.grid(row=0, column=0, padx=50, pady=50)
            FibraFrame.grid(row=1, column=0, padx=50, pady=50)

            # Cria Os Widgets Para O ResultFrame 
            YcgLabel = tk.Label(ResultFrame, text='Ycg =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            YcgLabelContent = tk.Label(ResultFrame, text=str(f'{Ycg:.2f} cm'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            IzLabel = tk.Label(ResultFrame, text='Iz =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            IzLabelContent = tk.Label(ResultFrame, text=str(f'{Iz:.2f} cm⁴'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            ScgLabel = tk.Label(ResultFrame, text='Scg =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            ScgLabelContent = tk.Label(ResultFrame, text=str(f'{Scg:.2f} cm³'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')

            # Layout Dos Widgets Do Frame Resultado
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=5, sticky='w')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=5, sticky='w')
            ScgLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')
            
            # Cria Os Widgets Para O FibraFrame
            FibraLabel = tk.Label(FibraFrame, text='Digite Sua Fibra', font=self.ResultFont, fg='#404040', bg='#b0b0b0')
            FibraEntry = tk.Entry(FibraFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER)
            jLabel = tk.Label(FibraFrame, text='POSIÇÃO:', font=self.ResultFont, fg='#404040', bg='#b0b0b0')

            jDrop = tk.OptionMenu(FibraFrame, self.OptionSelected, *self.FibraOptions)
            jDrop.configure(fg='#121212', bg='#808080', bd=0, highlightthickness=0)            

            sLabel = tk.Label(FibraFrame, text='-----', font=self.ResultFont, fg='#404040', bg='#b0b0b0')
            FibraButton = tk.Button(FibraFrame, text='CALCULAR', fg='#121212', bg='#808080', bd=0, command=get_fibra)

            # Layout Dos Widgets De FibraFrame
            FibraLabel.grid(row=0, column=0, columnspan=2)
            FibraEntry.grid(row=1, column=0, pady=15, columnspan=2)
            jLabel.grid(row=2, column=0)
            jDrop.grid(row=2, column=1)
            sLabel.grid(row=3, column=0, columnspan=2)
            FibraButton.grid(row=4, column=0, columnspan=2)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            xLabel = tk.Label(ValueFrame, text=f'x = {x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            bLabel = tk.Label(ValueFrame, text=f'b = {b} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            yLabel = tk.Label(ValueFrame, text=f'y = {y} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            zLabel = tk.Label(ValueFrame, text=f'z = {z} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')

            # Layout Dos Widgets Do ValueFrame  
            xLabel.pack(side=tk.TOP, pady=(50, 5))
            bLabel.pack(side=tk.LEFT, anchor='ne', pady=100)
            yLabel.pack(side=tk.RIGHT, anchor='w', pady=100)
            zLabel.pack(side=tk.BOTTOM)


            # Cria O Canvas Da Imagem Principal
            CanvasWidth = 694
            CanvasHeight = 844
            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()
            
            # Cria As Imagens No Canvas
            self.ImageList = []
            justTImage = self.CreateImage('Images/Shapes/tValues.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=justTImage)
            self.ImageList.append(justTImage)

            if Ycg < y:
                DotHeight = CanvasHeight - 650
                
            elif Ycg > y:
                DotHeight = CanvasHeight - 720

            elif Ycg == y:
                DotHeight = CanvasHeight - 496
                
            DotImage = self.CreateImage('Images/Shapes/dot.png')
            ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(DotImage)

            x1 = 158; y1 = DotHeight; x2 = x1 + 9; y2 = CanvasHeight - 50

            # Cria A Linha Do Ycg
            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)
            ShapeCanvas.create_text(153, 844 - 50, text='Ycg', font=self.ResultFont, fill='#303030', anchor='se')


        def Discard():
            TopEntry.delete(0, tk.END)
            RightEntry.delete(0, tk.END)
            LeftEntry.delete(0, tk.END)
            BottomEntry.delete(0, tk.END)


        self.ClearMainSpace()
        
        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        TopEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        TopEntry['validatecommand'] = (self.Register, '%P', '%d')
        TopEntry.pack(side=tk.TOP, pady=(50, 25)) 

        RightEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        RightEntry['validatecommand'] = (self.Register, '%P', '%d')
        RightEntry.pack(side=tk.RIGHT, anchor='w', padx=30)

        LeftEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        LeftEntry['validatecommand'] = (self.Register, '%P', '%d')
        LeftEntry.pack(side=tk.LEFT, anchor='n', pady=75, padx=30)

        self.tShapeImage = self.CreateImage('Images/Shapes/tShape.png')
        tShapeLabel = tk.Label(DataFrame, image=self.tShapeImage, bd=0)
        tShapeLabel.image = self.tShapeImage
        tShapeLabel.pack()

        BottomEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        BottomEntry['validatecommand'] = (self.Register, '%P', '%d')
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


    def LShape(self, event=None):
        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        self.LShapeImage = self.CreateImage('Images/Shapes/LShape.png')
        LShapeLabel = tk.Label(DataFrame, image=self.LShapeImage, bd=0)
        LShapeLabel.image = self.LShapeImage
        LShapeLabel.pack()

        WarningLabel = tk.Label(DataFrame, text='EM BREVE', font=self.WarningFont, fg='#8c8c8c', bg='#dbdbdb')
        WarningLabel.pack()


    def uShape(self, event=None):
        def Calculate(event=None):
            def get_fibra():
                fibra = float(FibraEntry.get())
                option = self.OptionSelected.get()
                sLabel['fg'] = '#404040'

                if ((option == 'ACIMA') and (Ycg + fibra <= y)) or ((option == 'ABAIXO') and (Ycg - fibra >= 0)):
                    if Ycg > x:
                        if option == 'ACIMA':
                            if (Ycg + fibra) < y:
                                m = y - (Ycg + fibra)
                                S = m * (a + h + a) * ((m / 2) + fibra)

                        elif option == 'ABAIXO':
                            if (Ycg - fibra) > x: 
                                i =(Ycg - x) - fibra 
                                S = (x * (h + a + a) * ((x / 2) + i + fibra)) + ( 2 * (i * a * ((i / 2) + fibra)))

                            elif (Ycg - fibra) <= (x):
                                m = Ycg - fibra
                                S = m * (h + a + a) * ((m / 2 ) + fibra)

                    elif (Ycg < x):
                        if option == 'ABAIXO':
                            if(Ycg - fibra) < (x):
                                i = Ycg - fibra
                                S = i * (a + a + h) * ((i / 2) + fibra)

                        elif option == 'ACIMA':
                            if (Ycg + fibra) >= x:
                                m = y - (Ycg + fibra) 
                                S = 2 * ( m * a * ((m / 2) + fibra))       

                            elif (Ycg + fibra) < x:
                                v = y - x
                                m = (Ycg + fibra) - x 
                                S = (m * (a + h + a) * ((m / 2)+ fibra)) + (2 * (a * v * ((v / 2) + fibra + m)))


                    elif (Ycg == x):
                        if option=='ABAIXO':
                            if (Ycg - fibra) <= x:
                                i = Ycg - fibra
                                S = (h + a + a) * i * ((i / 2) + fibra)

                        elif option == 'ACIMA':
                            if ( Ycg + fibra) >= x:
                                v = (Ycg + fibra)
                                S = (v * a * ((v / 2) + fibra)) * 2 

                    sLabel['text'] = str(S) + "cm³"

                else:
                    sLabel['fg'] = '#eb4034'
                    sLabel['text'] = 'NÃO É POSSÍVEL CALCULAR'


            def change_stringvar(option):
                print(option)
            
            # Converte Os Valores Das Caixas De Entrada
            x = float(xEntry.get())  
            y = float(yEntry.get())
            a = float(a1Entry.get())
            h = float(hEntry.get())

            self.ClearMainSpace()

            # Fórmulas
            Ycg = ((2 * (a * y * (y / 2))) + (h * x * (x / 2))) / ((2 * (a * y)) + (x * h))
            Iz = (2 * (((a * y ** 3) / (12)) + ((y * a * ((y / 2) - Ycg) ** 2)))) + ((((h) * (x ** 3)) / (12)) + (x * h * ((Ycg - (x / 2)) ** 2)))
            Scg = (((y - Ycg) * (a + h + a)) - ((y - Ycg) * (h))) * ((y - Ycg) / 2)

            # Cria Os Frames Principais
            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)

            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#b0b0b0')
            FibraFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=0, padx=20, pady=20)

            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            ResultFrame.grid(row=0, column=0, padx=50, pady=50)
            FibraFrame.grid(row=1, column=0, padx=50, pady=50)

            # Cria Os Widgets Para O ResultFrame 
            YcgLabel = tk.Label(ResultFrame, text='Ycg =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            YcgLabelContent = tk.Label(ResultFrame, text=str(f'{Ycg:.2f} cm'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            IzLabel = tk.Label(ResultFrame, text='Iz =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            IzLabelContent = tk.Label(ResultFrame, text=str(f'{Iz:.2f} cm⁴'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            ScgLabel = tk.Label(ResultFrame, text='Scg =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            ScgLabelContent = tk.Label(ResultFrame, text=str(f'{Scg:.2f} cm³'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            
            # Layout Dos Widgets Do Frame Resultado
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=5, sticky='w')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=5, sticky='w')
            ScgLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')

            # Cria Os Widgets Para O FibraFrame
            FibraLabel = tk.Label(FibraFrame, text='Distância Da Fibra Em Relação Ao cg', font=self.ResultFont, fg='#404040', bg='#b0b0b0')
            FibraEntry = tk.Entry(FibraFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER)
            FibraButton = tk.Button(FibraFrame, text='CALCULAR', fg='#121212', bg='#808080', bd=0, command=get_fibra)
            jLabel = tk.Label(FibraFrame, text='Posição Da Fibra:', font=self.ResultFont, fg='#404040', bg='#b0b0b0')
            
            jDrop = tk.OptionMenu(FibraFrame, self.OptionSelected, *self.FibraOptions, command=change_stringvar)
            jDrop.configure(fg='#121212', bg='#808080', bd=0, highlightthickness=0)

            sLabel = tk.Label(FibraFrame, text='-----', font=self.ResultFont, fg='#404040', bg='#b0b0b0')

            # Layout Dos Widgets De FibraFrame
            FibraLabel.grid(row=0, column=0, columnspan=2)
            FibraEntry.grid(row=1, column=0, pady=15, columnspan=2)
            FibraButton.grid(row=2, column=0, columnspan=2)
            jLabel.grid(row=3, column=0)
            jDrop.grid(row=3, column=1)
            sLabel.grid(row=4, column=0, columnspan=2)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            TopLabelFrame = tk.Frame(ValueFrame, bg='#dbdbdb')
            a1Label = tk.Label(TopLabelFrame, text=f'a = {a} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            a2Label = tk.Label(TopLabelFrame, text=f'a = {a} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgL = tk.Label(ValueFrame, text='Ycg', font=self.ResultFont, bg='#dbdbdb', fg='#121212')
            hLabel = tk.Label(ValueFrame, text=f'h = {h} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')

            RightLabelFrame = tk.Frame(ValueFrame, bg='#dbdbdb')

            yLabel = tk.Label(RightLabelFrame, text=f'y = {y - x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            xLabel = tk.Label(RightLabelFrame, text=f'x = {x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')

            # Layout Dos Widgets Do ValueFrame  
            TopLabelFrame.pack(side=tk.TOP)
            a1Label.pack(side=tk.LEFT, padx=(0, 170))
            a2Label.pack(side=tk.RIGHT, padx=(170, 0))
            YcgL.pack(side=tk.LEFT, anchor='se', padx=(70, 0), pady=70)
            RightLabelFrame.pack(side=tk.RIGHT, anchor='w', fill=tk.Y)
            yLabel.pack(anchor='w', pady=(350, 0))
            xLabel.pack(side=tk.BOTTOM, anchor='w', pady=(0, 150))
            hLabel.pack(side=tk.BOTTOM)
            
            # Cria O Canvas Da Imagem Principal
            CanvasWidth = 702
            CanvasHeight = 840
            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()

            # Cria As Imagens No Canvas
            self.ImageList = []
            uValuesImage = self.CreateImage('Images/Shapes/uValues.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=uValuesImage)
            self.ImageList.append(uValuesImage)
            DotImage = self.CreateImage('Images/Shapes/dot.png')

            if Ycg < x:
                DotHeight = CanvasHeight - 145
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            elif Ycg > x:
                DotHeight = CanvasHeight - 350
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            elif Ycg == x:
                DotHeight = CanvasHeight - 190
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            self.ImageList.append(DotImage)

            # Cria A Linha Do Ycg
            x1 = 15; y1 = DotHeight; x2 = x1 + 9; y2 = 799
            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)


        def Discard():
            a1Entry.delete(0, tk.END)
            a2Entry.delete(0, tk.END)
            hEntry.delete(0, tk.END)
            xEntry.delete(0, tk.END)
            yEntry.delete(0, tk.END)

        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        TopEntryFrame = tk.Frame(DataFrame, bg='#dbdbdb')
        TopEntryFrame.pack(side=tk.TOP, pady=(50, 25))

        a1Entry = tk.Entry(TopEntryFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        a1Entry['validatecommand'] = (self.Register, '%P', '%d')
        a1Entry.pack(side=tk.LEFT, padx=30)

        a2Entry = tk.Entry(TopEntryFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        a2Entry['validatecommand'] = (self.Register, '%P', '%d')
        a2Entry.pack(side=tk.RIGHT, padx=30)        

        xEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        xEntry['validatecommand'] = (self.Register, '%P', '%d')
        xEntry.pack(side=tk.LEFT, anchor='s', pady=(0, 140), padx=30)

        yEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        yEntry['validatecommand'] = (self.Register, '%P', '%d')
        yEntry.pack(side=tk.RIGHT, anchor='w', padx=30)

        self.uShapeImage = self.CreateImage('Images/Shapes/uShape.png')
        uShapeLabel = tk.Label(DataFrame, image=self.uShapeImage, bd=0)
        uShapeLabel.image = self.uShapeImage
        uShapeLabel.pack()

        hEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        hEntry['validatecommand'] = (self.Register, '%P', '%d')
        hEntry.pack(pady=(30, 0))

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


    def cShape(self, event=None):
        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        self.cShapeImage = self.CreateImage('Images/Shapes/cShape.png')
        cShapeLabel = tk.Label(DataFrame, image=self.cShapeImage, bd=0)
        cShapeLabel.image = self.cShapeImage
        cShapeLabel.pack()

        WarningLabel = tk.Label(DataFrame, text='EM BREVE', font=self.WarningFont, fg='#8c8c8c', bg='#dbdbdb')
        WarningLabel.pack()


    def iShape(self, event=None):
        def Calculate(event=None):
            def get_fibra():
                fibra = float(FibraEntry.get())
                sLabel['fg'] = '#404040'

                if fibra < (h / 2):
                    if fibra == (h / 2):
                        S = 0

                    elif fibra == 0:
                        S = Scg

                    S = ((Ycg - fibra) * w) * (((Ycg - fibra) / 2) + fibra)
                    sLabel['text'] = S

                else:
                    S = 0
                    sLabel['fg'] = '#eb4034'
                    sLabel['text'] = 'NÃO É POSSÍVEL CALCULAR'


            # Converte Os Valores Das Caixas De Entrada
            h = float(HeightEntry.get())
            w = float(WidthEntry.get())

            self.ClearMainSpace()

            # Fórmulas
            Ycg = h / 2
            Iz = (w * (h ** 3)) / 12
            Scg = (w * Ycg * (Ycg / 2))

            # Cria Os Frames Principais
            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            
            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, anchor='n')
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=0)
            FibraFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=0, padx=20, pady=20)

            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            ResultFrame.grid(row=0, column=0, padx=50, pady=50)
            FibraFrame.grid(row=1, column=0, padx=50, pady=50)

            # Cria Os Widgets Para O ResultFrame 
            YcgLabel = tk.Label(ResultFrame, text='Ycg =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            YcgLabelContent = tk.Label(ResultFrame, text=str(f'{Ycg:.2f} cm'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            IzLabel = tk.Label(ResultFrame, text='Iz =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            IzLabelContent = tk.Label(ResultFrame, text=str(f'{Iz:.2f} cm⁴'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            ScgLabel = tk.Label(ResultFrame, text='Scg =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            ScgLabelContent = tk.Label(ResultFrame, text=str(f'{Scg:.2f} cm³'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
                
            # Layout Dos Labels Do Frame Resultado
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=5, sticky='w')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=5, sticky='w')
            ScgLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')

            # Cria Os Widgets Para O FibraFrame
            FibraLabel = tk.Label(FibraFrame, text='Qual A Distância Da Sua Fibra Em Relação Ao cg?', font=self.ResultFont, fg='#404040', bg='#b0b0b0')
            FibraEntry = tk.Entry(FibraFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
            FibraButton = tk.Button(FibraFrame, text='CALCULAR', fg='#121212', bg='#808080', bd=0, command=get_fibra)
            sLabel = tk.Label(FibraFrame, text='-----', font=self.ResultFont, fg='#404040', bg='#b0b0b0')

            # Teste De Validação
            FibraEntry['validatecommand'] = (self.Register, '%P', '%d')

            # Layout Dos Widgets De FibraFrame
            FibraLabel.grid(row=0, column=0)
            FibraEntry.grid(row=1, column=0, pady=15)
            FibraButton.grid(row=2, column=0)
            sLabel.grid(row=3, column=0)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            wLabel = tk.Label(ValueFrame, text=f'x = {w} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            hLabel = tk.Label(ValueFrame, text=f'y = {h} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            YcgL = tk.Label(ValueFrame, text='Ycg', font=self.ResultFont, bg='#dbdbdb', fg='#303030')

            # Layout Dos Widgets Do ValueFrame
            wLabel.pack(side=tk.TOP)
            hLabel.pack(side=tk.RIGHT)
            YcgL.pack(side=tk.LEFT, anchor='se', padx=(70, 0), pady=20)

            # Cria O Canvas Da Imagem Principal
            CanvasWidth = 265
            CanvasHeight = 819
            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()            

            # Cria As Imagens No Canvas
            self.ImageList = []
            iValuesImage = self.CreateImage('Images/Shapes/iValues.png')
            DotImage = self.CreateImage('Images/Shapes/dot.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=iValuesImage)
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(iValuesImage)
            self.ImageList.append(DotImage)

            # Cria A Linha Do Ycg
            x1 = 18; y1 = CanvasHeight / 2; x2 = x1 + 9; y2 = 796
            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)


        def Discard():
            WidthEntry.delete(0, tk.END)
            HeightEntry.delete(0, tk.END)


        self.ClearMainSpace()

        # Cria Os Widgets Do self.MainSpace
        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)

        # Layout Dos Widgets Do self.MainSpace
        DataFrame.pack(expand=True)
        MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

        # Cria Os Widgets Do DataFrame
        WidthEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        HeightEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')

        self.iShapeImage = self.CreateImage('Images/Shapes/iShape.png')
        iShapeLabel = tk.Label(DataFrame, image=self.iShapeImage, bd=0)
        iShapeLabel.image = self.iShapeImage

        # Teste De Validação Destes Widgets
        WidthEntry['validatecommand'] = (self.Register, '%P', '%d')
        HeightEntry['validatecommand'] = (self.Register, '%P', '%d')

        # Layout Dos Widgets Do DataFrame
        WidthEntry.pack(side=tk.TOP, pady=(50, 25))
        HeightEntry.pack(side=tk.RIGHT, anchor='n', pady=300, padx=30)
        iShapeLabel.pack(padx=(360, 0))

        ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
        ButtonsFrame.pack()

        # Widgets De ButtonsFrame
        CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        CalculateButton = tk.Button(ButtonsFrame, image=CalculateImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Calculate)
        CalculateButton.image = CalculateImage
        
        DiscardImage = self.CreateImage('Images/Buttons/discard.png')
        DiscardButton = tk.Button(ButtonsFrame, image=DiscardImage, bg='#dbdbdb', activebackground='#dbdbdb', bd=0, command=Discard)
        DiscardButton.image = DiscardImage

        # Layout Dos Widgets
        CalculateButton.grid(row=0, column=0, padx=5)
        DiscardButton.grid(row=0, column=1, padx=5)

        self.root.bind('<Return>', Calculate)


    def RomanIShape(self, event=None):
        def Calculate(event=None):
            def get_fibra():
                fibra = float(FibraEntry.get())
                option = self.OptionSelected.get()
                sLabel['fg'] = '#404040'

                if ((option == 'ACIMA') and (Ycg + fibra <= y + d + h)) or ((option == 'ABAIXO') and (Ycg - fibra >= 0)):
                    if Ycg >= (h + d):
                        if option == 'ACIMA':
                            if (Ycg + fibra) < (y + d + h):
                            	i = ((Ycg + fibra) - (y + h + d))
                            	S = i * x * ((i/2) + fibra)

                        elif option == 'ABAIXO':
                            if ( Ycg - fibra) <= (d + h) and (Ycg - fibra) > (d):
                                i = ( d + h) - (Ycg - fibra)
                                S = ((i * a * ((i / 2) + fibra)) + (d * r * ((d / 2) + i + fibra)))

                            elif (Ycg - fibra) <= (d):
                                u = ( Ycg - fibra)  
                                S = u * r * ((u / 2) + fibra)

                            elif (Ycg - fibra) > (d + h):    
                                u = (Ycg - fibra) - (h + d)
                                S = (u * x * ((u / 2 ) + fibra)) + (h * a * ((h / 2) + u + fibra)) + d * r * ((d / 2) + h + u + fibra)

                    elif ( Ycg > d ) and Ycg <= ( d + h):     
                        if option =='ACIMA':      
                        	if (Ycg + fibra) >= (d + h):
                        	    i = ( d + h + y) - (Ycg + fibra)
                        	    S = i * x * ((i / 2) + fibra)
                        	
                        	elif (Ycg + fibra) <= ( d + h) and (Ycg + fibra) >= (d):
                        	    i = (d + h) - (Ycg + fibra)
                        	    S = (y * x * ((y / 2) + i + fibra)) + (i * a * ((i / 2) + fibra))

                        elif option == 'ABAIXO':
                            if (Ycg - fibra) > (d):
                                v = (d + h) - ( Ycg - fibra)    
                                S = (v * a * ((v / 2) + fibra)) + (d * r * ((d / 2) + fibra))

                            elif (Ycg - fibra) <= (d): 
                                v = (Ycg - fibra)
                                S = v * r * ((v / 2) + fibra)

                    elif ( Ycg <= d ):
                        if option == 'ABAIXO':
                        	if ( Ycg - fibra) <= (d):
                        	    g = (Ycg - fibra)
                        	    S = g * r * ((g / 2)+ fibra)

                        elif option == 'ACIMA':
                        	if (Ycg + fibra) >= (d + h):
                        	    i = (d + h + fibra) - (Ycg + fibra)
                        	    S = (i * x * ((i / 2)+ fibra))

                        	elif (Ycg + fibra) >= (d):
                        	    m = (h + d) - (Ycg + fibra)    
                        	    S = y * x * ((y / 2) + fibra)

                        	elif (Ycg + fibra) < (d):   
                        	    m = (d) - (Ycg + fibra)
                        	    S = (y * x * ((y / 2) + h + m + fibra)) + (h * a * ((h / 2) + m + fibra)) + (m * r * ((m / 2) + fibra)) 
                    
                    sLabel['text'] = str(S) + "cm³"

                else:
                    sLabel['fg'] = '#eb4034'
                    sLabel['text'] = 'NÃO É POSSÍVEL CALCULAR'

            # Converte Os Valores Das Caixas De Entrada
            x = float(xEntry.get())
            y = float(yEntry.get())
            a = float(aEntry.get())
            d = float(dEntry.get())
            h = float(hEntry.get())
            x = float(xEntry.get())
            r = float(rEntry.get())

            self.ClearMainSpace()

            # Fórmulas
            Ycg = ((a * r * (a / 2)) + (h * d * (a + (h / 2))) + (y * x * (a + h + (y / 2)))) / ((a * r) + (d * h) + (y * x))
            Iz = (((r * (a ** 3)) / (12)) + ((a * r * (((Ycg - (a / 2)) ** 2))))) + (((d * (h ** 3)) / 12) + (h * d * ((((h / 2) + a) - (Ycg)) ** 2))) + (((x * (y ** 3)) / 12) + (y * x * (((a + h + (y / 2)) - Ycg) ** 2)))
            
            if Ycg == a:
                print('Primeira Fórmula')
                Scg = a * r * (a / 2)

            elif Ycg == (a + h):
                print('Segunda Fórmula')
                Scg = y * x * (y / 2)

            elif Ycg < (a + h) and Ycg > a:
                print('Terceira Fórmula')
                Scg = (a * r * (Ycg - (a / 2))) + (d * (Ycg - a) * ((Ycg - a) / 2))

            # Cria Os Frames Principais
            LeftFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0)
            
            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#b0b0b0')
            FibraFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=0, padx=20, pady=20)

            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            ResultFrame.grid(row=0, column=0, padx=50, pady=50)
            FibraFrame.grid(row=1, column=0, padx=50, pady=50)

            # Cria Os Widgets Para O ResultFrame 
            YcgLabel = tk.Label(ResultFrame, text='Ycg =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            YcgLabelContent = tk.Label(ResultFrame, text=str(f'{Ycg:.2f} cm'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            IzLabel = tk.Label(ResultFrame, text='Iz =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            IzLabelContent = tk.Label(ResultFrame, text=str(f'{Iz:.2f} cm⁴'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            ScgLabel = tk.Label(ResultFrame, text='Scg =', font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            ScgLabelContent = tk.Label(ResultFrame, text=str(f'{Scg:.2f} cm³'), font=self.ResultFont, bg='#b0b0b0', fg='#303030')
            
            # Layout Dos Widgets Do Frame Resultado
            YcgLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            YcgLabelContent.grid(row=0, column=1, padx=10, pady=5, sticky='w')
            IzLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            IzLabelContent.grid(row=1, column=1, padx=10, pady=5, sticky='w')
            ScgLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            ScgLabelContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')
            
            # Cria Os Widgets Para O FibraFrame
            FibraLabel = tk.Label(FibraFrame, text='Digite Sua Fibra', font=self.ResultFont, fg='#404040', bg='#b0b0b0')
            FibraEntry = tk.Entry(FibraFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER)
            jLabel = tk.Label(FibraFrame, text='POSIÇÃO:', font=self.ResultFont, fg='#404040', bg='#b0b0b0')
            jDrop = tk.OptionMenu(FibraFrame, self.OptionSelected, *self.FibraOptions)
            jDrop.configure(fg='#121212', bg='#808080', bd=0, highlightthickness=0) 

            sLabel = tk.Label(FibraFrame, text='-----', font=self.ResultFont, fg='#404040', bg='#b0b0b0')
            FibraButton = tk.Button(FibraFrame, text='CALCULAR', fg='#121212', bg='#808080', bd=0, command=get_fibra)

            # Layout Dos Widgets De FibraFrame
            FibraLabel.grid(row=0, column=0, columnspan=2)
            FibraEntry.grid(row=1, column=0, pady=15, columnspan=2)
            jLabel.grid(row=2, column=0)
            jDrop.grid(row=2, column=1)
            sLabel.grid(row=3, column=0, columnspan=2)
            FibraButton.grid(row=4, column=0, columnspan=2)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            xLabel = tk.Label(ValueFrame, text=f'x = {x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            aLabel = tk.Label(ValueFrame, text=f'a = {a} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            rLabel = tk.Label(ValueFrame, text=f'r = {r} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')

            RightValueFrame = tk.Frame(ValueFrame, bg='#dbdbdb')
            
            yLabel = tk.Label(RightValueFrame, text=f'y = {y} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            hLabel = tk.Label(RightValueFrame, text=f'h = {h} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            dLabel = tk.Label(RightValueFrame, text=f'd = {d} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')

            # Layout Dos Widgets Do ValueFrame  
            xLabel.pack(side=tk.TOP, pady=(50, 5))
            aLabel.pack(side=tk.LEFT, pady=(0, 40))
            RightValueFrame.pack(side=tk.RIGHT, fill=tk.Y)
            yLabel.pack(side=tk.TOP, anchor='w', pady=(100, 0))
            hLabel.pack(anchor='w', pady=(290, 0))
            dLabel.pack(side=tk.BOTTOM, anchor='w', pady=(0, 120))
            rLabel.pack(side=tk.BOTTOM)
           
            # Cria O Canvas Da Imagem Principal
            CanvasWidth = 496
            CanvasHeight = 820
            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()

            # Cria As Imagens No Canvas
            self.ImageList = []
            RomanIValuesImage = self.CreateImage('Images/Shapes/RomanIValues.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=RomanIValuesImage)
            self.ImageList.append(RomanIValuesImage)

            if Ycg > (h + d):
                DotHeight = CanvasHeight - 708
                
            elif Ycg == (h + d):
                DotHeight = CanvasHeight - 632
            
            elif ((y + h + d) / 2) < Ycg < (h + d):
                DotHeight = CanvasHeight - 522

            elif Ycg == ((y + h + d) / 2):
                DotHeight = CanvasHeight - 411

            elif Ycg == ((h + d) / 2):
                DotHeight = CanvasHeight - 336

            elif d < Ycg < ((y + d + h) / 2):
                DotHeight = CanvasHeight - 299
            
            elif Ycg == d:
                DotHeight = CanvasHeight - 189

            elif Ycg < d:
                DotHeight = CanvasHeight - 94

            DotImage = self.CreateImage('Images/Shapes/dot.png')
            ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(DotImage)

            x1 = 283; y1 = DotHeight; x2 = x1 + 9; y2 = CanvasHeight - 37

            # Cria A Linha Do Ycg
            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)
            ShapeCanvas.create_text(x2 + 10, y2, text='Ycg', font=self.ResultFont, fill='#303030', anchor='sw')

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

        xEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        xEntry['validatecommand'] = (self.Register, '%P', '%d')
        xEntry.pack(side=tk.TOP, pady=(50, 25))

        LeftFrame = tk.Frame(DataFrame, bg='#dbdbdb')
        LeftFrame.pack(side=tk.LEFT, anchor='s', pady=50, padx=30)

        yEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        yEntry['validatecommand'] = (self.Register, '%P', '%d')
        yEntry.pack(side=tk.TOP, pady=(0, 245))

        aEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        aEntry['validatecommand'] = (self.Register, '%P', '%d')
        aEntry.pack(pady=(0, 160))

        dEntry = tk.Entry(LeftFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.RIGHT, validate='key')
        dEntry['validatecommand'] = (self.Register, '%P', '%d')
        dEntry.pack(side=tk.BOTTOM, pady=(0, 100))

        hEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.LEFT, validate='key')
        hEntry['validatecommand'] = (self.Register, '%P', '%d')
        hEntry.pack(side=tk.RIGHT, anchor='n', pady=325, padx=30)

        self.RomanIShapeImage = self.CreateImage('Images/Shapes/RomanIShape.png')
        RomanIShapeLabel = tk.Label(DataFrame, image=self.RomanIShapeImage, bd=0)
        RomanIShapeLabel.image = self.RomanIShapeImage
        RomanIShapeLabel.pack()

        rEntry = tk.Entry(DataFrame, font=self.EntryFont, bg='#bfbfbf', fg='#303030', bd=0, justify=tk.CENTER, validate='key')
        rEntry['validatecommand'] = (self.Register, '%P', '%d')
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

        self.root.bind('<Return>', Calculate)


def main():
    root = tk.Tk()
    MainProgram(root)
    root.mainloop()


if __name__ == '__main__':
    main()
