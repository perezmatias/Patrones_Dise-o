from Auto import Auto
from abc import ABC, abstractmethod

class AutoBuilder(ABC):
    def __init__(self):
        self.auto = None

    def get_auto(self):
        return self.auto

    def crear_auto(self):
        self.auto = Auto()

    @abstractmethod
    def build_motor(self):
        pass

    @abstractmethod
    def build_modelo(self):
        pass

    @abstractmethod
    def build_marca(self):
        pass

    @abstractmethod
    def build_puertas(self):
        pass
