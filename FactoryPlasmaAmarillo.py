from TvAbstractFactory import TvAbstractFactory
from Amarillo import Amarillo
from Plasma import Plasma

class FactoryPlasmaAmarillo(TvAbstractFactory):
    def create_color(self):
        return Amarillo()

    def create_tv(self):
        return Plasma()
