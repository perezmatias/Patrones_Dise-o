from Triangulo import Triangulo
from TrianguloFactoryMethod import TrianguloFactoryMethod
from Equilatero import Equilatero
from Escaleno import Escaleno
from Isosceles import Isosceles

class TrianguloFactory(TrianguloFactoryMethod):
    def create_triangulo(self, ladoA, ladoB, ladoC):
        if ladoA == ladoB and ladoA == ladoC:
            return Equilatero(ladoA, ladoB, ladoC)
        elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
            return Escaleno(ladoA, ladoB, ladoC)
        else:
            return Isosceles(ladoA, ladoB, ladoC)
