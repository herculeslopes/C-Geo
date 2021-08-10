import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from PIL import ImageTk, Image
from sections import tSection, lSection, uSection, cSection, iSection, hSection
import widgets

class FibraWindow():
    def __init__(self, master, section, values):
        self.win_fibra = master
        self.win_fibra.geometry("700x400")
        self.win_fibra.title("Calcular Fibra")
        self.win_fibra['bg'] = '#dbdbdb'
        self.win_fibra.resizable(0, 0)
        # self.win_fibra.attributes('-topmost', True)
        # self.win_fibra.grab_set()

        self.imgCalc = ImageTk.PhotoImage(Image.open('Images/Buttons/calculate.png'))
        self.imgDisc = ImageTk.PhotoImage(Image.open('Images/Buttons/discard.png'))

        print(f'Imagem: {self.imgCalc}')

        self.section = section

        self.label_fibra = Font(family='Calibri', size=16)

        self.FibraOptions = (
            "ACIMA",
            "ABAIXO"
        )

        # Coverte cada valor de values para float
        print(f'antes = {type(values[0])}')
        for index, valor in enumerate(values):
            print(f'index = {index}, valor = {valor}')
            values[index] = float(valor)

        print(f'antes = {type(values[0])}')

        self.sectionValues = values

        self.main_layout()

    def clearValues(self):
        self.entryDist.delete(0, tk.END)
        self.lblFibra['text'] = ''

    def main_layout(self):
        frmMain = tk.Frame(self.win_fibra, bg="#dbdbdb")
        frmMain.pack(side=tk.TOP, fill=tk.X, padx=100)

        self.lblFibra = widgets.FibraResult(frmMain)
        self.lblFibra.pack(pady=(40, 0))

        frmLine = tk.Frame(frmMain, bg="#121212", height=3)
        frmLine.pack(expand=True, fill=tk.X)

        lblDist = widgets.WinFibraLabel(frmMain, "Distância da fibra")
        lblDist.pack(anchor='w', pady=(30, 5))

        self.entryDist = widgets.WinFibraEntry(frmMain)
        self.entryDist.pack(fill=tk.X) # , padx=100

        lblPos = widgets.WinFibraLabel(frmMain, "Posição da fibra")
        lblPos.pack(anchor='w', pady=(20, 5))

        self.comboPos = widgets.FibraCombo(frmMain)
        self.comboPos.pack(anchor='w')
        
        frmMenu = tk.Frame(self.win_fibra, bg='#dbdbdb', bd=0)
        frmMenu.pack(side=tk.BOTTOM, pady=(0, 25))

        CalculateButton = widgets.MenuButton(frmMenu, img=self.imgCalc, action=self.show_result)
        DiscardButton = widgets.MenuButton(frmMenu, img=self.imgDisc, action=self.clearValues)

        CalculateButton.grid(row=0, column=0, padx=5)
        DiscardButton.grid(row=0, column=1, padx=5)


    def show_result(self):
        distancia = float(self.entryDist.get())
        posicao = self.comboPos.get()

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
        
        self.lblFibra['text'] = result
