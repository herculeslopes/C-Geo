# Fórmulas do U

def getYcg(x, y, a, h):
    ycg = ((2 * (a * y * (y / 2))) + (h * x * (x / 2))) / ((2 * (a * y)) + (x * h))
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'a = {a}')
    print(f'h = {h}')
    print(f'ycg = {ycg}')
    return ycg


def getIz(x, y, a, h, ycg):
    iz = (2 * (((a * y ** 3) / (12)) + ((y * a * ((y / 2) - ycg) ** 2)))) + ((((h) * (x ** 3)) / (12)) + (x * h * ((ycg - (x / 2)) ** 2)))
    print(f'iz = {iz}')
    return iz


def getScg(x, y, a, h, ycg):
    scg = (((y - ycg) * (a + h + a)) - ((y - ycg) * (h))) * ((y - ycg) / 2)
    print(f'scg = {scg}')
    return scg
