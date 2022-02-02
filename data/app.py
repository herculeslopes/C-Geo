import tkinter as tk
from tkinter.font import Font
from . import utilities
from .windows import win_info, win_fibra
from . import widgets
from .sections import *
import os

class App:
    """ Classe principal do programa

    """
    TITLE = 'C-Geo'
    LOGO_PATH = os.path.join('rsc', 'img', 'c-geo.ico')

    def __init__(self, master):
        """
        Parâmetros
        ----------
        master: tkinter.Tk
            Janela principal do programa
        """

        self.root = master

        self.root.title(App.TITLE)
        self.root.iconbitmap(App.LOGO_PATH)
        self.root.state('zoomed')

        self.SideFrame = tk.Frame(self.root, bg='#c9c9c9', width=90, bd=0)
        self.SideFrame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.MainSpace = tk.Frame(self.root, bg='#dbdbdb', bd=0)
        self.MainSpace.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.EntryFont = Font(family='Calibri', size=20)
        self.ResultFont = Font(family='Calibri', size=16)
        self.WarningFont = Font(size=50)

        self.screen_info = utilities.get_screen_info()
        self.screen_resolution = self.screen_info[0]
        self.windows_zoom = self.screen_info[1]

        # self.OptionSelected = tk.StringVar()

        print(f'\nScreen Info: {self.screen_info}')
        print(f'Zoom Ratio: {self.windows_zoom}')
        print(f'Screen Resolution {self.screen_resolution}\n')

        self.root.bind('<Control-Key-1>', self.tShape)
        self.root.bind('<Control-Key-2>', self.LShape)
        self.root.bind('<Control-Key-3>', self.uShape)
        self.root.bind('<Control-Key-4>', self.cShape)
        self.root.bind('<Control-Key-5>', self.iShape)
        self.root.bind('<Control-Key-6>', self.hShape)

        self.InitImages()
        self.SideFramePacking()
        self.HomePage()


    def OpenFibra(self, section, values):
        win_fibra.FibraWindow(self, tk.Toplevel(), section, values)


    def show_info(self):
        win_info.InfoWindow(self, tk.Toplevel())


    @staticmethod
    def EntryDiscard(entries):
        for e in entries:
            e.delete(0, tk.END)


    def InitImages(self):
        """Inicializa as variáveis de imagem utilizadas ao longo do programa.
        
        O caminho relativo das imagens é passada para a função self.CreateImage.
        """

        # Side Button
        self.homeButtonImage = utilities.create_image(self, ['btn', 'home.png'])
        self.tButtonImage = utilities.create_image(self, ['btn', 'btn-t.png'])
        self.LButtonImage = utilities.create_image(self, ['btn', 'btn-l.png'])
        self.uButtonImage = utilities.create_image(self, ['btn', 'btn-u.png'])
        self.cButtonImage = utilities.create_image(self, ['btn', 'btn-c.png'])
        self.iButtonImage = utilities.create_image(self, ['btn', 'btn-i.png'])
        self.hButtonImage = utilities.create_image(self, ['btn', 'btn-h.png'])
        self.infoButtonImage = utilities.create_image(self, ['btn', 'info-btn.png'])

        # Home Image
        self.homeImage = utilities.create_image(self, ['general', 'img-home.png'])

        # Shapes Labels
        self.tShapeImage = utilities.create_image(self, ['Shapes', 'section-t.png'])
        self.LShapeImage = utilities.create_image(self, ['Shapes', 'section-l.png'])
        self.uShapeImage = utilities.create_image(self, ['Shapes', 'section-u.png'])
        self.cShapeImage = utilities.create_image(self, ['Shapes', 'section-c.png'])
        self.iShapeImage = utilities.create_image(self, ['Shapes', 'section-i.png'])
        self.RomanIShapeImage = utilities.create_image(self, ['Shapes', 'section-h.png'])

        #Menu Buttons
        self.CalculateImage = utilities.create_image(self, ['btn', 'calculate.png'])
        self.DiscardImage = utilities.create_image(self, ['btn', 'discard.png'])


    def SideFramePacking(self):
        # Botões Laterias
        self.btnHome = widgets.SideButton(self.SideFrame, self.homeButtonImage, self.HomePage)

        devider = widgets.DividingLine(self.SideFrame)

        self.tButton = widgets.SideButton(self.SideFrame, self.tButtonImage, self.tShape)
        self.LButton = widgets.SideButton(self.SideFrame, self.LButtonImage, self.LShape)
        self.uButton = widgets.SideButton(self.SideFrame, self.uButtonImage, self.uShape)
        self.cButton = widgets.SideButton(self.SideFrame, self.cButtonImage, self.cShape)
        self.iButton = widgets.SideButton(self.SideFrame, self.iButtonImage, self.iShape)
        self.hButton = widgets.SideButton(self.SideFrame, self.hButtonImage, self.hShape)
        self.infoButton = widgets.SideButton(self.SideFrame, self.infoButtonImage, self.show_info)

        # Layout
        self.btnHome.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        devider.pack(fill=tk.X, padx=10)
        self.tButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.LButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.uButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.cButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.iButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.hButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.infoButton.pack(side=tk.BOTTOM, pady=(0, 10))


    def ClearMainSpace(self):
        for widget in self.MainSpace.winfo_children():
            widget.destroy()


    def HomePage(self):
        self.ClearMainSpace()

        homeLabel = tk.Label(self.MainSpace, bg='#dbdbdb', image=self.homeImage)
        homeLabel.image = self.homeImage
        homeLabel.pack()


    def tShape(self, event=None):
        def Calculate(event=None, entry=None):
            # Converte Os Valores Das Caixas De Entrada
            try:
                x = float(entry[0].get())
                b = float(entry[1].get())
                y = float(entry[2].get())
                z = float(entry[3].get())
            except ValueError:
                return

            medidas = [x, b, y, z]
            if 0 in medidas:
                return
            elif not x > z:
                return
            else:
                del medidas

            self.ClearMainSpace()
            
            t_section = TSection(x, b, y, z)

            area = t_section.area
            perimeter = t_section.perimeter
            cy = t_section.cy
            cx = t_section.cx
            iz = t_section.iz
            iy = t_section.iy
            scgz = t_section.scgz
            scgy = t_section.scgy
            kz = t_section.kz
            ky = t_section.ky
            '''
                area = tSection.get_area(x, b, y, z)
                perim = tSection.get_perim(x, b, y, z)
                cy = tSection.get_cy(x, b, y ,z)
                cx = tSection.get_cx(x)
                iz = tSection.get_iz(x, b, y, z , cy)
                iy = tSection.get_iy(x, b, y, z)
                scgz = tSection.get_scgz(x, b, y, z, cy)
                scgy = tSection.get_scgy(x, b, y, z)
                kz = tSection.get_kz(area, iz)
                ky = tSection.get_ky(area, iy)'''

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
            pValue = widgets.ResultValue(ResultFrame, f'{perimeter:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            iyLabel = widgets.ResultLabel(ResultFrame, 'Iy =')
            iyContent = widgets.ResultValue(ResultFrame, f'{iy:.2f} cm⁴')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultValue(ResultFrame, f'{scgy:.2f} cm³')

            kzLabel = widgets.ResultLabel(ResultFrame, 'Kz =')
            kzContent = widgets.ResultValue(ResultFrame, f'{kz:.2f} cm')

            kyLabel = widgets.ResultLabel(ResultFrame, 'Ky =')
            kyContent = widgets.ResultValue(ResultFrame, f'{ky:.2f} cm')


            # Layout Dos Widgets Do Frame Resultado
            AreaLabel.grid(row=0, column=0, padx=(25, 5), pady=5, sticky='e')
            AreaValue.grid(row=0, column=1, padx=10, pady=5, sticky='w')

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

            kzLabel.grid(row=8, column=0, padx=(25, 5), pady=5, sticky='e')
            kzContent.grid(row=8, column=1, padx=10, pady=5, sticky='w')

            kyLabel.grid(row=9, column=0, padx=(25, 5), pady=5, sticky='e')
            kyContent.grid(row=9, column=1, padx=10, pady=5, sticky='w')
            
            # FibraButton = widgets.OpenFibraButton(ButtonFrame, OpenFibra)
            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra(t_section, [x, b, y, z, cy]))
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
            CANVAS_WIDTH = 694
            CANVAS_HEIGHT = 844
            
            ShapeCanvas = tk.Canvas(ValueFrame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()
            
            # Cria As Imagens No Canvas
            self.ImageList = []
            justTImage = utilities.create_image(self, ['Shapes', 'tValues.png'])
            ShapeCanvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, anchor=tk.CENTER, image=justTImage)
            self.ImageList.append(justTImage)

            if cy < y:
                DotHeight = CANVAS_HEIGHT - 650
                
            elif cy > y:
                DotHeight = CANVAS_HEIGHT - 720

            elif cy == y:
                DotHeight = CANVAS_HEIGHT - 496
                
            DotImage = utilities.create_image(self, ['Shapes', 'dot.png'])
            ShapeCanvas.create_image(CANVAS_WIDTH/2, DotHeight, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(DotImage)

            x1 = 158; y1 = DotHeight; x2 = x1 + 9; y2 = CANVAS_HEIGHT - 50

            # Cria A Linha Do Ycg
            # ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)
            # ShapeCanvas.create_text(153, 844 - 50, text='Ycg', font=self.ResultFont, fill='#303030', anchor='se')


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
            try:
                y = float(entry[0].get())
                x = float(entry[1].get())
                k = float(entry[2].get())
                u = float(entry[3].get())
            except ValueError:
                return

            medidas = [y, x, k, u]
            if 0 in medidas:
                return
            else:
                del medidas

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            l_section = LSection(y, k, x, u)

            area = l_section.area
            perimeter = l_section.perimeter
            cy = l_section.cy
            cx = l_section.cx
            iz = l_section.iz
            iy = l_section.iy
            scgz = l_section.scgz
            scgy = l_section.scgy
            kz = l_section.kz
            ky = l_section.ky
            
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
            pValue = widgets.ResultValue(ResultFrame, f'{perimeter:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            iyLabel = widgets.ResultLabel(ResultFrame, 'Iy =')
            iyContent = widgets.ResultValue(ResultFrame, f'{iy:.2f} cm⁴')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultValue(ResultFrame, f'{scgy:.2f} cm³')

            kzLabel = widgets.ResultLabel(ResultFrame, 'Kz =')
            kzContent = widgets.ResultValue(ResultFrame, f'{kz:.2f} cm⁴')

            kyLabel = widgets.ResultLabel(ResultFrame, 'Ky =')
            kyContent = widgets.ResultValue(ResultFrame, f'{ky:.2f} cm⁴')

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

            kzLabel.grid(row=8, column=0, padx=(25, 5), pady=5, sticky='e')
            kzContent.grid(row=8, column=1, padx=10, pady=5, sticky='w')

            kyLabel.grid(row=9, column=0, padx=(25, 5), pady=5, sticky='e')
            kyContent.grid(row=9, column=1, padx=10, pady=5, sticky='w')

            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra(l_section, [y, x, k, u, cy]))
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
            justLImage = utilities.create_image(self, ['Shapes', 'section-l.png'])
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=justLImage)
            self.ImageList.append(justLImage)    

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
            xEntry.pack(side=tk.BOTTOM, pady=(0, 140))
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
            try:
                x = float(entry[0].get())  
                a = float(entry[1].get())
                y = float(entry[2].get())
                h = float(entry[3].get())
            except ValueError:
                return

            medidas = [x, a, y, h]
            if 0 in medidas: 
                return 
            else: 
                del medidas

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            u_section = USection(x, y, a, h)

            area = u_section.area
            perimeter = u_section.perimeter
            cy = u_section.cy
            cx = u_section.cx
            j = u_section.j
            iz = u_section.iz
            iy = u_section.iy
            scgz = u_section.scgz
            scgy = u_section.scgy
            kz = u_section.kz
            ky = u_section.ky

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
            pValue = widgets.ResultValue(ResultFrame, f'{perimeter:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            iyLabel = widgets.ResultLabel(ResultFrame, 'Iy =')
            iyContent = widgets.ResultValue(ResultFrame, f'{iy:.2f} cm⁴')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultValue(ResultFrame, f'{scgy:.2f} cm³')

            kzLabel = widgets.ResultLabel(ResultFrame, 'Kz =')
            kzContent = widgets.ResultValue(ResultFrame, f'{kz:.2f} cm')

            kyLabel = widgets.ResultLabel(ResultFrame, 'Ky =')
            kyContent = widgets.ResultValue(ResultFrame, f'{ky:.2f} cm')

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

            kzLabel.grid(row=8, column=0, padx=(25, 5), pady=5, sticky='e')
            kzContent.grid(row=8, column=1, padx=10, pady=5, sticky='w')

            kyLabel.grid(row=9, column=0, padx=(25, 5), pady=5, sticky='e')
            kyContent.grid(row=9, column=1, padx=10, pady=5, sticky='w')

            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra(u_section, [x, y, a, h, cy]))
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
            uValuesImage = utilities.create_image(self, ['Shapes', 'uValues.png'])
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=uValuesImage)
            self.ImageList.append(uValuesImage)
            DotImage = utilities.create_image(self, 'img/Shapes/dot.png')

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
            #ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)


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
        def Calculate(event=None, entry=None):
            # Converte Os Valores Das Caixas De Entrada

            try:
                b = float(entry[0].get())
                h = float(entry[1].get())
                a = float(entry[2].get())
                m = float(entry[3].get())

                print(f'b: {b}')
                print(f'h: {h}')
                print(f'a: {a}')
                print(f'm: {m}')

            except ValueError:
                return

            if b == 0 or h == 0 or a == 0 or m == 0:
                return

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            c_section = CSection(b, h, a, m)

            area = c_section.area
            perimeter = c_section.perimeter
            cy = c_section.cy
            cx = c_section.cx
            iz = c_section.iz
            iy = c_section.iy
            scgz = c_section.scgz
            # scgy = c_section.scgy()
            kz = c_section.kz
            ky = c_section.ky

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
            pValue = widgets.ResultValue(ResultFrame, f'{perimeter:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            iyLabel = widgets.ResultLabel(ResultFrame, 'Iy =')
            iyContent = widgets.ResultValue(ResultFrame, f'{iy:.2f} cm⁴')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultValue(ResultFrame, f'scgy cm³')

            kzLabel = widgets.ResultLabel(ResultFrame, 'Kz =')
            kzContent = widgets.ResultValue(ResultFrame, f'{kz:.2f} cm')

            kyLabel = widgets.ResultLabel(ResultFrame, 'Ky =')
            kyContent = widgets.ResultValue(ResultFrame, f'{ky:.2f} cm')

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

            kzLabel.grid(row=8, column=0, padx=(25, 5), pady=5, sticky='e')
            kzContent.grid(row=8, column=1, padx=10, pady=5, sticky='w')

            kyLabel.grid(row=9, column=0, padx=(25, 5), pady=5, sticky='e')
            kyContent.grid(row=9, column=1, padx=10, pady=5, sticky='w')
            
            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra(c_section, [b, h, a, m, cy]))
            FibraButton.pack(fill=tk.X)

            # Layout Dos Frames Da Direita
            ValueFrame.pack(expand=True, padx=(0, 400))

            # Cria Os Widgets Do ValueFrame
            # wLabel = widgets.ValueLabel(ValueFrame, f'x = {w} cm')
            hLabel = widgets.ValueLabel(ValueFrame, f'y = {h} cm')
            YcgL = widgets.ValueLabel(ValueFrame, 'Ycg')

            # Layout Dos Widgets Do ValueFrame
            # wLabel.pack(side=tk.TOP)
            hLabel.pack(side=tk.RIGHT)
            YcgL.pack(side=tk.LEFT, anchor='se', padx=(70, 0), pady=20)

            # Cria O Canvas Da Imagem Principal
            CanvasWidth = 265
            CanvasHeight = 819
            ShapeCanvas = tk.Canvas(ValueFrame, width=CanvasWidth, height=CanvasHeight, bg='#dbdbdb', bd=0, highlightthickness=0)
            ShapeCanvas.pack()            

            # Cria As Imagens No Canvas
            self.ImageList = []
            iValuesImage = utilities.create_image(self, ['Shapes', 'section-c.png'])
            DotImage = utilities.create_image(self, ['Shapes', 'dot.png'])
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=iValuesImage)
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(iValuesImage)
            self.ImageList.append(DotImage)

            # Cria A Linha Do Ycg
            x1 = 18; y1 = CanvasHeight / 2; x2 = x1 + 9; y2 = 796
            # ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)


        def cLayout():
            self.ClearMainSpace()

            # Cria Os Widgets Do self.MainSpace
            EntriesFrame = tk.Frame(self.MainSpace, bg='#dbdbdb')
            rEntries = tk.Frame(EntriesFrame, bg='#dbdbdb', bd=0)
            bEntries = tk.Frame(EntriesFrame, bg='#dbdbdb', bd=0)
            MenuFrame = tk.Frame(self.MainSpace, bg='#dbdbdb', bd=0, height=100)

            # Layout Dos Widgets Do self.MainSpace
            EntriesFrame.pack(expand=True)
            rEntries.pack(side=tk.RIGHT, fill=tk.Y)
            bEntries.pack(side=tk.BOTTOM, fill=tk.X)
            MenuFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=25)

            # Cria Os Widgets Do DataFrame
            b1Entry = widgets.EntryField(rEntries)
            hEntry = widgets.EntryField(rEntries)
            b2Entry = widgets.EntryField(rEntries)
            aEntry = widgets.EntryField(bEntries)
            mEntry = widgets.EntryField(bEntries)
            cShapeLabel = widgets.ShapeImage(EntriesFrame, img=self.cShapeImage)

            entries = [b1Entry, hEntry, aEntry, mEntry]

            # Layout Dos Widgets Do DataFrame
            b1Entry.pack(side=tk.TOP, pady=(50, 0))
            hEntry.pack(pady=200)
            b2Entry.pack(side=tk.BOTTOM, pady=(0, 160))
            # WidthEntry.pack(side=tk.TOP, pady=(50, 25))
            # HeightEntry.pack(side=tk.RIGHT, anchor='n', pady=300, padx=30)
            cShapeLabel.pack()
            aEntry.pack(side=tk.LEFT)
            mEntry.pack(side=tk.RIGHT)

            b1Entry.focus_set()

            ButtonsFrame = tk.Frame(MenuFrame, bg='#dbdbdb', bd=0)
            ButtonsFrame.pack()

            # Widgets De ButtonsFrame
            CalculateButton = widgets.MenuButton(ButtonsFrame, img=self.CalculateImage, action= lambda: Calculate(entry=entries))
            DiscardButton = widgets.MenuButton(ButtonsFrame, img=self.DiscardImage, action=lambda: self.EntryDiscard(entries))

            # Layout Dos Widgets
            CalculateButton.grid(row=0, column=0, padx=5)
            DiscardButton.grid(row=0, column=1, padx=5)

            self.root.bind('<Return>', lambda event, ent=entries: Calculate(entry=ent))

        cLayout()


    def iShape(self, event=None):
        def Calculate(event=None, entry=None):
            # Converte Os Valores Das Caixas De Entrada
            try:
                w = float(entry[0].get())
                h = float(entry[1].get())
            except ValueError:
                return

            medidas = [w, h]
            if 0 in medidas:
                return
            else:
                del medidas

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            i_section = ISection(w, h)

            area = i_section.area
            perimeter = i_section.perimeter
            cy = i_section.cy
            cx = i_section.cx
            iz = i_section.iz
            iy = i_section.iy
            scgz = i_section.scgz
            scgy = i_section.scgy
            kz = i_section.kz
            ky = i_section.ky

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
            pValue = widgets.ResultValue(ResultFrame, f'{perimeter:.2f} cm')

            cyLabel = widgets.ResultLabel(ResultFrame, 'cy =')
            cyContent = widgets.ResultLabel(ResultFrame, f'{cy:.2f} cm')

            cxLabel = widgets.ResultLabel(ResultFrame, 'cx =')
            cxContent = widgets.ResultLabel(ResultFrame, f'{cx:.2f} cm')

            izLabel = widgets.ResultLabel(ResultFrame, 'Iz =')
            izContent = widgets.ResultValue(ResultFrame, f'{iz:.2f} cm⁴')

            iyLabel = widgets.ResultLabel(ResultFrame, 'Iy =')
            iyContent = widgets.ResultValue(ResultFrame, f'{iy:.2f} cm⁴')

            scgzLabel = widgets.ResultLabel(ResultFrame, 'Scgz =')
            scgzContent = widgets.ResultValue(ResultFrame, f'{scgz:.2f} cm³')

            scgyLabel = widgets.ResultLabel(ResultFrame, 'Scgy =')
            scgyContent = widgets.ResultValue(ResultFrame, f'{scgy:.2f} cm³')

            kzLabel = widgets.ResultLabel(ResultFrame, 'kz =')
            kzContent = widgets.ResultValue(ResultFrame, f'{kz:.2f} cm³')

            kyLabel = widgets.ResultLabel(ResultFrame, 'ky =')
            kyContent = widgets.ResultValue(ResultFrame, f'{ky:.2f} cm³')

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

            kzLabel.grid(row=8, column=0, padx=(25, 5), pady=5, sticky='e')
            kzContent.grid(row=8, column=1, padx=10, pady=5, sticky='w')

            kyLabel.grid(row=9, column=0, padx=(25, 5), pady=5, sticky='e')
            kyContent.grid(row=9, column=1, padx=10, pady=5, sticky='w')

            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra(i_section, [w, h, cy]))
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
            iValuesImage = utilities.create_image(self, ['Shapes', 'iValues.png'])
            DotImage = utilities.create_image(self, ['Shapes', 'dot.png'])
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=iValuesImage)
            ShapeCanvas.create_image(CanvasWidth/2, CanvasHeight/2, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(iValuesImage)
            self.ImageList.append(DotImage)

            # Cria A Linha Do Ycg
            x1 = 18; y1 = CanvasHeight / 2; x2 = x1 + 9; y2 = 796
            # ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)


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

            try:
                x = float(entry[0].get())
                y = float(entry[1].get())
                a = float(entry[2].get())
                d = float(entry[3].get())
                h = float(entry[4].get())
                r = float(entry[5].get())
            except ValueError:
                return

            medidas = [x, y, a, d, h, r]
            if 0 in medidas:
                return
            else:
                del medidas

            self.ClearMainSpace()

            # Calcular As Seções Geométricas
            h_section  = HSection(x, y, a, d, h, r)

            area = h_section.area
            perim = h_section.area
            cy = h_section.cy
            cx = h_section.cx
            iz = h_section.iz
            iy = h_section.iy
            scgz = h_section.scgz
            scgy = h_section.scgy
            kz = h_section.kz
            ky = h_section.ky

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

            kzLabel = widgets.ResultLabel(ResultFrame, 'Kz =')
            kzContent = widgets.ResultValue(ResultFrame, f'{kz:.2f} cm³')

            kyLabel = widgets.ResultLabel(ResultFrame, 'Ky =')
            kyContent = widgets.ResultLabel(ResultFrame, f'{ky:.2f} cm')

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

            kzLabel.grid(row=8, column=0, padx=(25, 5), pady=5, sticky='e')
            kzContent.grid(row=8, column=1, padx=10, pady=5, sticky='w')

            kyLabel.grid(row=9, column=0, padx=(25, 5), pady=5, sticky='e')
            kyContent.grid(row=9, column=1, padx=10, pady=5, sticky='w')

            # Cria Os Widgets Para O FibraFrame
            FibraButton = widgets.OpenFibraButton(ButtonFrame, lambda: self.OpenFibra(h_section, [x, y, a, d, h, r, cy]))
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
            RomanIValuesImage = utilities.create_image(self, ['Shapes', 'RomanIValues.png'])
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

            DotImage = utilities.create_image(self, ['Shapes', 'dot.png'])
            ShapeCanvas.create_image(CanvasWidth/2, DotHeight, anchor=tk.CENTER, image=DotImage)
            self.ImageList.append(DotImage)

            x1 = 283; y1 = DotHeight; x2 = x1 + 9; y2 = CanvasHeight - 37

            # Cria A Linha Do Ycg
            # ShapeCanvas.create_rectangle(x1, y1, x2, y2, fill='#121212', width=0)
            # ShapeCanvas.create_text(x2 + 10, y2, text='Ycg', font=self.ResultFont, fill='#303030', anchor='sw')


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
    App(root)
    root.mainloop()
