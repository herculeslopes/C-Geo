# Fórmulas do I

def getYcg(h):
    ycg = h / 2
    return ycg


def getIz(h, w):
    iz = (w * (h ** 3)) / 12
    return iz


def getScg(w, ycg):
    scg = (w * ycg * (ycg / 2))
    return scg
