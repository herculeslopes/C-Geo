from math import sqrt

# Fórmulas do H

def get_area(x, y, a, d, h, r):
    area = x * y + h * a + d * r
    return area


def get_perim(x, y, a, d, h, r):
    perim = 2 * d + 2 * y + r * x + 2 * h + (x - a) + (r * a)
    return perim

    
def get_cy(x, y, a, d, h, r):
    cy = (
        ((a * r * (a / 2)) + (h * d * (a + (h / 2))) + (y * x * (a + h + (y / 2))))
        /
        ((a * r) + (d * h) + (y * x))
    )
    
    return cy


def get_cx(x, r):
    if x >= r:
        cx = x / 2

    elif x < r:
        cx = r / 2

    return cx


def get_iz(x, y, a, d, h, r, cy):
    iz = (
        (((r * (a ** 3)) / (12)) + ((a * r * (((cy - (a / 2)) ** 2)))))
        +
        (((d * (h ** 3)) / 12) + (h * d * ((((h / 2) + a) - cy) ** 2)))
        +
        (((x * (y ** 3)) / 12) + (y * x * (((a + h + (y / 2)) - cy) ** 2)))
    )

    return iz


def get_iy(x, y, a, d, h, r):
    iy = (d * (r ** 3)) / 12 + ((h * (a ** 3)) / 12) + ((y * (x ** 3))/ 12)
    return iy   


def get_scgz(x, y, a, d, h, r, cy):
    if cy >= (y + h + d):
        scgz = (y + h + d - cy) * x * ((y + h + d - cy) / 2)
    
    elif cy < h + d:
        scgz = d * r * ((d / 2) + (cy - d)) + (cy - d) * a * ((cy - d) / 2)

    elif cy <= d:
        scgz = cy * r * (cy / 2)

    return scgz


def get_scgy(x, y, a, d, h, r):
    scgy = (r / 2) * d * (r / 4) + y * (x / 2) * (x / 4) + h * (a / 2) * (a / 4)
    return scgy


def get_kz(area, iz):
    kz = sqrt(iz / area)
    return kz


def get_ky(area, iy):
    ky = sqrt(iy / area)
    return ky


def get_fibra(x, y, a, d, h, r, cy, fibra, pos):
    if ((pos == 'ACIMA') and (cy + fibra <= y + d + h)) or ((pos == 'ABAIXO') and (cy - fibra >= 0)):
        if cy >= (h + d):
            if pos == 'ACIMA':
                if (cy + fibra) < (y + d + h):
                    i = ((cy + fibra) - (y + h + d))
                    S = i * x * ((i/2) + fibra)

            elif pos == 'ABAIXO':
                if (cy - fibra) <= (d + h) and (cy - fibra) > d:
                    i = ( d + h) - (cy - fibra)
                    S = ((i * a * ((i / 2) + fibra)) + (d * r * ((d / 2) + i + fibra)))

                elif (cy - fibra) <= d:
                    u = ( cy - fibra)  
                    S = u * r * ((u / 2) + fibra)

                elif (cy - fibra) > (d + h):    
                    u = (cy - fibra) - (h + d)
                    S = (u * x * ((u / 2 ) + fibra)) + (h * a * ((h / 2) + u + fibra)) + d * r * ((d / 2) + h + u + fibra)

        elif (cy > d) and cy <= (d + h):     
            if pos =='ACIMA':      
                if (cy + fibra) >= (d + h):
                    i = ( d + h + y) - (cy + fibra)
                    S = i * x * ((i / 2) + fibra)
                
                elif (cy + fibra) <= ( d + h) and (cy + fibra) >= d:
                    i = (d + h) - (cy + fibra)
                    S = (y * x * ((y / 2) + i + fibra)) + (i * a * ((i / 2) + fibra))

            elif pos == 'ABAIXO':
                if (cy - fibra) > d:
                    v = (d + h) - ( cy - fibra)    
                    S = (v * a * ((v / 2) + fibra)) + (d * r * ((d / 2) + fibra))

                elif (cy - fibra) <= d: 
                    v = (cy - fibra)
                    S = v * r * ((v / 2) + fibra)

        elif ( cy <= d ):
            if pos == 'ABAIXO':
                if ( cy - fibra) <= d:
                    g = (cy - fibra)
                    S = g * r * ((g / 2)+ fibra)

            elif pos == 'ACIMA':
                if (cy + fibra) >= (d + h):
                    i = (d + h + fibra) - (cy + fibra)
                    S = (i * x * ((i / 2)+ fibra))

                elif (cy + fibra) >= d:
                    m = (h + d) - (cy + fibra)    
                    S = y * x * ((y / 2) + fibra)

                elif (cy + fibra) < d:   
                    m = (d) - (cy + fibra)
                    S = (y * x * ((y / 2) + h + m + fibra)) + (h * a * ((h / 2) + m + fibra)) + (m * r * ((m / 2) + fibra)) 
        
    else:
        S = -1 # NÃO DEVE ACONTECER
    
    return S
