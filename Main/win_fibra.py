import enum
import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from sections import tSection

class FibraWindow():
    def __init__(self, master, values):
        self.win_fibra = master
        self.win_fibra.geometry("700x400")
        self.win_fibra.title("Calcular Fibra")
        self.win_fibra['bg'] = '#dbdbdb'
        self.win_fibra.resizable(0, 0)
        # self.win_fibra.attributes('-topmost', True)
        # self.win_fibra.grab_set()

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

    def main_layout(self):
        frmMain = tk.Frame(self.win_fibra, bg="#dbdbdb")
        frmMain.pack(fill=tk.X)

        lblDist = tk.Label(frmMain, font=self.label_fibra, text="Distância da fibra:")
        lblDist.grid(row=0, column=0, sticky='w', padx=20)

        self.entryDist = tk.Entry(frmMain, font=self.label_fibra)
        self.entryDist.grid(row=0, column=1, sticky='w')

        lblPos = tk.Label(frmMain, font=self.label_fibra, text="Posição da fibra: ")
        lblPos.grid(row=1, column = 0, sticky='w', padx=20)

        self.comboPos = ttk.Combobox(frmMain, font=self.label_fibra, values=self.FibraOptions, width=10)
        self.comboPos.current(0)
        self.comboPos.grid(row=1, column=1, sticky='w')

        btnCalc = tk.Button(frmMain, text='Calcular Fibra', command=self.show_result)
        btnCalc.grid(row=2, column=0, sticky='w', padx=20)

        self.lblFibra = tk.Label(frmMain)
        self.lblFibra.grid(row=3, column=0, sticky='w', padx=20)

    
    def show_result(self):
        distancia = float(self.entryDist.get())
        posicao = self.comboPos.get()
        result = tSection.getFibra(*self.sectionValues, distancia, posicao)
        self.lblFibra['text'] = result

