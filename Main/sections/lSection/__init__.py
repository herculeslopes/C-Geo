# Fórmulas do L

def get_area(y, k, x, u):
    area = x * u + k * y
    print(f'area = {area}')
    return area


def get_perim(y, k, x, u):
    perim = 2 * u + 2 * x + 2 * k
    print(f'perímetro = {perim}')
    return perim


def get_ycg(y, k, x, u):
    ycg = ((x * u * (x / 2)) + (k * y * ((k / 2) + x))) / (x * u + k * y)
    print(f'y = {y}')
    print(f'k = {k}')
    print(f'x = {x}')
    print(f'u = {u}')
    print(f'ycg = {ycg}')
    return ycg
            

def get_ix(y, k, x, u, ycg):
    t = x + (k / 2)
    h = (x / 2)
    ix = (((y * k ** 3) / 12+y * k * (t - ycg) ** 2)+((u * x ** 3 / 12)+u * x * (ycg - h) ** 2))

    print(f't = {t}')
    print(f'h = {h}')
    print(f'ix = {ix}')

def get_iy(y, k, x, u, ycg):
    iy = ((y * k ** 3) / 3 + k * y * (ycg - y / 2) ** 2) + (x * u ** 3 / 12 + x * u * (u / 2 * ycg))
    return iy

def get_scg():
    pass


def get_fibra():
    pass
