import sys 
sys.path.insert(0, "")
import unittest
from geometría import Punto, Rectangulo

class TestGeometría(unittest.TestCase):

    def test_constructor(self):
        p1 = Punto(2, 3)
        p2 = Punto(-3, -1)
        p3 = Punto(0, 0)
        self.assertEqual(p1.constructor(), [2, 3])
        self.assertEqual(p2.constructor(), [-3, -1])
        self.assertEqual(p3.constructor(), [0, 0])

    def test_cuadrante(self):
        p1 = Punto(2, 3)
        p2 = Punto(-3, -1)
        p3 = Punto(0, 0)
        p4 = Punto(0, 2)
        p5 = Punto(2, 0)
        self.assertEqual(p1.cuadrante(), "El punto (2, 3) se localiza en el primer cuadrante")
        self.assertEqual(p2.cuadrante(), "El punto (-3, -1) se localiza en el tercer cuadrante")
        self.assertEqual(p3.cuadrante(), "El punto (0, 0) se localiza en el origen")
        self.assertEqual(p4.cuadrante(), "El punto (0, 2) se localiza en el eje Y")
        self.assertEqual(p5.cuadrante(), "El punto (2, 0) se localiza en el eje X")

    def test_vector(self):
        p1 = Punto(2, 3)
        p2 = Punto(-3, -1)
        p3 = Punto(0, 0)
        self.assertEqual(p1.vector(p2), [-5, -4])
        self.assertEqual(p2.vector(p1), [5, 4])
        self.assertEqual(p3.vector(p1), [2, 3])
        self.assertEqual(p3.vector(p2), [-3, -1])

    def test_distancia(self):
        p1 = Punto(4, 0)
        p2 = Punto(0, 3)
        p3 = Punto()
        self.assertEqual(p1.distancia(p3), 4)
        self.assertEqual(p2.distancia(p3), 3)
        self.assertEqual(p1.distancia(p2), 5)

    def test_constructor_rectangulo(self):
        r1 = Rectangulo(0, 0, 2, 3)
        r2 = Rectangulo(0, 0, -2, -3)
        r3 = Rectangulo(0, 0, 0, 0)
        self.assertEqual(r1.constructor(), ([0, 0], [2, 0], [2, 3], [0, 3]))
        self.assertEqual(r2.constructor(), ([0, 0], [-2, 0], [-2, -3], [0, -3]))
        self.assertEqual(r3.constructor(), ([0, 0], [0, 0], [0, 0], [0, 0]))

    def test_base(self):
        r1 = Rectangulo(0, 0, 2, 3)
        r2 = Rectangulo(0, 0, -2, -3)
        r3 = Rectangulo(0, 0, 0, 0)
        self.assertEqual(r1.base(), 2)
        self.assertEqual(r2.base(), -2)
        self.assertEqual(r3.base(), 0)