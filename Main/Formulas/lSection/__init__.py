# Fórmulas do L

def getYcg(y, k, x, u):
    ycg = ((x * u * (x / 2)) + (k * y * ((k / 2) + x))) / (x * u + k * y)
    print(f'y = {y}')
    print(f'k = {k}')
    print(f'x = {x}')
    print(f'u = {u}')
    print(f'ycg = {ycg}')
    return ycg
            

def getIx(y, k, x, u, ycg):
    t = x + (k / 2)
    h = (x / 2)
    ix = (((y * k ** 3) / 12+y * k * (t - ycg) ** 2)+((u * x ** 3 / 12)+u * x * (ycg - h) ** 2))

    print(f't = {t}')
    print(f'h = {h}')
    print(f'ix = {ix}')

def getIz():
    pass

def getScg():
    pass
