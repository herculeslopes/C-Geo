# Fórmulas do T

def getYcg(x, b, y, z):
    ycg = (z * y * (y / 2) + b * x * (y + (b / 2))) / (z * y + b * x)
    print(f'x = {x}')
    print(f'b = {b}')
    print(f'y = {y}')
    print(f'z = {z}')
    print(f'ycg = {ycg}')
    return ycg


def getIz(x, b, y, z, ycg):
    iz = (((x * (b ** 3)) / (12) ) + (b * x * ((y + (b / 2) - ycg)) ** 2)) + (((z * (y ** 3)) / (12)) + (y * z * ((ycg - (y / 2)) ** 2)))
    print(f'iz = {iz}')
    return iz


def getScg(x, b, y, z, ycg):
    if ycg < y or ycg == y:
        scg = (ycg * z * (ycg / 2))
            
    else:
        scg = x * (y + b - ycg) * ((y + b - ycg) / 2)

    print(f'scg = {scg}')
    return scg


def getFibra(x, b, y, z, ycg, fibra, pos):
    # fibra = float(FibraEntry.get())
    # pos = OptionSelected.get()

    if ((pos == 'ACIMA') and (ycg + fibra <= y + b)) or ((pos == 'ABAIXO') and (ycg - fibra >= 0)):
        if ycg > y:
            if pos == 'ABAIXO':
                if ycg - fibra < y:
                    h = ycg - fibra
                    S = h * z * ((h / 2) + fibra)
                    print('1')
                
                elif ycg - fibra > y:
                    d = ycg - fibra - y
                    S = (d * x * ((d / 2) + fibra)) + (y * z * ((y / 2) + d + fibra))
                    print('2')

                elif ycg - fibra == y:
                    S = y * z * (y / 2) + fibra
                    print('3')

            elif pos == 'ACIMA':
                if ycg + fibra < ( y + b):
                    i = y + b  - (ycg + fibra)
                    S = i * x * ((i / 2) + fibra)
                        
                print('4')

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
                    print('5')
            
        elif ycg == y:
            if pos == 'ACIMA':
                if (ycg + fibra) > y:
                    a = b - fibra
                    S = a * x * ((a / 2) + fibra)
            
                print('6')
            
            elif pos == 'ABAIXO':
                if (ycg - fibra) < y:
                    a = ycg - fibra
                    S = a * z * ((a / 2) + fibra) 

            print('7')

        # sLabel['text'] = S
        sLabel = str(S)

    else:
        # sLabel['fg'] = '#eb4034'
        # sLabel['text'] = 'NÃO É POSSÍVEL CALCULAR'
        sLabel = 'NÃO É POSSÍVEL CALCULAR'
        print('8')

    return sLabel
