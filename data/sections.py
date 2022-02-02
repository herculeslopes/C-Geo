from math import sqrt

class TSection:
    def __init__(self, x, b, y, z):
        self.x = x
        self.b = b
        self.y = y
        self.z = z

        self.letter = 'T'

        self.set_area()
        self.set_perimeter()
        self.set_cy()
        self.set_cx()
        self.set_iz()
        self.set_iy()
        self.set_scgz()
        self.set_scgy()
        self.set_kz()
        self.set_ky()

    
    def set_area(self):
        x, b, y, z = self.x, self.b, self.y, self.z
        self.area = x * b + y *z


    def set_perimeter(self):
        x, b, y, z = self.x, self.b, self.y, self.z
        self.perimeter = z + 2 * y + 2 * b + x + x - z


    def set_cy(self):
        x, b, y, z = self.x, self.b, self.y, self.z
        self.cy = (z * y * (y / 2) + b * x * (y + (b / 2))) / (z * y + b * x)


    def set_cx(self):
        x, b, y, z = self.x, self.b, self.y, self.z
        self.cx = x / 2


    def set_iz(self):
        x, b, y, z = self.x, self.b, self.y, self.z
        cy = self.cy
        self.iz = (
            (((x * (b ** 3)) / (12) ) + (b * x * ((y + (b / 2) - cy)) ** 2))
            +
            (((z * (y ** 3)) / (12)) + (y * z * ((cy - (y / 2)) ** 2)))
        )


    def set_iy(self):
        x, b, y, z = self.x, self.b, self.y, self.z
        self.iy = ((y * z ** 3) / 12) + ((b * x ** 3) / 12)


    def set_scgz(self):
        x, b, y, z = self.x, self.b, self.y, self.z
        cy = self.cy
        if cy == y:
            self.scgz = y * z * (y / 2)
        
        elif cy < y:
            self.scgz = cy * z * (cy / 2)

        else:
            self.scgz = (b + y - cy) * x * ((b + y - cy) / 2)
            

    def set_scgy(self):
        x, b, y, z = self.x, self.b, self.y, self.z
        self.scgy = (z / 2) * y * (z / 4) + (x / 2) * b * (x / 4)


    def set_kz(self):
        area, iz = self.area, self.iz
        self.kz = sqrt(iz / area)


    def set_ky(self):
        area, iy = self.area, self.iy
        self.ky = sqrt(iy / area)


    def get_fibra(self, length, position):
        x, b, y, z = self.x, self.b, self.y, self.z
        cy = self.cy
        if ((position == 'up') and (cy + length <= y + b)) or ((position == 'down') and (cy - length >= 0)):
            if cy > y:
                if position == 'down':
                    if cy - length < y:
                        h = cy - length
                        S = h * z * ((h / 2) + length)
                    
                    elif cy - length > y:
                        d = cy - length - y
                        S = (d * x * ((d / 2) + length)) + (y * z * ((y / 2) + d + length))

                    elif cy - length == y:
                        S = y * z * (y / 2) + length

                elif position == 'up':
                    if cy + length < ( y + b):
                        i = y + b  - (cy + length)
                        S = i * x * ((i / 2) + length)
                            
            elif cy < y:
                if position == 'up':
                    if (cy + length) == y:
                        S = b * x * ((b / 2) + length)

                    elif (cy + length) < y:
                        i = y - (cy + length)
                        S = (b * x * ((b / 2 )+ (length + i))) + (i * z * ((i/2) + length))

                    elif (cy + length) > y: 
                        a = (y + b) - (cy + length)
                        S = a * x * ((a/2) + length)        

                elif position == 'down':
                    if (cy - length < y):
                        d = cy - length
                        S = d * z * ((d / 2 ) + length)
                
            else:
                if position == 'up':
                    if (cy + length) > y:
                        a = b - length
                        S = a * x * ((a / 2) + length)
                            
                elif position == 'down':
                    if (cy - length) < y:
                        a = cy - length
                        S = a * z * ((a / 2) + length) 

        else:
            S = -1

        return S

