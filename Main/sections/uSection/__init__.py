# Fórmulas do U

def get_area(x, y, a, h):
    area = 2 * a * y + x * h
    print(f'area = {area}')
    return area


def get_perim(x, y, a, h):
    perim = 2 * y + 2 * (2 * a + h) + 2 * (y - x)
    print(f'perímetro = {perim}')
    return perim
    

def get_cy(x, y, a, h):
    cy = ((2 * (a * y * (y / 2))) + (h * x * (x / 2))) / ((2 * (a * y)) + (x * h))
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'a = {a}')
    print(f'h = {h}')
    print(f'ycg = {cy}')
    return cy


def get_cx(a, h):
    cx = (h + 2 * a) / 2
    print(f'cx = {cx}')
    return cx


def get_j(a, h, cx):
    j = h + (2 * a) - cx
    print(f'j = {j}')
    return j


def get_iz(x, y, a, h, cy):
    iz = (2 * (((a * y ** 3) / (12)) + ((y * a * ((y / 2) - cy) ** 2)))) + ((((h) * (x ** 3)) / (12)) + (x * h * ((cy - (x / 2)) ** 2)))
    print(f'iz = {iz}')
    return iz


def get_scgz(x, y, a, h, cy):
    scgz = (((y - cy) * (a + h + a)) - ((y - cy) * (h))) * ((y - cy) / 2)
    print(f'scg = {scgz}')
    return scgz


def get_fibra(x, y, a, h, ycg, fibra, pos):
    if ((pos == 'ACIMA') and (ycg + fibra <= y)) or ((pos == 'ABAIXO') and (ycg - fibra >= 0)):
        if ycg > x:
            if pos == 'ACIMA':
                if (ycg + fibra) < y:
                    m = y - (ycg + fibra)
                    S = m * (a + h + a) * ((m / 2) + fibra)

            elif pos == 'ABAIXO':
                if (ycg - fibra) > x: 
                    i =(ycg - x) - fibra 
                    S = (x * (h + a + a) * ((x / 2) + i + fibra)) + ( 2 * (i * a * ((i / 2) + fibra)))

                elif (ycg - fibra) <= (x):
                    m = ycg - fibra
                    S = m * (h + a + a) * ((m / 2 ) + fibra)

        elif ycg < x:
            if pos == 'ABAIXO':
                if(ycg - fibra) < (x):
                    i = ycg - fibra
                    S = i * (a + a + h) * ((i / 2) + fibra)

            elif pos == 'ACIMA':
                if (ycg + fibra) >= x:
                    m = y - (ycg + fibra) 
                    S = 2 * ( m * a * ((m / 2) + fibra))       

                elif (ycg + fibra) < x:
                    v = y - x
                    m = (ycg + fibra) - x 
                    S = (m * (a + h + a) * ((m / 2)+ fibra)) + (2 * (a * v * ((v / 2) + fibra + m)))


        else:
            if pos=='ABAIXO':
                if (ycg - fibra) <= x:
                    i = ycg - fibra
                    S = (h + a + a) * i * ((i / 2) + fibra)

            elif pos == 'ACIMA':
                if ( ycg + fibra) >= x:
                    v = (ycg + fibra)
                    S = (v * a * ((v / 2) + fibra)) * 2 


    else:
        S = -1

    return S
