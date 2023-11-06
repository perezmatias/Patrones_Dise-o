from abc import ABC, abstractmethod

class Triangulo(ABC):
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    @property
    def lado_a(self):
        return self.ladoA

    @lado_a.setter
    def lado_a(self, ladoA):
        self.ladoA = ladoA

    @property
    def lado_b(self):
        return self.ladoB

    @lado_b.setter
    def lado_b(self, ladoB):
        self.ladoB = ladoB

    @property
    def lado_c(self):
        return self.ladoC

    @lado_c.setter
    def lado_c(self, ladoC):
        self.ladoC = ladoC

    @abstractmethod
    def get_descripcion(self):
        pass

    @abstractmethod
    def get_superficie(self, base, altura):
        pass

    @abstractmethod
    def dibujate(self):
        pass
