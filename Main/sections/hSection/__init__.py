# Fórmulas do H

def get_area(x, y, a, d, h, r):
    area = x * y + h * a + d * r
    return area


def get_perim(x, y, a, d, h, r):
    perim = 2 * d + 2 * y + r * x + 2 * h + (x - a) + (r * a)
    return perim

    
def get_cy(x, y, a, d, h, r):
    cy = ((a * r * (a / 2)) + (h * d * (a + (h / 2))) + (y * x * (a + h + (y / 2)))) / ((a * r) + (d * h) + (y * x))
    return cy


def get_cx(x, r):
    if x >= r:
        cx = x / 2

    elif x < r:
        cx = r / 2

    return cx


def get_iz(x, y, a, d, h, r, cy):
    iz = (((r * (a ** 3)) / (12)) + ((a * r * (((cy - (a / 2)) ** 2))))) + (((d * (h ** 3)) / 12) + (h * d * ((((h / 2) + a) - cy) ** 2))) + (((x * (y ** 3)) / 12) + (y * x * (((a + h + (y / 2)) - cy) ** 2)))
    return iz


def get_iy(x, y, a, d, h, r):
    iy = (d * (r ** 3)) / 12 + ((h * (a ** 3)) / 12) + ((y * (x ** 3))/ 12)
    return iy


def get_scgz(x, y, a, d, h, r, cy):
    if cy == a:
        scg = a * r * (a / 2)

    elif cy == (a + h):
        scg = y * x * (y / 2)

    elif cy < (a + h) and cy > a:
        scg = (a * r * (cy - (a / 2))) + (d * (cy - a) * ((cy - a) / 2))
    
    return scg


def get_scgy(x, y, a, d, h, r):
    scgy = (r / 2) * d * (r / 4) + y * (x / 2) * (x / 4) + h * (a / 2) * (a / 4)
    return scgy


def get_fibra(x, y, a, d, h, r, ycg, fibra, pos):
    if ((pos == 'ACIMA') and (ycg + fibra <= y + d + h)) or ((pos == 'ABAIXO') and (ycg - fibra >= 0)):
        if ycg >= (h + d):
            if pos == 'ACIMA':
                if (ycg + fibra) < (y + d + h):
                    i = ((ycg + fibra) - (y + h + d))
                    S = i * x * ((i/2) + fibra)

            elif pos == 'ABAIXO':
                if (ycg - fibra) <= (d + h) and (ycg - fibra) > d:
                    i = ( d + h) - (ycg - fibra)
                    S = ((i * a * ((i / 2) + fibra)) + (d * r * ((d / 2) + i + fibra)))

                elif (ycg - fibra) <= d:
                    u = ( ycg - fibra)  
                    S = u * r * ((u / 2) + fibra)

                elif (ycg - fibra) > (d + h):    
                    u = (ycg - fibra) - (h + d)
                    S = (u * x * ((u / 2 ) + fibra)) + (h * a * ((h / 2) + u + fibra)) + d * r * ((d / 2) + h + u + fibra)

        elif (ycg > d) and ycg <= (d + h):     
            if pos =='ACIMA':      
                if (ycg + fibra) >= (d + h):
                    i = ( d + h + y) - (ycg + fibra)
                    S = i * x * ((i / 2) + fibra)
                
                elif (ycg + fibra) <= ( d + h) and (ycg + fibra) >= d:
                    i = (d + h) - (ycg + fibra)
                    S = (y * x * ((y / 2) + i + fibra)) + (i * a * ((i / 2) + fibra))

            elif pos == 'ABAIXO':
                if (ycg - fibra) > d:
                    v = (d + h) - ( ycg - fibra)    
                    S = (v * a * ((v / 2) + fibra)) + (d * r * ((d / 2) + fibra))

                elif (ycg - fibra) <= d: 
                    v = (ycg - fibra)
                    S = v * r * ((v / 2) + fibra)

        elif ( ycg <= d ):
            if pos == 'ABAIXO':
                if ( ycg - fibra) <= d:
                    g = (ycg - fibra)
                    S = g * r * ((g / 2)+ fibra)

            elif pos == 'ACIMA':
                if (ycg + fibra) >= (d + h):
                    i = (d + h + fibra) - (ycg + fibra)
                    S = (i * x * ((i / 2)+ fibra))

                elif (ycg + fibra) >= d:
                    m = (h + d) - (ycg + fibra)    
                    S = y * x * ((y / 2) + fibra)

                elif (ycg + fibra) < d:   
                    m = (d) - (ycg + fibra)
                    S = (y * x * ((y / 2) + h + m + fibra)) + (h * a * ((h / 2) + m + fibra)) + (m * r * ((m / 2) + fibra)) 
        
    else:
        S = -1 # NÃO DEVE ACONTECER
    
    return S
