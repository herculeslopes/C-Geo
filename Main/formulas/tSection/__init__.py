from math import sqrt

# Fórmulas do T

def get_area(x, b, y, z):
    area = x * b + y *z
    return area


def get_perim(x, b, y, z):
    perimetro = z + 2 * y + 2 * b + x + x - z
    return perimetro


def get_cy(x, b, y, z):
    cy = (z * y * (y / 2) + b * x * (y + (b / 2))) / (z * y + b * x)
    return cy


def get_cx(x):
    cx = x / 2
    return cx


def get_iz(x, b, y, z, cy):
    iz = (
        (((x * (b ** 3)) / (12) ) + (b * x * ((y + (b / 2) - cy)) ** 2))
        +
        (((z * (y ** 3)) / (12)) + (y * z * ((cy - (y / 2)) ** 2)))
        )
        
    return iz


def get_iy(x, b, y, z):
    iy = ((y * z ** 3) / 12) + ((b * x ** 3) / 12)
    return iy


def get_scgz(x, b, y, z, cy):
    if cy == y:
        scgz = y * z * (y / 2)
    
    elif cy < y:
        scgz = cy * z * (cy / 2)

    else:
        scgz = (b + y - cy) * x * ((b + y - cy) / 2)
        
    return scgz


def get_scgy(x, b, y, z):
    scgy = (z / 2) * y * (z / 4) + (x / 2) * b * (x / 4)
    return scgy


def get_kz(area, iz):
    kz = sqrt(iz / area)
    return kz


def get_ky(area, iy):
    ky = sqrt(iy / area)
    return ky


def get_fibra(x, b, y, z, cy, fibra, pos):
    if ((pos == 'ACIMA') and (cy + fibra <= y + b)) or ((pos == 'ABAIXO') and (cy - fibra >= 0)):
        if cy > y:
            if pos == 'ABAIXO':
                if cy - fibra < y:
                    h = cy - fibra
                    S = h * z * ((h / 2) + fibra)
                
                elif cy - fibra > y:
                    d = cy - fibra - y
                    S = (d * x * ((d / 2) + fibra)) + (y * z * ((y / 2) + d + fibra))

                elif cy - fibra == y:
                    S = y * z * (y / 2) + fibra

            elif pos == 'ACIMA':
                if cy + fibra < ( y + b):
                    i = y + b  - (cy + fibra)
                    S = i * x * ((i / 2) + fibra)
                        
        elif cy < y:
            if pos == 'ACIMA':
                if (cy + fibra) == y:
                    S = b * x * ((b / 2) + fibra)

                elif (cy + fibra) < y:
                    i = y - (cy + fibra)
                    S = (b * x * ((b / 2 )+ (fibra + i))) + (i * z * ((i/2) + fibra))

                elif (cy + fibra) > y: 
                    a = (y + b) - (cy + fibra)
                    S = a * x * ((a/2) + fibra)        

            elif pos == 'ABAIXO':
                if (cy - fibra < y):
                    d = cy - fibra
                    S = d * z * ((d / 2 ) + fibra)
            
        else:
            if pos == 'ACIMA':
                if (cy + fibra) > y:
                    a = b - fibra
                    S = a * x * ((a / 2) + fibra)
                        
            elif pos == 'ABAIXO':
                if (cy - fibra) < y:
                    a = cy - fibra
                    S = a * z * ((a / 2) + fibra) 

    else:
        S = -1

    return S
