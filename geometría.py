import math as m

class Punto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def constructor(self):
        return [self.x, self.y]

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "El punto ({}, {}) se localiza en el primer cuadrante".format(self.x, self.y)
        elif self.x < 0 and self.y > 0:
            return "El punto ({}, {}) se localiza en el segundo cuadrante".format(self.x, self.y)
        elif self.x < 0 and self.y < 0:
            return "El punto ({}, {}) se localiza en el tercer cuadrante".format(self.x, self.y)
        elif self.x > 0 and self.y < 0:
            return "El punto ({}, {}) se localiza en el cuarto cuadrante".format(self.x, self.y)
        elif self.x == 0 and self.y == 0:
            return "El punto ({}, {}) se localiza en el origen".format(self.x, self.y)
        elif self.x == 0 and self.y != 0:
            return "El punto ({}, {}) se localiza en el eje Y".format(self.x, self.y)   
        elif self.x != 0 and self.y == 0:  
            return "El punto ({}, {}) se localiza en el eje X".format(self.x, self.y)

    def string(self):
        print("({}, {})".format(self.x, self.y))
    
    def vector(self, punto):
        return [punto.x - self.x, punto.y - self.y]
    
    def distancia(self, punto):
        v = self.vector(punto)
        return m.sqrt(v[0]**2 + v[1]**2)

class Rectangulo:

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def constructor(self):
        A = [self.a, self.b]
        B = [self.c, self.b]
        C = [self.c, self.d]
        D = [self.a, self.d]
        return A, B, C, D
    
    def base(self):
        A, B, _, _ = self.constructor()
        p1 = Punto(A[0], A[1])
        p2 = Punto(B[0], A[1])
        v1 = p1.vector(p2)
        dist1 = p1.distancia(p2)
        return A, B, v1, dist1
    
    def altura(self):
        A, _, _, D = self.constructor()
        p1 = Punto(A[0], A[1])
        p2 = Punto(A[0], D[1])
        v1 = p1.vector(p2)
        dist1 = p1.distancia(p2)
        return A, D, v1, dist1
    
    def area(self):
        _, _, _, dist1 = self.base()
        _, _, _, dist2 = self.altura()
        return dist1 * dist2
    
    def __str__(self):
        return "Rectangulo: A = ({}, {}), B = ({}, {}), C = ({}, {}), D = ({}, {}), base: {}, altura: {}, area: {}".format(self.a, self.b, self.c, self.b, self.c, self.d, self.a, self.d, self.base(), self.altura(), self.area())