class LSection:
    def __init__(self, y, k, x, u):
        self.y = y
        self.k = k
        self.x = x
        self.u = u

        self.letter = 'L'

        self.set_area()
        self.set_perimeter()
        self.set_cy()
        self.set_cx()
        self.set_iz()
        self.set_iy()
        self.set_scgz()
        self.set_scgy()
        self.set_kz()
        self.set_ky()


    def set_area(self):
        x, u, k, y = self.x, self.u, self.k, self.y
        self.area = x * u + k * y


    def set_perimeter(self):
        x, u, k, y = self.x, self.u, self.k, self.y
        self.perimeter = 2 * u + 2 * x + 2 * k


    def set_cy(self):
        x, u, k, y = self.x, self.u, self.k, self.y
        self.cy = ((x * u * (x / 2)) + (k * y * ((k / 2) + x))) / (x * u + k * y)
                

    def set_cx(self):
        x, u, k, y = self.x, self.u, self.k, self.y
        self.cx = ((y * k * (y / 2)) + (x * u * (u / 2))) / (x * u + y * k)


    def set_iz(self):
        x, u, k, y = self.x, self.u, self.k, self.y
        cy = self.cy
        t = x + (k / 2)
        h = (x / 2)
        self.iz = (
                ((y * k ** 3) / 12 + y * k * (t - cy) ** 2)
                +
                ((u * x ** 3 / 12) + u * x * (cy - h) ** 2)
            )
            

    def set_iy(self):
        x, u, k, y = self.x, self.u, self.k, self.y
        cx = self.cx
        self.iy = (
            (
                ((k * (y ** 3)) / 12) + (y * k * ((cx - (y / 2)) ** 2))
            )
            +
            (
                ((x * (u ** 3)) / 12) + (u * x * ((cx - (u / 2)) ** 2))
            )
        )
            
        
    def set_scgz(self):
        x, u, k, y = self.x, self.u, self.k, self.y
        cy = self.cy
        a = k + x

        if cy >= x:
            self.scgz = (a - cy) * y * ((a - cy) / 2)

        else:
            self.scgz = cy * u * (cy / 2)


    def set_scgy(self):
        x, u, k, y = self.x, self.u, self.k, self.y
        cx = self.cx
        if x >= y:
            self.scgy = x * (u - cx) * (u - cx / 2)

        else:
            self.scgy = cx * k * (cx / 2)


    def set_kz(self):
        iz, area = self.iz, self.area
        self.kz = sqrt(iz / area)


    def set_ky(self):
        iy, area = self.iy, self.area
        self.ky = sqrt(iy / area)
    

    def get_fibra(self, length, position):
        pass

