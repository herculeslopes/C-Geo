import screeninfo, ctypes, os
from PIL import ImageTk, Image

# ctypes.windll.shcore.SetProcessDpiAwareness(2)

def get_screen_info():
    """ Define a resolução e taxa de zoom do display.

    Quando o programa rodar em um monitor com resolução < fullhd
    ou zoom > 100% as imagens serão criadas em um tamanho < original.
    """

    # Pega A Quantidade De Pixels Da Tela (Windows)
    user32 = ctypes.windll.user32
    relative_resolution = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

    # Pega A Resolução Real Da Tela (Monitor)
    screen_resolution = screeninfo.get_monitors()[0].width, screeninfo.get_monitors()[0].height

    if screen_resolution == (1920, 1080):
        if relative_resolution == screen_resolution: zoom_ratio = 100

        elif relative_resolution == (1536, 864): zoom_ratio = 125

        elif relative_resolution == (1280, 720): zoom_ratio = 150

        else: zoom_ratio = 0

    elif screen_resolution == (1280, 720):
        if relative_resolution == relative_resolution: zoom_ratio = 150

        else: zoom_ratio = 100

    else: zoom_ratio = 100

    return screen_resolution, zoom_ratio


def create_image(self, path_elements, resize=None):
    path = os.path.join('rsc', 'img', *path_elements)
    """Cria um objeto de imagem ImageTk proporcial a resolução da tela.
    
    No primeiro parâmetro do método ImageFile.resize é passado uma tupla
    contendo as medidas x e y para a criação da imagem. Essas medidas são
    armazenadas nas variáveis x_size e y_size.

    Parâmetros
    ----------
    path: string
        Caminho das imagens
    """
    
    image_file = Image.open(path)
    img_width, img_height = image_file.size
    
    if self.windows_zoom == 100:
        x_size = img_width
        y_size = img_height

    elif self.windows_zoom == 125:
        x_size = img_width - (img_width * 0.25)
        y_size = img_height - (img_height * 0.25)

    elif self.windows_zoom == 150:
        x_size = img_width - (img_width * 0.50)
        y_size = img_height - (img_height * 0.50)

    elif self.windows_zoom == 175:
        x_size = img_width - (img_width * 0.75)
        y_size = img_height - (img_height * 0.75)

    if resize == None:
        TkImage = ImageTk.PhotoImage(image_file.resize((int(x_size), int(y_size)), Image.ANTIALIAS))
    else:
        TkImage = ImageTk.PhotoImage(image_file.resize((resize[0], resize[1]), Image.ANTIALIAS))

    return TkImage

