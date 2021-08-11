# Fórmulas do H

def get_area(x, y, a, d, h, r):
    area = x * y + h * a + d * r
    print(f'area = {area}')
    return area


def get_perim(x, y, a, d, h, r):
    perim = 2 * d + 2 * y + r * x + 2 * h + (x - a) + (r * a)
    print(f'perim = {perim}')
    return perim

    
def get_ycg(x, y, a, d, h, r):
    ycg = ((a * r * (a / 2)) + (h * d * (a + (h / 2))) + (y * x * (a + h + (y / 2)))) / ((a * r) + (d * h) + (y * x))
    return ycg


def get_iz(x, y, a, d, h, r, ycg):
    iz = (((r * (a ** 3)) / (12)) + ((a * r * (((ycg - (a / 2)) ** 2))))) + (((d * (h ** 3)) / 12) + (h * d * ((((h / 2) + a) - (ycg)) ** 2))) + (((x * (y ** 3)) / 12) + (y * x * (((a + h + (y / 2)) - ycg) ** 2)))
    return iz


def get_scg(x, y, a, d, h, r, ycg):
    if ycg == a:
        print('Primeira Fórmula')
        scg = a * r * (a / 2)

    elif ycg == (a + h):
        print('Segunda Fórmula')
        scg = y * x * (y / 2)

    elif ycg < (a + h) and ycg > a:
        print('Terceira Fórmula')
        scg = (a * r * (ycg - (a / 2))) + (d * (ycg - a) * ((ycg - a) / 2))
    
    return scg


def get_fibra(x, y, a, d, h, r, ycg, fibra, pos):
    if ((pos == 'ACIMA') and (ycg + fibra <= y + d + h)) or ((pos == 'ABAIXO') and (ycg - fibra >= 0)):
        if ycg >= (h + d):
            if pos == 'ACIMA':
                if (ycg + fibra) < (y + d + h):
                    i = ((ycg + fibra) - (y + h + d))
                    S = i * x * ((i/2) + fibra)

            elif pos == 'ABAIXO':
                if (ycg - fibra) <= (d + h) and (ycg - fibra) > (d):
                    i = ( d + h) - (ycg - fibra)
                    S = ((i * a * ((i / 2) + fibra)) + (d * r * ((d / 2) + i + fibra)))

                elif (ycg - fibra) <= (d):
                    u = ( ycg - fibra)  
                    S = u * r * ((u / 2) + fibra)

                elif (ycg - fibra) > (d + h):    
                    u = (ycg - fibra) - (h + d)
                    S = (u * x * ((u / 2 ) + fibra)) + (h * a * ((h / 2) + u + fibra)) + d * r * ((d / 2) + h + u + fibra)

        elif (ycg > d ) and ycg <= ( d + h):     
            if pos =='ACIMA':      
                if (ycg + fibra) >= (d + h):
                    i = ( d + h + y) - (ycg + fibra)
                    S = i * x * ((i / 2) + fibra)
                
                elif (ycg + fibra) <= ( d + h) and (ycg + fibra) >= (d):
                    i = (d + h) - (ycg + fibra)
                    S = (y * x * ((y / 2) + i + fibra)) + (i * a * ((i / 2) + fibra))

            elif pos == 'ABAIXO':
                if (ycg - fibra) > (d):
                    v = (d + h) - ( ycg - fibra)    
                    S = (v * a * ((v / 2) + fibra)) + (d * r * ((d / 2) + fibra))

                elif (ycg - fibra) <= (d): 
                    v = (ycg - fibra)
                    S = v * r * ((v / 2) + fibra)

        elif ( ycg <= d ):
            if pos == 'ABAIXO':
                if ( ycg - fibra) <= (d):
                    g = (ycg - fibra)
                    S = g * r * ((g / 2)+ fibra)

            elif pos == 'ACIMA':
                if (ycg + fibra) >= (d + h):
                    i = (d + h + fibra) - (ycg + fibra)
                    S = (i * x * ((i / 2)+ fibra))

                elif (ycg + fibra) >= (d):
                    m = (h + d) - (ycg + fibra)    
                    S = y * x * ((y / 2) + fibra)

                elif (ycg + fibra) < (d):   
                    m = (d) - (ycg + fibra)
                    S = (y * x * ((y / 2) + h + m + fibra)) + (h * a * ((h / 2) + m + fibra)) + (m * r * ((m / 2) + fibra)) 
        
        sLabel = str(S) + "cm³"

    else:
        # sLabel['fg'] = '#eb4034'
        sLabel = 'NÃO É POSSÍVEL CALCULAR'
    
    return sLabel
