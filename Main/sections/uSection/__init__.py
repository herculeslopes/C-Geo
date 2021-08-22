from math import sqrt

# Fórmulas do U

def get_area(x, y, a, h):
    area = 2 * a * y + x * h
    return area


def get_perim(x, y, a, h):
    perim = 2 * y + 2 * (2 * a + h) + 2 * (y - x)
    return perim
    

def get_cy(x, y, a, h):
    cy = (
            ((2 * (a * y * (y / 2))) + (h * x * (x / 2)))
            /
            ((2 * (a * y)) + (x * h))
        )

    return cy


def get_cx(a, h):
    cx = (h + 2 * a) / 2
    return cx


def get_j(a, h, cx):
    j = h + (2 * a) - cx
    return j


def get_g(y, x):
    g = y - x
    return g


def get_iz(x, y, a, h, cy):
    iz = (
            (2 * (((a * y ** 3) / (12)) + ((y * a * ((y / 2) - cy) ** 2))))
            +
            ((((h) * (x ** 3)) / (12)) + (x * h * ((cy - (x / 2)) ** 2)))
        )

    return iz


def get_iy(x, y, a, cx):
    g = y - x
    iy = (x * cx ** 3) / 12 + cx * x * (cx / 2) ** 2 + (g * a ** 3) + (g * a * (cx - (a / 2)) ** 2)
    return iy


def get_scgz(x, y, a, h, cy):
    v = y - x

    if cy <= x:
        scgz = cy * (a + h + a) * (cy / 2) 
    
    else:
        scgz = ((y - cy) * a * ((v - cy) / 2)) * 2

    return scgz


def get_scgy(x, a, j, g):
    scgy = (j * x * (j / 2)) + (g * a * (j * (a / 2)))
    return scgy


def get_kz(a, iz):
    kz = sqrt(iz / a)
    return kz


def get_ky(a, iy):
    ky = sqrt(iy / a)
    return ky


def get_fibra(x, y, a, h, cy, fibra, pos):
    if ((pos == 'ACIMA') and (cy + fibra <= y)) or ((pos == 'ABAIXO') and (cy - fibra >= 0)):
        if cy > x:
            if pos == 'ACIMA':
                if (cy + fibra) < y:
                    m = y - (cy + fibra)
                    S = m * (a + h + a) * ((m / 2) + fibra)

            elif pos == 'ABAIXO':
                if (cy - fibra) > x: 
                    i =(cy - x) - fibra 
                    S = (x * (h + a + a) * ((x / 2) + i + fibra)) + ( 2 * (i * a * ((i / 2) + fibra)))

                elif (cy - fibra) <= x:
                    m = cy - fibra
                    S = m * (h + a + a) * ((m / 2 ) + fibra)

        elif cy < x:
            if pos == 'ABAIXO':
                if(cy - fibra) < x:
                    i = cy - fibra
                    S = i * (a + a + h) * ((i / 2) + fibra)

            elif pos == 'ACIMA':
                if (cy + fibra) >= x:
                    m = y - (cy + fibra) 
                    S = 2 * ( m * a * ((m / 2) + fibra))       

                elif (cy + fibra) < x:
                    v = y - x
                    m = (cy + fibra) - x 
                    S = (m * (a + h + a) * ((m / 2)+ fibra)) + (2 * (a * v * ((v / 2) + fibra + m)))

        else:
            if pos=='ABAIXO':
                if (cy - fibra) <= x:
                    i = cy - fibra
                    S = (h + a + a) * i * ((i / 2) + fibra)

            elif pos == 'ACIMA':
                if (cy + fibra) >= x:
                    v = (cy + fibra)
                    S = (v * a * ((v / 2) + fibra)) * 2 

    else:
        S = -1

    return S
