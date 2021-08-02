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
