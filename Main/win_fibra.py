import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
from formulas import tSection, lSection, uSection, cSection, iSection, hSection
import widgets

class FibraWindow():
    def __init__(self, master, section, values):
        self.win_fibra = master

        self.win_fibra.grab_set()
        self.win_fibra.geometry("700x400")
        self.win_fibra.title(f"Calcular Fibra {section.upper()}")
        self.win_fibra['bg'] = '#dbdbdb'
        self.win_fibra.resizable(0, 0)

        self.imgCalc = ImageTk.PhotoImage(Image.open('img/btn/calculate.png'))
        self.imgDisc = ImageTk.PhotoImage(Image.open('img/btn/discard.png'))

        self.section = section

        self.label_fibra = Font(family='Calibri', size=16)

        self.FibraOptions = (
            "ACIMA",
            "ABAIXO"
        )

        values = [float(valor) for valor in values] # Converte as medidas para float

        self.pos = ''

        self.sectionValues = values

        self.main_layout()


    def set_pos(self, pos):
        self.pos = pos

        print(pos)

        if pos == 'ABAIXO':
            self.abButton['relief'] = tk.SUNKEN
            self.abButton['bg'] = '#B0B0B0'
            self.acButton['relief'] = tk.FLAT
            self.acButton['bg'] = '#8c8c8c'

        elif pos == 'ACIMA':
            self.abButton['relief'] = tk.FLAT
            self.abButton['bg'] = '#8c8c8c'
            self.acButton['relief'] = tk.SUNKEN
            self.acButton['bg'] = '#b0b0b0'


    def clearValues(self):
        self.entryDist.delete(0, tk.END)
        self.lblFibra['text'] = ''
        self.abButton['relief'] = tk.FLAT
        self.acButton['relief'] = tk.FLAT
        self.abButton['bg'] = '#8c8c8c'
        self.acButton['bg'] = '#8c8c8c'
        self.pos = ''


    def main_layout(self):
        frmMain = tk.Frame(self.win_fibra, bg="#dbdbdb")
        frmMain.pack(side=tk.TOP, fill=tk.X, padx=100)

        lblDist = widgets.WinFibraLabel(frmMain, "Distância da fibra")
        lblDist.pack(pady=(30, 5))

        self.entryDist = widgets.WinFibraEntry(frmMain)
        self.entryDist.pack(fill=tk.X) # , padx=100

        lblPos = widgets.WinFibraLabel(frmMain, "Posição da fibra")
        lblPos.pack(pady=(20, 5))

        """self.comboPos = widgets.FibraCombo(frmMain)
        self.comboPos.pack(anchor='w')"""

        frmPos = tk.Frame(frmMain, bg='#dbdbdb')
        frmPos.pack()

        self.abButton = widgets.ButtonPos(frmPos, 'ABAIXO', lambda: self.set_pos('ABAIXO'))
        self.abButton.pack(side=tk.LEFT, padx=(0, 10))

        self.acButton = widgets.ButtonPos(frmPos, 'ACIMA', lambda: self.set_pos('ACIMA'))
        self.acButton.pack(side=tk.RIGHT, padx=(10, 0))

        self.lblFibra = widgets.FibraResult(frmMain)
        self.lblFibra.pack(pady=(40, 0))

        # frmLine = tk.Frame(frmMain, bg="#121212", height=3)
        frmLine = widgets.EntryLine(frmMain)
        frmLine.pack(expand=True, fill=tk.X)

        frmMenu = tk.Frame(self.win_fibra, bg='#dbdbdb', bd=0)
        frmMenu.pack(side=tk.BOTTOM, pady=(0, 25))

        CalculateButton = widgets.MenuButton(frmMenu, img=self.imgCalc, action=self.show_result)
        DiscardButton = widgets.MenuButton(frmMenu, img=self.imgDisc, action=self.clearValues)

        CalculateButton.grid(row=0, column=0, padx=5)
        DiscardButton.grid(row=0, column=1, padx=5)

        self.entryDist.focus_set()


    def show_result(self):
        distancia = float(self.entryDist.get())
        posicao = self.pos

        if self.section == 't':
            result = tSection.get_fibra(*self.sectionValues, distancia, posicao)

        elif self.section == 'l':
            result = lSection.get_fibra(*self.sectionValues, distancia, posicao)

        elif self.section == 'u':
            result = uSection.get_fibra(*self.sectionValues, distancia, posicao)
        
        elif self.section == 'c':
            result = cSection.get_fibra(*self.sectionValues, distancia, posicao)

        elif self.section == 'i':
            result = iSection.get_fibra(*self.sectionValues, distancia)
        
        elif self.section == 'h':
            result = hSection.get_fibra(*self.sectionValues, distancia, posicao)
        
        print(f'Fibra: {result}')
        print(f'Tipo: {type(result)}')

        if result != -1:
            self.lblFibra['text'] = f'{result} cm³'

        else:
            self.lblFibra['text'] = 'NÃO É POSSÍVEL CALCULAR'
