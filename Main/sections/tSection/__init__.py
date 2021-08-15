# Fórmulas do T

def get_area(x, b, y, z):
    area = x * b + y *z
    print(f'area = {area}')
    return area


def get_perim(x, b, y, z):
    perimetro = z + 2 * y + 2 * b + x + x - z
    print(f'perimetro = {perimetro}')
    return perimetro


def get_cy(x, b, y, z):
    cy = (z * y * (y / 2) + b * x * (y + (b / 2))) / (z * y + b * x)
    print(f'x = {x}')
    print(f'b = {b}')
    print(f'y = {y}')
    print(f'z = {z}')
    print(f'ycg = {cy}')
    return cy


def get_cx(x):
    cx = x / 2
    print(f'cx = {cx}')
    return cx


def get_iz(x, b, y, z, cy):
    iz = (((x * (b ** 3)) / (12) ) + (b * x * ((y + (b / 2) - cy)) ** 2)) + (((z * (y ** 3)) / (12)) + (y * z * ((cy - (y / 2)) ** 2)))
    print(f'iz = {iz}')
    return iz


def get_iy(x, b, y, z):
    iy = ((y * z ** 3) / 12) + ((b * x ** 3) / 12)
    print(f'iy = {iy}')
    return iy


def get_scgz(x, b, y, z, cy):
    if cy < y or cy == y:
        scgz = (cy * z * (cy / 2))
            
    else:
        scgz = x * (y + b - cy) * ((y + b - cy) / 2)

    print(f'scg = {scgz}')
    return scgz


def get_scgy(x, b, y, z):
    scgy = (z / 2) * y * (z / 4) + (x / 2) * b * (x / 4)
    print(f'scgy = {scgy}')
    return scgy


def get_fibra(x, b, y, z, ycg, fibra, pos):
    # fibra = float(FibraEntry.get())
    # pos = OptionSelected.get()

    print(f'x = {x}, {type(x)}')
    print(f'b = {b}, {type(b)}')
    print(f'y = {y}, {type(y)}')
    print(f'z = {z}, {type(z)}')
    print(f'ycg = {ycg}, {type(ycg)}')
    print(f'Fibra = {fibra}, {type(fibra)}')
    print(f'Posição = {pos}, {type(pos)}')

    if ((pos == 'ACIMA') and (ycg + fibra <= y + b)) or ((pos == 'ABAIXO') and (ycg - fibra >= 0)):
        if ycg > y:
            if pos == 'ABAIXO':
                if ycg - fibra < y:
                    h = ycg - fibra
                    S = h * z * ((h / 2) + fibra)
                
                elif ycg - fibra > y:
                    d = ycg - fibra - y
                    S = (d * x * ((d / 2) + fibra)) + (y * z * ((y / 2) + d + fibra))

                elif ycg - fibra == y:
                    S = y * z * (y / 2) + fibra

            elif pos == 'ACIMA':
                if ycg + fibra < ( y + b):
                    i = y + b  - (ycg + fibra)
                    S = i * x * ((i / 2) + fibra)
                        
        elif ycg < y:
            if pos == 'ACIMA':
                if (ycg + fibra) == y:
                    S = b * x * ((b / 2) + fibra)

                elif (ycg + fibra) < y:
                    i = y - (ycg + fibra)
                    S = (b * x * ((b / 2 )+ (fibra + i))) + (i * z * ((i/2) + fibra))

                elif (ycg + fibra) > y: 
                    a = (y + b) - (ycg + fibra)
                    S = a * x * ((a/2) + fibra)        

            elif pos == 'ABAIXO':
                if (ycg - fibra < y):
                    d = ycg - fibra
                    S = d * z * ((d / 2 ) + fibra)
            
        else:
            if pos == 'ACIMA':
                if (ycg + fibra) > y:
                    a = b - fibra
                    S = a * x * ((a / 2) + fibra)
                        
            elif pos == 'ABAIXO':
                if (ycg - fibra) < y:
                    a = ycg - fibra
                    S = a * z * ((a / 2) + fibra) 

    else:
        S = -1

    return S
