from abc import ABC, abstractmethod

class TrianguloFactoryMethod(ABC):
    @abstractmethod
    def create_triangulo(self, ladoA, ladoB, ladoC):
        pass
