# Fórmulas do L

from math import sqrt

def get_area(y, k, x, u):
    area = x * u + k * y
    return area


def get_perim(y, k, x, u):
    perim = 2 * u + 2 * x + 2 * k
    return perim


def get_cy(y, k, x, u):
    cy = ((x * u * (x / 2)) + (k * y * ((k / 2) + x))) / (x * u + k * y)
    return cy
            

def get_cx(y, k, x, u):
    cx = ((y * k * (y / 2)) + (x * u * (u / 2))) / (x * u + y * k)
    return cx


def get_iz(y, k, x, u, cy):
    t = x + (k / 2)
    h = (x / 2)
    iz = (
            ((y * k ** 3) / 12 + y * k * (t - cy) ** 2)
            +
            ((u * x ** 3 / 12) + u * x * (cy - h) ** 2)
        )
        
    return iz


def get_iy(y, k, x, u, cy):
    iy = (
            ((y * k ** 3) / 3 + k * y * (cy - y / 2) ** 2)
            +
            (x * u ** 3 / 12 + x * u * (u / 2 * cy))
        )
        
    return iy


def get_scgz(y, k, x, u, cy):
    a = k + x

    if cy >= x:
        scgz = (a - cy) * y * ((a - cy) / 2)

    else:
        scgz = cy * u * (cy / 2)

    return scgz


def get_scgy(y, k, x, u, cx):
    if x >= y:
        scgy = x * (u - cx) * (u - cx / 2)

    else:
        scgy = cx * k * (cx / 2)

    return scgy


def get_kz(k, x, iz):
    a = k + x
    kz = sqrt(iz / a)
    return kz


def get_ky(k, x, iy):
    a = k + x
    ky = sqrt(iy / a)
    return ky


def get_fibra():
    pass
