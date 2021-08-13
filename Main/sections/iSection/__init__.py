# Fórmulas do I

def get_area(w, h):
    area = w * h
    print(f'area = {area}')
    return area


def get_perim(w, h):
    perim = 2 * w + 2 * h
    print(f'perímetro = {perim}')
    return perim

    
def get_ycg(h):
    ycg = h / 2
    print(f'h = {h}')
    print(f'ycg = {ycg}')
    return ycg


def get_iz(h, w):
    iz = (w * (h ** 3)) / 12
    print(f'w = {w}')
    print(f'iz = {iz}')
    return iz


def get_scg(w, ycg):
    scg = (w * ycg * (ycg / 2))
    print(f'scg = {scg}')
    return scg


def get_fibra(w, h, ycg, fibra):
    if fibra <= (h / 2):
        S = ((ycg - fibra) * w) * (((ycg - fibra) / 2) + fibra)

    else:
        S = -1

    return S

