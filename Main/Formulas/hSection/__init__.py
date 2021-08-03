# Fórmulas do H

def getYcg(x, y, a, d, h, r):
    ycg = ((a * r * (a / 2)) + (h * d * (a + (h / 2))) + (y * x * (a + h + (y / 2)))) / ((a * r) + (d * h) + (y * x))
    return ycg


def getIz(x, y, a, d, h, r, ycg):
    iz = (((r * (a ** 3)) / (12)) + ((a * r * (((ycg - (a / 2)) ** 2))))) + (((d * (h ** 3)) / 12) + (h * d * ((((h / 2) + a) - (ycg)) ** 2))) + (((x * (y ** 3)) / 12) + (y * x * (((a + h + (y / 2)) - ycg) ** 2)))
    return iz


def getScg(x, y, a, d, h, r, ycg):
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
