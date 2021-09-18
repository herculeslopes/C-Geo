import tkinter as tk
from PIL import ImageTk, Image
import widgets
from webbrowser import open_new as webbrowser_open_new

class CreditsWindow():
    def __init__(self, window):
        self.win_credits = window

        self.win_credits.grab_set()
        self.win_credits.resizable(0, 0)
        self.win_credits.title('Credits')
        self.win_credits.geometry('800x500')

        self.win_credits.configure(
            bg='#dbdbdb'
        )

        self.main_layout()


    def open_profile(self, url):
        webbrowser_open_new(url)

    def main_layout(self):
        self.MainFrame = tk.Frame(
            self.win_credits,
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

        hercules_pic = ImageTk.PhotoImage(Image.open('img/hercules.png').resize((184, 184), Image.ANTIALIAS))
        HerculesPic = tk.Label(HerculesProfile, image=hercules_pic, bg='#dbdbdb', bd=0)
        HerculesPic.image = hercules_pic
        HerculesGitHub = widgets.ProfileLink(HerculesProfile, 'Github Hércules Lopes', lambda e: self.open_profile(urls['hercules_github']))
        Hercules_Linkedin = widgets.ProfileLink(HerculesProfile, 'Linkedin Hércules Lopes', lambda e: self.open_profile(urls['hercules_linkedin']))
        HerculesDescription = widgets.ProfileDescription(HerculesProfile, hercules_desc)
        
        alex_pic = ImageTk.PhotoImage(Image.open('img/lecao.jpg').resize((184, 184), Image.ANTIALIAS))
        AlexPic = tk.Label(AlexProfile, image=alex_pic, bg='#dbdbdb', bd=0)
        AlexPic.image = alex_pic
        AlexGithub = widgets.ProfileLink(AlexProfile, 'Github Alex Gomes', lambda e: self.open_profile(urls['alex_github']))
        AlexLinkedin = widgets.ProfileLink(AlexProfile, 'Linkedin Alex Gomes', lambda e: self.open_profile(urls['alex_linkedin']))
        AlexDescription = widgets.ProfileDescription(AlexProfile, alex_desc)

        HerculesPic.pack(pady=10)
        HerculesGitHub.pack(anchor='w')
        Hercules_Linkedin.pack(anchor='w')
        HerculesDescription.pack()

        AlexPic.pack(pady=10)
        AlexGithub.pack(anchor='w')
        AlexLinkedin.pack(anchor='w')
        AlexDescription.pack(fill=tk.X)



