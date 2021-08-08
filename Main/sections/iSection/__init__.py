# Fórmulas do I

def getYcg(h):
    ycg = h / 2
    print(f'h = {h}')
    print(f'ycg = {ycg}')
    return ycg


def getIz(h, w):
    iz = (w * (h ** 3)) / 12
    print(f'w = {w}')
    print(f'iz = {iz}')
    return iz


def getScg(w, ycg):
    scg = (w * ycg * (ycg / 2))
    print(f'scg = {scg}')
    return scg
