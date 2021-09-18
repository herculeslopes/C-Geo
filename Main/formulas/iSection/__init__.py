from math import sqrt

# Fórmulas do I

def get_area(w, h):
    area = w * h
    return area


def get_perim(w, h):
    perim = 2 * w + 2 * h
    return perim

    
def get_cy(h):
    cy = h / 2
    return cy


def get_cx(w):
    cx = w / 2
    return cx


def get_iz(h, w):
    iz = (w * (h ** 3)) / 12
    return iz


def get_iy(h, w):
    iy = (h * (w ** 3)) / 12
    return iy
    

def get_scgz(w, ycg):
    scgz = (w * ycg * (ycg / 2))
    return scgz


def get_scgy(h, w):
    scgy = h * ( w / 2 ) * ( w / 4 ) 
    return scgy


def get_kz(area, iz):
    kz = sqrt(iz / area)
    return kz


def get_ky(area, iy):
    ky = sqrt(iy / area)
    return ky


def get_fibra(w, h, cy, fibra):
    if fibra <= (h / 2):
        S = ((cy - fibra) * w) * (((cy - fibra) / 2) + fibra)

    else:
        S = -1

    return S