class USection:
    def __init__(self, x, y, a, h):
        self.x = x
        self.y = y
        self.a = a
        self.h = h

        self.letter = 'U'

        self.set_area()
        self.set_perimeter()
        self.set_cy()
        self.set_cx()
        self.set_j()
        self.set_g()
        self.set_iz()
        self.set_iy()
        self.set_scgz()
        self.set_scgy()
        self.set_kz()
        self.set_ky()

    def set_area(self):
        a, y, x, h = self.a, self.y, self.x, self.h
        self.area = 2 * a * y + x * h


    def set_perimeter(self):
        a, y, x, h = self.a, self.y, self.x, self.h
        self.perimeter = 2 * y + 2 * (2 * a + h) + 2 * (y - x)
        

    def set_cy(self):
        a, y, x, h = self.a, self.y, self.x, self.h
        self.cy = (
                ((2 * (a * y * (y / 2))) + (h * x * (x / 2)))
                /
                ((2 * (a * y)) + (x * h))
            )


    def set_cx(self):
        a, h = self.a, self.h
        self.cx = (h + 2 * a) / 2


    def set_j(self):
        a, h = self.a, self.h
        cx = self.cx
        self.j = h + (2 * a) - cx


    def set_g(self):
        y, x = self.y, self.x
        self.g = y - x


    def set_iz(self):
        a, y, x, h = self.a, self.y, self.x, self.h
        cy = self.cy
        self.iz = (
                (2 * (((a * y ** 3) / (12)) + ((y * a * ((y / 2) - cy) ** 2))))
                +
                ((((h) * (x ** 3)) / (12)) + (x * h * ((cy - (x / 2)) ** 2)))
            )


    def set_iy(self):
        a, y, x = self.a, self.y, self.x
        cx = self.cx
        g = y - x
        self.iy = (x * cx ** 3) / 12 + cx * x * (cx / 2) ** 2 + (g * a ** 3) + (g * a * (cx - (a / 2)) ** 2)


    def set_scgz(self):
        a, y, x, h = self.a, self.y, self.x, self.h
        cy = self.cy
        v = y - x

        if cy <= x:
            self.scgz = cy * (a + h + a) * (cy / 2) 
        
        else:
            self.scgz = ((y - cy) * a * ((v - cy) / 2)) * 2


    def set_scgy(self):
        a, y, x = self.a, self.y, self.x
        j = self.j
        g = y - x
        self.scgy = (j * x * (j / 2)) + (g * a * (j * (a / 2)))


    def set_kz(self):
        area, iz = self.area, self.iz
        self.kz = sqrt(iz / area)


    def set_ky(self):
        area, iy = self.area, self.iy
        self.ky = sqrt(iy / area)


    def get_fibra(self, length, position):
        a, y, x, h = self.a, self.y, self.x, self.h
        cy = self.cy
        if ((position == 'up') and (cy + length <= y)) or ((position == 'down') and (cy - length >= 0)):
            if cy > x:
                if position == 'up':
                    if (cy + length) < y:
                        m = y - (cy + length)
                        S = m * (a + h + a) * ((m / 2) + length)

                elif position == 'down':
                    if (cy - length) > x: 
                        i =(cy - x) - length 
                        S = (x * (h + a + a) * ((x / 2) + i + length)) + ( 2 * (i * a * ((i / 2) + length)))

                    elif (cy - length) <= x:
                        m = cy - length
                        S = m * (h + a + a) * ((m / 2 ) + length)

            elif cy < x:
                if position == 'down':
                    if(cy - length) < x:
                        i = cy - length
                        S = i * (a + a + h) * ((i / 2) + length)

                elif position == 'up':
                    if (cy + length) >= x:
                        m = y - (cy + length) 
                        S = 2 * ( m * a * ((m / 2) + length))       

                    elif (cy + length) < x:
                        v = y - x
                        m = (cy + length) - x 
                        S = (m * (a + h + a) * ((m / 2)+ length)) + (2 * (a * v * ((v / 2) + length + m)))

            else:
                if position=='down':
                    if (cy - length) <= x:
                        i = cy - length
                        S = (h + a + a) * i * ((i / 2) + length)

                elif position == 'up':
                    if (cy + length) >= x:
                        v = (cy + length)
                        S = (v * a * ((v / 2) + length)) * 2 

        else:
            S = -1

        return S

class CSection:
    def __init__(self, b, h, a, m):
        self.b = b
        self.h = h
        self.a = a
        self.m = m

        self.letter = 'C'

        self.set_area()
        self.set_perimeter()
        self.set_cy()
        self.set_cx()
        self.set_iz()
        self.set_iy()
        self.set_scgz()
        # self.set_scgy()
        self.set_kz()
        self.set_ky()

    def set_area(self):
        b, h, a, m = self.b, self.h, self.a, self.m
        self.area = 2 * (a + m) * b + h * a


    def set_perimeter(self):
        b, h, a, m = self.b, self.h, self.a, self.m
        self.perimeter = 2 * (a + m) + 2 * (2 * b + h) + 2 * m


    def set_cy(self):
        b, h, a, m = self.b, self.h, self.a, self.m
        x = a + m
        self.cy = ((b * x * (b / 2)) + h * a * (b + (h / 2)) + (b * x * (b + h + (b / 2)))) / h * a + b * x + b * x


    def set_cx(self):
        b, h, a, m = self.b, self.h, self.a, self.m
        x = a + m
        self.cx = (b * x * (x / 2) + h * a * (a / 2) + b * x * (x / 2)) / h * a + b * x + b * x


    def set_iz(self):
        b, h, a, m = self.b, self.h, self.a, self.m
        cy = self.cy
        x = a + m
        self.iz = (
                ((x * b ** 3 / 12) + (x * b * (cy - (b / 2)) ** 2))
                +
                ((a * h ** 3 / 12) + ((cy - ((h / 2) + b)) ** 2 * (a * h)))
                +
                ((x * b ** 3 / 12) + (x * b * (cy - ((b / 2) + h + b) ** 2)))
            )


    def set_iy(self):
        b, h, a, m = self.b, self.h, self.a, self.m
        cy = self.cy
        self.iy = 2 * (
                    (((b * (m + a) ** 3) / 12) + b * (m + a) * ((cy - ((m + a) / 2)) ** 2))
                    +
                    (h * a ** 3 / 12 + h * a * ((cy - (a / 2)) ** 2))
                )
                

    def set_scgz(self):
        b, h, a, m = self.b, self.h, self.a, self.m
        cy = self.cy
        if cy >= (2 * b + h):
            self.scgz = (2 * b + h - cy) * (a + m) * ((2 * b + h - cy) / 2)
        
        elif cy < (h + b):
            self.scgz = b * (a + m) * (cy - b / 2) + (cy - b) * a * ((cy - b) / 2)

        elif cy <= b:
            self.scgz = cy * (a + m) * (cy / 2)


    def set_kz(self):
        area, iz = self.area, self.iz
        self.kz = sqrt(iz / area)


    def set_ky(self):
        area, iy = self.area, self.iy
        self.ky = sqrt(iy / area)


    def get_fibra(self, length, position):
        pass

