import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

class MainProgram:
    def __init__(self, master):
        self.root = master
        self.root.title('Características Geométricas')
        self.root.state('zoomed')

        self.SideFrame = tk.Frame(master, bg='#c9c9c9', width=90, bd=0)
        self.SideFrame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.MainSpace = tk.Frame(master, bg='#dbdbdb', bd=0)
        self.MainSpace.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.EntryFont = Font(family='Arial', size=20)
        self.ResultFont = Font(family='Arial', size=16)
        self.WarningFont = Font(size=50)

        self.WindowsZoom = 125

        self.SideFramePacking()     


    def SideFramePacking(self):
        tButtonImage = self.CreateImage(r'Images\Buttons\tButton.png')
        self.tButton = tk.Button(self.SideFrame, image=tButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0)
        self.tButton.image = tButtonImage
        self.tButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        LButtonImage = self.CreateImage(r'Images\Buttons\LButton.png')
        self.LButton = tk.Button(self.SideFrame, image=LButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0)
        self.LButton.image = LButtonImage
        self.LButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        uButtonImage = self.CreateImage(r'Images\Buttons\uButton.png')
        self.uButton = tk.Button(self.SideFrame, image=uButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0)
        self.uButton.image = uButtonImage
        self.uButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        cButtonImage = self.CreateImage(r'Images\Buttons\cButton.png')
        self.cButton = tk.Button(self.SideFrame, image=cButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0)
        self.cButton.image = cButtonImage
        self.cButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        iButtonImage = self.CreateImage(r'Images\Buttons\iButton.png')
        self.iButton = tk.Button(self.SideFrame, image=iButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0)
        self.iButton.image = iButtonImage
        self.iButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        RomanIButtonImage = self.CreateImage(r'Images\Buttons\RomanIButton.png')
        self.RomanIButton = tk.Button(self.SideFrame, image=RomanIButtonImage, bg='#c9c9c9', activebackground='#c9c9c9', bd=0)
        self.RomanIButton.image = RomanIButtonImage
        self.RomanIButton.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


    def ClearMainSpace(self):
        for widget in self.MainSpace.winfo_children():
            widget.destroy()


    def CreateImage(self, path):
        ImageFile = Image.open(path)
        ImageWidth, ImageHeight = ImageFile.size
        
        if self.WindowsZoom == 125:
            xSize = ImageWidth - (ImageWidth * 0.25)
            ySize = ImageHeight - (ImageHeight * 0.25)

        TkImage = ImageTk.PhotoImage(ImageFile.resize((int(xSize), int(ySize)), Image.ANTIALIAS))
        
        return TkImage


def main():
    root = tk.Tk()
    MainProgram(root)
    root.mainloop()


if __name__ == '__main__':
    main()
