from math import sqrt

# Fórmulas do C

def get_area(b, h, a, m):
    area = 2 * (a + m) * b + h * a
    return area


def get_perim(b, h, a, m):
    perimetro = 2 * (a + m) + 2 * (2 * b + h) + 2 * m
    return perimetro


def get_cy(b, h, a, m):
    x = a + m
    cy = ((b * x * (b / 2)) + h * a * (b + (h / 2)) + (b * x * (b + h + (b / 2)))) / h * a + b * x + b * x
    return cy


def get_cx(b, h, a, m):
    x = a + m
    cx = (b * x * (x / 2) + h * a * (a / 2) + b * x * (x / 2)) / h * a + b * x + b * x
    return cx


def get_iz(b, h, a, m, cy):
    x = a + m
    iz = (
            ((x * b ** 3 / 12) + (x * b * (cy - (b / 2)) ** 2))
            +
            ((a * h ** 3 / 12) + ((cy - ((h / 2) + b)) ** 2 * (a * h)))
            +
            ((x * b ** 3 / 12) + (x * b * (cy - ((b / 2) + h + b) ** 2)))
        )

    return iz


def get_iy(b, h, a, m, cy):
    iy = 2 * (
                (((b * (m + a) ** 3) / 12) + b * (m + a) * ((cy - ((m + a) / 2)) ** 2))
                +
                (h * a ** 3 / 12 + h * a * ((cy - (a / 2)) ** 2))
            )
            
    return iy


def get_scgz(b, h, a, m, cy):
    if cy >= (2 * b + h):
        scgz = (2 * b + h - cy) * (a + m) * ((2 * b + h - cy) / 2)
        return scgz
    
    elif cy < (h + b):
        scgz = b * (a + m) * (cy - b / 2) + (cy - b) * a * ((cy - b) / 2)

    elif cy <= b:
        scgz = cy * (a + m) * (cy / 2)

    return scgz


def get_kz(area, iz):
    kz = sqrt(iz / area)
    return kz


def get_ky(area, iy):
    ky = sqrt(iy / area)
    return ky

def get_fibra():
    pass