class ISection:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.letter = 'I'

        self.set_area()
        self.set_perimeter()
        self.set_cy()
        self.set_cx()
        self.set_iz()
        self.set_iy()
        self.set_scgz()
        self.set_scgy()
        self.set_kz()
        self.set_ky()


    def set_area(self):
        w, h = self.w, self.h
        self.area = w * h


    def set_perimeter(self):
        w, h = self.w, self.h
        self.perimeter = 2 * w + 2 * h

        
    def set_cy(self):
        h = self.h
        self.cy = h / 2


    def set_cx(self):
        w = self.w
        self.cx = w / 2


    def set_iz(self):
        w, h = self.w, self.h
        self.iz = (w * (h ** 3)) / 12


    def set_iy(self):
        w, h = self.w, self.h
        self.iy = (h * (w ** 3)) / 12
        

    def set_scgz(self):
        w = self.w
        cy = self.cy
        self.scgz = (w * cy * (cy / 2))


    def set_scgy(self):
        w, h = self.w, self.h
        self.scgy = h * ( w / 2 ) * ( w / 4 ) 


    def set_kz(self):
        area, iz = self.area, self.iz
        self.kz = sqrt(iz / area)


    def set_ky(self):
        area, iy = self.area, self.iy
        self.ky = sqrt(iy / area)
   

    def get_fibra(self, length, position=None):
        w, h = self.w, self.h
        cy = self.cy
        if length <= (h / 2):
            S = ((cy - length) * w) * (((cy - length) / 2) + length)

        else:
            S = -1

        return S

