from ILibroMalEstado import ILibroMalEstado
from Subject import Subjet

class AlarmaLibro(Subjet):

    def __init__(self):
        self.observadores = []

    def attach(self, observador: ILibroMalEstado):
        self.observadores.append(observador)

    def detach(self, observador: ILibroMalEstado):
        self.observadores.remove(observador)

    def notify_observer(self):
        for observer in self.observadores:
            observer.update()
