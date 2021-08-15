import tkinter as tk
from tkinter.constants import Y
from tkinter.font import Font
from PIL import ImageTk, Image
import ctypes
import screeninfo
from sections import tSection, lSection, uSection, iSection, hSection
from win_fibra import FibraWindow
import widgets

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

        self.EntryFont = Font(family='Calibri', size=20)
        self.ResultFont = Font(family='Calibri', size=16)
        self.WarningFont = Font(size=50)

        self.ScreenInfo = self.GetScreenInfo()
        self.ScreenResolution = self.ScreenInfo[0]
        self.WindowsZoom = self.ScreenInfo[1]

        self.OptionSelected = tk.StringVar()

        print(f'\nScreen Info: {self.ScreenInfo}')
        print(f'Zoom Ration: {self.WindowsZoom}')
        print(f'Screen Resolution {self.ScreenResolution}\n')

        self.root.bind('<Control-Key-1>', self.tShape)
        self.root.bind('<Control-Key-2>', self.LShape)
        self.root.bind('<Control-Key-3>', self.uShape)
        self.root.bind('<Control-Key-4>', self.cShape)
        self.root.bind('<Control-Key-5>', self.iShape)
        self.root.bind('<Control-Key-6>', self.hShape)

        self.InitImages()
        self.SideFramePacking()     


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
    
    
    def InitImages(self):
        # Side Button
        self.tButtonImage = self.CreateImage('Images/Buttons/tButton.png')
        self.LButtonImage = self.CreateImage('Images/Buttons/LButton.png')
        self.uButtonImage = self.CreateImage('Images/Buttons/uButton.png')
        self.cButtonImage = self.CreateImage('Images/Buttons/cButton.png')
        self.iButtonImage = self.CreateImage('Images/Buttons/iButton.png')
        self.RomanIButtonImage = self.CreateImage('Images/Buttons/RomanIButton.png')


        # Shapes Labels
        self.tShapeImage = self.CreateImage('Images/Shapes/tShape.png')
        self.LShapeImage = self.CreateImage('Images/Shapes/LShape.png')
        self.uShapeImage = self.CreateImage('Images/Shapes/uShape.png')
        self.cShapeImage = self.CreateImage('Images/Shapes/cShape.png')
        self.iShapeImage = self.CreateImage('Images/Shapes/iShape.png')
        self.RomanIShapeImage = self.CreateImage('Images/Shapes/RomanIShape.png')

        #Menu Buttons
        self.CalculateImage = self.CreateImage('Images/Buttons/calculate.png')
        self.DiscardImage = self.CreateImage('Images/Buttons/discard.png')


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

        else:
            ZoomRatio = 100

        return ScreenResolution, ZoomRatio


    def EntryDiscard(self, entries):
        for e in entries:
            e.delete(0, tk.END)


    def SideFramePacking(self):
        # Botões Laterias
        self.tButton = widgets.SideButton(self.SideFrame, self.tButtonImage, self.tShape)
        self.LButton = widgets.SideButton(self.SideFrame, self.LButtonImage, self.LShape)
        self.uButton = widgets.SideButton(self.SideFrame, self.uButtonImage, self.uShape)
        self.cButton = widgets.SideButton(self.SideFrame, self.cButtonImage, self.cShape)
        self.iButton = widgets.SideButton(self.SideFrame, self.iButtonImage, self.iShape)
        self.RomanIButton = widgets.SideButton(self.SideFrame, self.RomanIButtonImage, self.hShape)

        # Layout
        self.tButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.LButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.uButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.cButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.iButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.RomanIButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


    def ClearMainSpace(self):
        for widget in self.MainSpace.winfo_children():
            widget.destroy()


    def OpenFibra(self, sec, meds):
        win_fibra = tk.Toplevel()
        FibraWindow(win_fibra, sec, meds)


    def tShape(self, event=None):
        def Calculate(event=None, entry=None):

            # Converte Os Valores Das Caixas De Entrada
            x = float(entry[0].get())
            b = float(entry[1].get())
            y = float(entry[2].get())
            z = float(entry[3].get())

            self.ClearMainSpace()
            
            area = tSection.get_area(x, b, y, z)
            perim = tSection.get_perim(x, b, y, z)
            cy = tSection.get_cy(x, b, y ,z)
            cx = tSection.get_cx(x)
            iz = tSection.get_iz(x, b, y, z , cy)
            scgz = tSection.get_scgz(x, b, y, z, cy)
            scgy = tSection.get_scgy(x, b, y, z)

            LeftFrame = tk.Frame(self.MainSpace, bg='#8c8c8c', bd=0) #dbdbdb
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0) #dbdbdb

            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#d1d1d1', bd=0)
            ButtonFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=5)
            # FibraFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=0, padx=20, pady=20)
            
            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            # ResultFrame.grid(row=0, column=0, padx=50, pady=50)
            ButtonFrame.pack(side=tk.TOP, fill=tk.X)
            ResultFrame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)
            # FibraFrame.grid(row=1, column=0, padx=50, pady=50)

            # Cria Os Widgets Para O ResultFrame 
            AreaLabel = widgets.ResultLabel(ResultFrame, 'Área =') 
            AreaValue = widgets.ResultValue(ResultFrame, f'{area:.2f} cm²')

            pLabel = widgets.ResultLabel(ResultFrame, 'Perímetro = ')
            pValue = widgets.ResultValue(ResultFrame, f'{perim:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            IzLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            IzContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            ScgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            ScgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            ScgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            ScgyContent = widgets.ResultValue(ResultFrame, f'{scgy:.2f} cm³')

            # Layout Dos Widgets Do Frame Resultado
            AreaLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            AreaValue.grid(row=0, column=1, padx=10, pady=5, sticky='w')

            pLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            pValue.grid(row=1, column=1, padx=10, pady=5, sticky='w')

            cyLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            cyContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')

            cxLabel.grid(row=3, column=0, padx=(25, 5), pady=5, sticky='e')
            cxContent.grid(row=3, column=1, padx=10, pady=5, sticky='w')

            IzLabel.grid(row=4, column=0, padx=(25, 5), pady=5, sticky='e')
            IzContent.grid(row=4, column=1, padx=10, pady=5, sticky='w')

            ScgzLabel.grid(row=5, column=0, padx=(25, 5), pady=5, sticky='e')
            ScgzContent.grid(row=5, column=1, padx=10, pady=5, sticky='w')

            ScgyLabel.grid(row=6, column=0, padx=(25, 5), pady=5, sticky='e')
            ScgyContent.grid(row=6, column=1, padx=10, pady=5, sticky='w')
            
            # FibraButton = widgets.OpenFibraButton(ButtonFrame, OpenFibra)
            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra('t', [x, b, y, z, cy]))
            FibraButton.pack(fill=tk.X)
            
            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 300)) # ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            xLabel = widgets.ValueLabel(ValueFrame, f'x = {x} cm')
            bLabel = widgets.ValueLabel(ValueFrame, f'b = {b} cm')
            yLabel = widgets.ValueLabel(ValueFrame, f'y = {y} cm')
            zLabel = widgets.ValueLabel(ValueFrame, f'z = {z} cm')

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

            if cy < y:
                DotHeight = CanvasHeight - 650
                
            elif cy > y:
                DotHeight = CanvasHeight - 720

            elif cy == y:
                DotHeight = CanvasHeight - 496
                
            DotImage = self.CreateImage('Images/Shapes/dot.png')
            ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(DotImage)

            x1 = 158; y1 = DotHeight; x2 = x1 + 9; y2 = CanvasHeight - 50

            # Cria A Linha Do Ycg
            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)
            ShapeCanvas.create_text(153, 844 - 50, text='Ycg', font=self.ResultFont, fill='#303030', anchor='se')


        def tLayout():
            self.ClearMainSpace()
            
            DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
            DataFrame.pack(expand=True)

            TopEntry = widgets.EntryField(DataFrame)
            RightEntry = widgets.EntryField(DataFrame)
            LeftEntry = widgets.EntryField(DataFrame)
            BottomEntry = widgets.EntryField(DataFrame)  
            tShapeLabel = widgets.ShapeImage(DataFrame, img=self.tShapeImage)

            entries = [TopEntry, LeftEntry, RightEntry  , BottomEntry]

            TopEntry.pack(side=tk.TOP, pady=(50, 25))
            RightEntry.pack(side=tk.RIGHT, anchor='w', padx=30)
            LeftEntry.pack(side=tk.LEFT, anchor='n', pady=75, padx=30)
            tShapeLabel.pack()
            BottomEntry.pack(side=tk.BOTTOM, pady=(25, 50))
            
            TopEntry.focus_set()

            MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
            MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

            ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
            ButtonsFrame.pack()

            CalculateButton = widgets.MenuButton(ButtonsFrame, img=self.CalculateImage, action=lambda: Calculate(entry=entries))
            DiscardButton = widgets.MenuButton(ButtonsFrame, img=self.DiscardImage, action= lambda:self.EntryDiscard(entries))

            CalculateButton.grid(row=0, column=0, padx=5)
            DiscardButton.grid(row=0, column=1, padx=5)
            
            self.root.bind('<Return>', lambda event, ent=entries: Calculate(entry=ent))


        tLayout()


    def LShape(self, event=None):
        def Calculate(event=None, entry=None):
            #Converte Os Valores Das Caixas De Entrada
            y = float(entry[0].get())
            x = float(entry[1].get())
            k = float(entry[2].get())
            u = float(entry[3].get())

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            area = lSection.get_area(y, k, x, u)
            perim = lSection.get_perim(y, k, x, u)
            cy = lSection.get_cy(y, k, x, u)
            cx = lSection.get_cx(y, k, x, u)
            iz = lSection.get_iz(y, k, x, u , cy) 
            iy = lSection.get_iy(y, k, x, u, cy)
            scgz = lSection.get_scgz(y, k, x, cy)
            scgy = lSection.get_scgy(x, u, cx)
            
             # Cria Os Frames Principais
            LeftFrame = tk.Frame(self.MainSpace, bg='#8c8c8c', bd=0) #dbdbdb
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0) #dbdbdb

            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#d1d1d1', bd=0)
            ButtonFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=5)
            
            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            ButtonFrame.pack(side=tk.TOP, fill=tk.X)
            ResultFrame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)

            # Cria Os Widgets Para O ResultFrame 
            areaLabel = widgets.ResultLabel(ResultFrame, 'Área =') 
            areaValue = widgets.ResultValue(ResultFrame, f'{area:.2f} cm²')

            pLabel = widgets.ResultLabel(ResultFrame, 'Perímetro = ')
            pValue = widgets.ResultValue(ResultFrame, f'{perim:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            iyLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            iyContent = widgets.ResultValue(ResultFrame, f'{iy:.2f} cm⁴')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultValue(ResultFrame, f'{scgy:.2f} cm³')

            # Layout Dos Widgets Do Frame Resultado
            areaLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            areaValue.grid(row=0, column=1, padx=10, pady=5, sticky='w')

            pLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            pValue.grid(row=1, column=1, padx=10, pady=5, sticky='w')

            cyLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            cyContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')

            cxLabel.grid(row=3, column=0, padx=(25, 5), pady=5, sticky='e')
            cxContent.grid(row=3, column=1, padx=10, pady=5, sticky='w')

            izLabel.grid(row=4, column=0, padx=(25, 5), pady=5, sticky='e')
            izContent.grid(row=4, column=1, padx=10, pady=5, sticky='w')

            iyLabel.grid(row=4, column=0, padx=(25, 5), pady=5, sticky='e')
            iyContent.grid(row=4, column=1, padx=10, pady=5, sticky='w')

            scgzLabel.grid(row=5, column=0, padx=(25, 5), pady=5, sticky='e')
            scgzContent.grid(row=5, column=1, padx=10, pady=5, sticky='w')

            scgyLabel.grid(row=6, column=0, padx=(25, 5), pady=5, sticky='e')
            scgyContent.grid(row=6, column=1, padx=10, pady=5, sticky='w')

            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra('l', [y, x, k, u, cy]))
            FibraButton.pack(fill=tk.X)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True)    

            RightValueFrame = tk.Frame(ValueFrame, bg='#dbdbdb')
            RightValueFrame.pack(side=tk.RIGHT, fill=tk.Y)

            # Cria Os Widgets Do ValueFrame
            yLabel = widgets.ValueLabel(ValueFrame, f'y = {y} cm')

            kLabel = widgets.ValueLabel(RightValueFrame, f'k = {k} cm')
            xLabel = widgets.ValueLabel(RightValueFrame, f'x = {x} cm')

            uLabel = widgets.ValueLabel(ValueFrame, f'u = {u} cm')


            # Layout Dos Widgets Do ValueFrame  
            yLabel.pack(side=tk.TOP, anchor='w', pady=(50, 25))
            kLabel.pack(side=tk.TOP, anchor='ne', pady=(400, 0))
            xLabel.pack(side=tk.BOTTOM, anchor='w', pady=(0, 140))
            uLabel.pack(side=tk.BOTTOM, pady=(25, 0))


            # Cria O Canvas Da Imagem Principal
            CanvasWidth = 486
            CanvasHeight = 700
            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()
            
            # Cria As Imagens No Canvas
            self.ImageList = []
            justTImage = self.CreateImage('Images/Shapes/LShape.png')
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=justTImage)
            self.ImageList.append(justTImage)    

            # self.ClearMainSpace()

       
        def lLayout():
            self.ClearMainSpace()

            DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
            DataFrame.pack(expand=True)

            RightEntries = tk.Frame(DataFrame, bg='#dbdbdb')
            RightEntries.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

            yEntry = widgets.EntryField(DataFrame)
            kEntry = widgets.EntryField(RightEntries)
            xEntry = widgets.EntryField(RightEntries)
            uEntry = widgets.EntryField(DataFrame)

            entries = [yEntry, xEntry, kEntry, uEntry]

            yEntry.pack(side=tk.TOP, anchor='w', pady=(50, 25))
            kEntry.pack(side=tk.TOP, pady=(400, 0))
            xEntry.pack(side=tk.BOTTOM, pady=(0, 180))
            uEntry.pack(side=tk.BOTTOM, pady=(25, 0))

            kEntry.focus_set()

            LShapeLabel = tk.Label(DataFrame, image=self.LShapeImage, bd=0)
            LShapeLabel.image = self.LShapeImage
            LShapeLabel.pack()

            MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
            MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

            ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
            ButtonsFrame.pack()

            CalculateButton = widgets.MenuButton(ButtonsFrame, img=self.CalculateImage, action=lambda: Calculate(entry=entries))
            DiscardButton = widgets.MenuButton(ButtonsFrame, img=self.DiscardImage, action= lambda:self.EntryDiscard(entries))

            CalculateButton.grid(row=0, column=0, padx=5)
            DiscardButton.grid(row=0, column=1, padx=5)

            self.root.bind('<Return>', lambda event, ent=entries: Calculate(entry=ent))


        lLayout()


    def uShape(self, event=None):
        def Calculate(event=None, entry=None):
            # Converte Os Valores Das Caixas De Entrada
            x = float(entry[0].get())  
            a = float(entry[1].get())
            y = float(entry[2].get())
            h = float(entry[3].get())

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            area = uSection.get_area(x, y, a ,h)
            perim = uSection.get_perim(x, y, a, h)
            cy = uSection.get_cy(x, y, a, h)
            cx = uSection.get_cx(a, h)
            iz = uSection.get_iz(x, y, a, h ,cy)
            scgz = uSection.get_scgz(x, y, a, h, cy)
            scgy = uSection.get_scgz(x, y, a, h, cx)

            # Cria Os Frames Principais
            LeftFrame = tk.Frame(self.MainSpace, bg='#8c8c8c', bd=0) #dbdbdb
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0) #dbdbdb

            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#d1d1d1', bd=0)
            ButtonFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=5)
            
            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            ButtonFrame.pack(side=tk.TOP, fill=tk.X)
            ResultFrame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)

            # Cria Os Widgets Para O ResultFrame 
            areaLabel = widgets.ResultLabel(ResultFrame, 'Área =') 
            areaValue = widgets.ResultValue(ResultFrame, f'{area:.2f} cm²')

            pLabel = widgets.ResultLabel(ResultFrame, 'Perímetro = ')
            pValue = widgets.ResultValue(ResultFrame, f'{perim:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultValue(ResultFrame, f'{scgy:.2f} cm³')

            # Layout Dos Widgets Do Frame Resultado
            areaLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            areaValue.grid(row=0, column=1, padx=10, pady=5, sticky='w')

            pLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            pValue.grid(row=1, column=1, padx=10, pady=5, sticky='w')

            cyLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            cyContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')

            cxLabel.grid(row=3, column=0, padx=(25, 5), pady=5, sticky='e')
            cxContent.grid(row=3, column=1, padx=10, pady=5, sticky='w')

            izLabel.grid(row=4, column=0, padx=(25, 5), pady=5, sticky='e')
            izContent.grid(row=4, column=1, padx=10, pady=5, sticky='w')

            scgzLabel.grid(row=5, column=0, padx=(25, 5), pady=5, sticky='e')
            scgzContent.grid(row=5, column=1, padx=10, pady=5, sticky='w')

            scgyLabel.grid(row=6, column=0, padx=(25, 5), pady=5, sticky='e')
            scgyContent.grid(row=6, column=1, padx=10, pady=5, sticky='w')

            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra('u', [x, y, a, h, cy]))
            FibraButton.pack(fill=tk.X)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            TopLabelFrame = tk.Frame(ValueFrame, bg='#dbdbdb')
            a1Label = widgets.ValueLabel(TopLabelFrame, f'a = {a} cm')
            a2Label = widgets.ValueLabel(TopLabelFrame, f'a = {a} cm')
            YcgL = widgets.ValueLabel(ValueFrame, 'Ycg')
            hLabel = widgets.ValueLabel(ValueFrame, f'h = {h} cm')

            RightLabelFrame = tk.Frame(ValueFrame, bg='#dbdbdb')

            gLabel = tk.Label(RightLabelFrame, text=f'g = {y - x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')
            xLabel = tk.Label(RightLabelFrame, text=f'x = {x} cm', font=self.ResultFont, bg='#dbdbdb', fg='#303030')

            # Layout Dos Widgets Do ValueFrame  
            TopLabelFrame.pack(side=tk.TOP)
            a1Label.pack(side=tk.LEFT, padx=(0, 170))
            a2Label.pack(side=tk.RIGHT, padx=(170, 0))
            YcgL.pack(side=tk.LEFT, anchor='se', padx=(70, 0), pady=70)
            RightLabelFrame.pack(side=tk.RIGHT, anchor='w', fill=tk.Y)
            gLabel.pack(anchor='w', pady=(350, 0))
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

            if cy < x:
                DotHeight = CanvasHeight - 145
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            elif cy > x:
                DotHeight = CanvasHeight - 350
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            elif cy == x:
                DotHeight = CanvasHeight - 190
                ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)

            self.ImageList.append(DotImage)

            # Cria A Linha Do Ycg
            x1 = 15; y1 = DotHeight; x2 = x1 + 9; y2 = 799
            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)


        def uLayout():
            self.ClearMainSpace()

            DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
            DataFrame.pack(expand=True)

            TopEntryFrame = tk.Frame(DataFrame, bg='#dbdbdb')
            TopEntryFrame.pack(side=tk.TOP, pady=(50, 25))

            a1Entry = widgets.EntryField(TopEntryFrame)
            a2Entry = widgets.EntryField(TopEntryFrame)
            xEntry = widgets.EntryField(DataFrame)
            yEntry = widgets.EntryField(DataFrame)
            hEntry = widgets.EntryField(DataFrame)
            uShapeLabel = widgets.ShapeImage(DataFrame, img=self.uShapeImage)

            entries = [xEntry, a1Entry, yEntry, hEntry, a2Entry]

            a1Entry.pack(side=tk.LEFT, padx=30)
            a2Entry.pack(side=tk.RIGHT, padx=30)        
            xEntry.pack(side=tk.LEFT, anchor='s', pady=(0, 140), padx=30)
            yEntry.pack(side=tk.RIGHT, anchor='w', padx=30)
            uShapeLabel.pack()
            hEntry.pack(pady=(30, 0))

            a1Entry.focus_set()

            MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
            MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

            ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
            ButtonsFrame.pack()

            CalculateButton = widgets.MenuButton(ButtonsFrame, img=self.CalculateImage, action= lambda: Calculate(entry=entries))
            DiscardButton = widgets.MenuButton(ButtonsFrame, img=self.DiscardImage, action= lambda: self.EntryDiscard(entries))

            CalculateButton.grid(row=0, column=0, padx=5)
            DiscardButton.grid(row=0, column=1, padx=5)
            
            self.root.bind('<Return>', lambda event, ent=entries: Calculate(entry=ent))


        uLayout()


    def cShape(self, event=None):
        self.ClearMainSpace()

        DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
        DataFrame.pack(expand=True)

        cShapeLabel = tk.Label(DataFrame, image=self.cShapeImage, bd=0)
        cShapeLabel.image = self.cShapeImage
        cShapeLabel.pack()

        WarningLabel = tk.Label(DataFrame, text='EM BREVE', font=self.WarningFont, fg='#8c8c8c', bg='#dbdbdb')
        WarningLabel.pack()


    def iShape(self, event=None):
        def Calculate(event=None, entry=None):
            # Converte Os Valores Das Caixas De Entrada
            w = float(entry[0].get())
            h = float(entry[1].get())

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            area = iSection.get_area(w, h)
            perim = iSection.get_perim(w, h)
            cy = iSection.get_cy(h)
            cx = iSection.get_cx(w)
            iz = iSection.get_iz(h, w)
            scgz = iSection.get_scgz(w, cy)
            scgy = iSection.get_scgy(h, w, cx)

            # Cria Os Frames Principais
            LeftFrame = tk.Frame(self.MainSpace, bg='#8c8c8c', bd=0) #dbdbdb
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0) #dbdbdb

            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#d1d1d1', bd=0)
            ButtonFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=5)
            
            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            ButtonFrame.pack(side=tk.TOP, fill=tk.X)
            ResultFrame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)

            # Cria Os Widgets Para O ResultFrame 
            areaLabel = widgets.ResultLabel(ResultFrame, 'Área =') 
            areaValue = widgets.ResultValue(ResultFrame, f'{area:.2f} cm²')

            pLabel = widgets.ResultLabel(ResultFrame, 'Perímetro = ')
            pValue = widgets.ResultValue(ResultFrame, f'{perim:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultValue(ResultFrame, f'{scgy:.2f} cm³')

            # Layout Dos Widgets Do Frame Resultado
            areaLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            areaValue.grid(row=0, column=1, padx=10, pady=5, sticky='w')

            pLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            pValue.grid(row=1, column=1, padx=10, pady=5, sticky='w')

            cyLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            cyContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')

            cxLabel.grid(row=3, column=0, padx=(25, 5), pady=5, sticky='e')
            cxContent.grid(row=3, column=1, padx=10, pady=5, sticky='w')

            izLabel.grid(row=4, column=0, padx=(25, 5), pady=5, sticky='e')
            izContent.grid(row=4, column=1, padx=10, pady=5, sticky='w')

            scgzLabel.grid(row=5, column=0, padx=(25, 5), pady=5, sticky='e')
            scgzContent.grid(row=5, column=1, padx=10, pady=5, sticky='w')

            scgyLabel.grid(row=6, column=0, padx=(25, 5), pady=5, sticky='e')
            scgyContent.grid(row=6, column=1, padx=10, pady=5, sticky='w')
            
            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra('i', [w, h, cy]))
            FibraButton.pack(fill=tk.X)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            wLabel = widgets.ValueLabel(ValueFrame, f'x = {w} cm')
            hLabel = widgets.ValueLabel(ValueFrame, f'y = {h} cm')
            YcgL = widgets.ValueLabel(ValueFrame, 'Ycg')

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


        def iLayout():
            self.ClearMainSpace()

            # Cria Os Widgets Do self.MainSpace
            DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
            MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)

            # Layout Dos Widgets Do self.MainSpace
            DataFrame.pack(expand=True)
            MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

            # Cria Os Widgets Do DataFrame
            WidthEntry = widgets.EntryField(DataFrame)
            HeightEntry = widgets.EntryField(DataFrame)
            iShapeLabel = widgets.ShapeImage(DataFrame, img=self.iShapeImage)

            entries = [WidthEntry, HeightEntry]

            # Layout Dos Widgets Do DataFrame
            WidthEntry.pack(side=tk.TOP, pady=(50, 25))
            HeightEntry.pack(side=tk.RIGHT, anchor='n', pady=300, padx=30)
            iShapeLabel.pack(padx=(360, 0))

            WidthEntry.focus_set()

            ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
            ButtonsFrame.pack()

            # Widgets De ButtonsFrame
            CalculateButton = widgets.MenuButton(ButtonsFrame, img=self.CalculateImage, action= lambda: Calculate(entry=entries))
            DiscardButton = widgets.MenuButton(ButtonsFrame, img=self.DiscardImage, action=lambda: self.EntryDiscard(entries))

            # Layout Dos Widgets
            CalculateButton.grid(row=0, column=0, padx=5)
            DiscardButton.grid(row=0, column=1, padx=5)

            self.root.bind('<Return>', lambda event, ent=entries: Calculate(entry=ent))

        iLayout()


    def hShape(self, event=None):
        def Calculate(event=None, entry=None):
            # Converte Os Valores Das Caixas De Entrada
            x = float(entry[0].get())
            y = float(entry[1].get())
            a = float(entry[2].get())
            d = float(entry[3].get())
            h = float(entry[4].get())
            r = float(entry[5].get())

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            area = hSection.get_area(x, y, a, d, h, r)
            perim = hSection.get_area(x, y, a, d, h, r)
            cy = hSection.get_cy(x, y, a, d, h, r)
            cx = hSection.get_cx(x, r)
            iz = hSection.get_iz(x, y, a, d, h, r, cy)
            iy = hSection.get_iy(x, y, a, d, h, r)
            scgz = hSection.get_scgz(x, y, a, d, h, r, cy)
            scgy = hSection.get_scgy(x, y, a, d, h, r)

            # Cria Os Frames Principais
            LeftFrame = tk.Frame(self.MainSpace, bg='#8c8c8c', bd=0) #dbdbdb
            RightFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0) #dbdbdb

            # Layout Dos Frames Principais 
            LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH)
            RightFrame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

            # Cria Frames Para O Frame Esquerdo 
            ResultFrame = tk.Frame(LeftFrame, bg='#d1d1d1', bd=0)
            ButtonFrame = tk.Frame(LeftFrame, bg='#b0b0b0', bd=5)
            
            # Cria Frames Para O Frame Direito
            ValueFrame = tk.Frame(RightFrame, bg='#dbdbdb')

            # Layout Dos Frames Da Esquerda
            ButtonFrame.pack(side=tk.TOP, fill=tk.X)
            ResultFrame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)

            # Cria Os Widgets Para O ResultFrame 
            areaLabel = widgets.ResultLabel(ResultFrame, 'Área =') 
            areaValue = widgets.ResultValue(ResultFrame, f'{area:.2f} cm²')

            pLabel = widgets.ResultLabel(ResultFrame, 'Perímetro = ')
            pValue = widgets.ResultValue(ResultFrame, f'{perim:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            iyLabel = widgets.ResultLabel(ResultFrame, 'iy =')
            iyContent = widgets.ResultLabel(ResultFrame, f'{iy:.2f} cm')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultLabel(ResultFrame, f'{scgy:.2f} cm')

            # Layout Dos Widgets Do Frame Resultado
            areaLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            areaValue.grid(row=0, column=1, padx=10, pady=5, sticky='w')

            pLabel.grid(row=1, column=0, padx=(25, 5), pady=5, sticky='e')
            pValue.grid(row=1, column=1, padx=10, pady=5, sticky='w')

            cyLabel.grid(row=2, column=0, padx=(25, 5), pady=5, sticky='e')
            cyContent.grid(row=2, column=1, padx=10, pady=5, sticky='w')
            
            cxLabel.grid(row=3, column=0, padx=(25, 5), pady=5, sticky='e')
            cxContent.grid(row=3, column=1, padx=10, pady=5, sticky='w')

            izLabel.grid(row=4, column=0, padx=(25, 5), pady=5, sticky='e')
            izContent.grid(row=4, column=1, padx=10, pady=5, sticky='w')

            iyLabel.grid(row=5, column=0, padx=(25, 5), pady=5, sticky='e')
            iyContent.grid(row=5, column=1, padx=10, pady=5, sticky='w')
            
            scgzLabel.grid(row=6, column=0, padx=(25, 5), pady=5, sticky='e')
            scgzContent.grid(row=6, column=1, padx=10, pady=5, sticky='w')

            scgyLabel.grid(row=7, column=0, padx=(25, 5), pady=5, sticky='e')
            scgyContent.grid(row=7, column=1, padx=10, pady=5, sticky='w')
            
            # Cria Os Widgets Para O FibraFrame
            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra('h', [x, y, a, d, h, r, cy]))
            FibraButton.pack(fill=tk.X)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            xLabel = widgets.ValueLabel(ValueFrame, f'x = {x} cm')
            aLabel = widgets.ValueLabel(ValueFrame, f'a = {a} cm')
            rLabel = widgets.ValueLabel(ValueFrame, f'r = {r} cm')

            RightValueFrame = tk.Frame(ValueFrame, bg='#dbdbdb')
            
            yLabel = widgets.ValueLabel(RightValueFrame, f'y = {y} cm')
            hLabel = widgets.ValueLabel(RightValueFrame, f'h = {h} cm')
            dLabel = widgets.ValueLabel(RightValueFrame, f'd = {d} cm')

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

            if cy > (h + d):
                DotHeight = CanvasHeight - 708
                
            elif cy == (h + d):
                DotHeight = CanvasHeight - 632
            
            elif ((y + h + d) / 2) < cy < (h + d):
                DotHeight = CanvasHeight - 522

            elif cy == ((y + h + d) / 2):
                DotHeight = CanvasHeight - 411

            elif cy == ((h + d) / 2):
                DotHeight = CanvasHeight - 336

            elif d < cy < ((y + d + h) / 2):
                DotHeight = CanvasHeight - 299
            
            elif cy == d:
                DotHeight = CanvasHeight - 189

            elif cy < d:
                DotHeight = CanvasHeight - 94

            DotImage = self.CreateImage('Images/Shapes/dot.png')
            ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(DotImage)

            x1 = 283; y1 = DotHeight; x2 = x1 + 9; y2 = CanvasHeight - 37

            # Cria A Linha Do Ycg
            ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)
            ShapeCanvas.create_text(x2 + 10, y2, text='Ycg', font=self.ResultFont, fill='#303030', anchor='sw')


        def hLayout():
            self.ClearMainSpace()

            DataFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
            DataFrame.pack(expand=True)

            xEntry = widgets.EntryField(DataFrame)
            LeftFrame = tk.Frame(DataFrame, bg='#dbdbdb')
            yEntry = widgets.EntryField(LeftFrame)
            aEntry = widgets.EntryField(LeftFrame)
            dEntry = widgets.EntryField(LeftFrame)
            hEntry = widgets.EntryField(DataFrame)
            rEntry = widgets.EntryField(DataFrame)
            RomanIShapeLabel = widgets.ShapeImage(DataFrame, img=self.RomanIShapeImage)

            entries = [xEntry, yEntry, aEntry, dEntry, hEntry, rEntry]

            xEntry.pack(side=tk.TOP, pady=(50, 25))
            LeftFrame.pack(side=tk.LEFT, anchor='s', pady=50, padx=30)
            yEntry.pack(side=tk.TOP, pady=(0, 245)) 
            aEntry.pack(pady=(0, 160)) 
            dEntry.pack(side=tk.BOTTOM, pady=(0, 100))
            hEntry.pack(side=tk.RIGHT, anchor='n', pady=325, padx=30)
            RomanIShapeLabel.pack()  
            rEntry.pack(pady=(20, 0))

            xEntry.focus_set()

            MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)
            MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

            ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
            ButtonsFrame.pack()

            CalculateButton = widgets.MenuButton(ButtonsFrame, img=self.CalculateImage, action= lambda: Calculate(entry=entries))
            DiscardButton = widgets.MenuButton(ButtonsFrame, img=self.DiscardImage, action=lambda: self.EntryDiscard(entries))

            CalculateButton.grid(row=0, column=0, padx=5)
            DiscardButton.grid(row=0, column=1, padx=5)

            self.root.bind('<Return>', lambda event, ent=entries: Calculate(entry=ent))


        hLayout()


def main():
    root = tk.Tk()
    MainProgram(root)
    root.mainloop()


if __name__ == '__main__':
    main()
