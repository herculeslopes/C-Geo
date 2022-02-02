import tkinter as tk
from webbrowser import open_new as webbrowser_open_new
from os import path
from .. import widgets
from .. import utilities

class InfoWindow():
    TITLE = 'Info'
    LOGO_PATH = path.join('rsc', 'img', 'c-geo.ico')
    SIZE = (800, 500)

    def __init__(self, app, toplevel):
        self.app = app
        self.win_info = toplevel
    
        self.win_info.grab_set()
        self.win_info.resizable(0, 0)
        self.win_info.title(InfoWindow.TITLE)
        self.win_info.iconbitmap(InfoWindow.LOGO_PATH)
        self.win_info.geometry(f'{InfoWindow.SIZE[0]}x{InfoWindow.SIZE[1]}')

        self.win_info.configure(
            bg='#dbdbdb'
        )

        self.main_layout()


    def open_profile(self, url):
        webbrowser_open_new(url)


    def main_layout(self):
        self.MainFrame = tk.Frame(
            self.win_info,
            bg='#dbdbdb'
        )
        self.ProfileFrame = tk.Frame(
            self.MainFrame,
            bg='#dbdbdb',
        )

        self.MainFrame.pack(fill=tk.BOTH)
        self.ProfileFrame.pack(expand=True)


        urls = {
            'hercules_github': 'https://github.com/herculeslopes',
            'hercules_linkedin': 'https://www.linkedin.com/in/hércules-lopes-612758215/',
            'alex_github': 'https://github.com/alexlecao',
            'alex_linkedin': 'https://www.linkedin.com/in/alex-gomes-eng-civil/'
        }

        hercules_desc = '''
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quidem odio est minus, facere vel nihil, modi inventore eveniet explicabo, veritatis adipisci reprehenderit odit accusantium quibusdam in doloribus possimus fugit? Et?Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quidem odio est minus, facere vel nihil, modi inventore eveniet explicabo, veritatis adipisci reprehenderit odit accusantium quibusdam in doloribus possimus fugit? Et?
        '''

        alex_desc = '''
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quidem odio est minus, facere vel nihil, modi inventore eveniet explicabo, veritatis adipisci reprehenderit odit accusantium quibusdam in doloribus possimus fugit? Et?Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quidem odio est minus, facere vel nihil, modi inventore eveniet explicabo, veritatis adipisci reprehenderit odit accusantium quibusdam in doloribus possimus fugit? Et?
        '''

        HerculesProfile = tk.Frame(self.ProfileFrame, bg='#dbdbdb')
        AlexProfile = tk.Frame(self.ProfileFrame, bg='#dbdbdb')

        HerculesProfile.pack(side=tk.LEFT, padx=10)
        AlexProfile.pack(side=tk.RIGHT, padx=10)

        # hercules_pic = ImageTk.PhotoImage(Image.open('img/info/python.png').resize((100, 100), Image.ANTIALIAS)) # resize(184, 184)
        hercules_pic = utilities.create_image(self.app, ['info', 'python.png'], (100, 100))
        HerculesPic = tk.Label(HerculesProfile, image=hercules_pic, bg='#dbdbdb', bd=0)
        HerculesTitle = widgets.ProfileTitle(HerculesProfile, 'Python Dev')
        HerculesPic.image = hercules_pic
        HerculesDescription = widgets.ProfileDescription(HerculesProfile, hercules_desc)
        HerculesGitHub = widgets.ProfileLink(HerculesProfile, 'Github Hércules Lopes', lambda e: self.open_profile(urls['hercules_github']))
        Hercules_Linkedin = widgets.ProfileLink(HerculesProfile, 'Linkedin Hércules Lopes', lambda e: self.open_profile(urls['hercules_linkedin']))
        
        # alex_pic = ImageTk.PhotoImage(Image.open('img/info/engenharia-civil.png').resize((100, 100), Image.ANTIALIAS))
        alex_pic = utilities.create_image(self.app, ['info', 'engenharia-civil.png'], (100, 100))
        AlexPic = tk.Label(AlexProfile, image=alex_pic, bg='#dbdbdb', bd=0)
        AlexTitle = widgets.ProfileTitle(AlexProfile, 'Engenheiro Civil')
        AlexPic.image = alex_pic
        AlexDescription = widgets.ProfileDescription(AlexProfile, alex_desc)
        AlexGithub = widgets.ProfileLink(AlexProfile, 'Github Alex Gomes', lambda e: self.open_profile(urls['alex_github']))
        AlexLinkedin = widgets.ProfileLink(AlexProfile, 'Linkedin Alex Gomes', lambda e: self.open_profile(urls['alex_linkedin']))
        
        HerculesPic.pack(pady=10)
        HerculesTitle.pack()
        HerculesDescription.pack()
        HerculesGitHub.pack(anchor='w')
        Hercules_Linkedin.pack(anchor='w')

        AlexPic.pack(pady=10)
        AlexTitle.pack()
        AlexDescription.pack(fill=tk.X)
        AlexGithub.pack(anchor='w')
        AlexLinkedin.pack(anchor='w')