class HSection:
    def __init__(self, x, y, a, d, h, r):
        self.x = x
        self.y = y
        self.a = a
        self.d = d
        self.h = h
        self.r = r

        self.letter = 'H'

        self.set_area()
        self.set_perimeter()
        self.set_cy()
        self.set_cx()
        self.set_iz()
        self.set_iy()
        self.set_scgz()
        self.set_scgy()
        self.set_kz()
        self.set_ky()


    def set_area(self):
        x, y, h, a, d, r = self.x, self.y, self.h, self.a, self.d, self.r
        self.area = x * y + h * a + d * r


    def set_perimeter(self):
        x, y, h, a, d, r = self.x, self.y, self.h, self.a, self.d, self.r
        self.perimeter = 2 * d + 2 * y + r * x + 2 * h + (x - a) + (r * a)

        
    def set_cy(self):
        x, y, h, a, d, r = self.x, self.y, self.h, self.a, self.d, self.r
        self.cy = (
            ((a * r * (a / 2)) + (h * d * (a + (h / 2))) + (y * x * (a + h + (y / 2))))
            /
            ((a * r) + (d * h) + (y * x))
        )
        

    def set_cx(self):
        x, r = self.x, self.r
        if x >= r:
            self.cx = x / 2

        elif x < r:
            self.cx = r / 2


    def set_iz(self):
        x, y, h, a, d, r = self.x, self.y, self.h, self.a, self.d, self.r
        cy = self.cy
        self.iz = (
            (((r * (a ** 3)) / (12)) + ((a * r * (((cy - (a / 2)) ** 2)))))
            +
            (((d * (h ** 3)) / 12) + (h * d * ((((h / 2) + a) - cy) ** 2)))
            +
            (((x * (y ** 3)) / 12) + (y * x * (((a + h + (y / 2)) - cy) ** 2)))
        )


    def set_iy(self):
        x, y, h, a, d, r = self.x, self.y, self.h, self.a, self.d, self.r
        self.iy = (d * (r ** 3)) / 12 + ((h * (a ** 3)) / 12) + ((y * (x ** 3))/ 12)


    def set_scgz(self):
        x, y, h, a, d, r = self.x, self.y, self.h, self.a, self.d, self.r
        cy = self.cy
        if cy >= (y + h + d):
            self.scgz = (y + h + d - cy) * x * ((y + h + d - cy) / 2)
        
        elif cy < h + d:
            self.scgz = d * r * ((d / 2) + (cy - d)) + (cy - d) * a * ((cy - d) / 2)

        elif cy <= d:
            self.scgz = cy * r * (cy / 2)


    def set_scgy(self):
        x, y, h, a, d, r = self.x, self.y, self.h, self.a, self.d, self.r
        self.scgy = (r / 2) * d * (r / 4) + y * (x / 2) * (x / 4) + h * (a / 2) * (a / 4)


    def set_kz(self):
        area, iz = self.area, self.iz
        self.kz = sqrt(iz / area)


    def set_ky(self):
        area, iy = self.area, self.iy
        self.ky = sqrt(iy / area)


    def get_fibra(self, length, position):
        x, y, h, a, d, r = self.x, self.y, self.h, self.a, self.d, self.r
        cy = self.cy
        if ((position == 'up') and (cy + length <= y + d + h)) or ((position == 'down') and (cy - length >= 0)):
            if cy >= (h + d):
                if position == 'up':
                    if (cy + length) < (y + d + h):
                        i = ((cy + length) - (y + h + d))
                        S = i * x * ((i/2) + length)

                elif position == 'down':
                    if (cy - length) <= (d + h) and (cy - length) > d:
                        i = ( d + h) - (cy - length)
                        S = ((i * a * ((i / 2) + length)) + (d * r * ((d / 2) + i + length)))

                    elif (cy - length) <= d:
                        u = ( cy - length)  
                        S = u * r * ((u / 2) + length)

                    elif (cy - length) > (d + h):    
                        u = (cy - length) - (h + d)
                        S = (u * x * ((u / 2 ) + length)) + (h * a * ((h / 2) + u + length)) + d * r * ((d / 2) + h + u + length)

            elif (cy > d) and cy <= (d + h):     
                if position =='up':      
                    if (cy + length) >= (d + h):
                        i = ( d + h + y) - (cy + length)
                        S = i * x * ((i / 2) + length)
                    
                    elif (cy + length) <= ( d + h) and (cy + length) >= d:
                        i = (d + h) - (cy + length)
                        S = (y * x * ((y / 2) + i + length)) + (i * a * ((i / 2) + length))

                elif position == 'down':
                    if (cy - length) > d:
                        v = (d + h) - ( cy - length)    
                        S = (v * a * ((v / 2) + length)) + (d * r * ((d / 2) + length))

                    elif (cy - length) <= d: 
                        v = (cy - length)
                        S = v * r * ((v / 2) + length)

            elif ( cy <= d ):
                if position == 'down':
                    if ( cy - length) <= d:
                        g = (cy - length)
                        S = g * r * ((g / 2)+ length)

                elif position == 'up':
                    if (cy + length) >= (d + h):
                        i = (d + h + length) - (cy + length)
                        S = (i * x * ((i / 2)+ length))

                    elif (cy + length) >= d:
                        m = (h + d) - (cy + length)    
                        S = y * x * ((y / 2) + length)

                    elif (cy + length) < d:   
                        m = (d) - (cy + length)
                        S = (y * x * ((y / 2) + h + m + length)) + (h * a * ((h / 2) + m + length)) + (m * r * ((m / 2) + length)) 
            
        else:
            S = -1 # NÃO DEVE ACONTECER
        
        return S
