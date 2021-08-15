# Fórmulas do I

def get_area(w, h):
    area = w * h
    print(f'area = {area}')
    return area


def get_perim(w, h):
    perim = 2 * w + 2 * h
    print(f'perímetro = {perim}')
    return perim

    
def get_cy(h):
    cy = h / 2
    print(f'h = {h}')
    print(f'ycg = {cy}')
    return cy


def get_cx(w):
    cx = w / 2
    print(f'w = {w}')
    return cx


def get_iz(h, w):
    iz = (w * (h ** 3)) / 12
    print(f'w = {w}')
    print(f'iz = {iz}')
    return iz


def get_iy(h, w):
    iy = (h * (w ** 3)) / 12
    print(f'iy = {iy}')
    return iy
    

def get_scgz(w, ycg):
    scgz = (w * ycg * (ycg / 2))
    print(f'scg = {scgz}')
    return scgz


def get_scgy(h, w, cx):
    scgy = h * w * cx
    print(f'scgy = {scgy}') 
    return scgy


def get_fibra(w, h, ycg, fibra):
    if fibra <= (h / 2):
        S = ((ycg - fibra) * w) * (((ycg - fibra) / 2) + fibra)

    else:
        S = -1

    return S

