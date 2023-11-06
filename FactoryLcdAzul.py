from TvAbstractFactory import TvAbstractFactory
from Azul import Azul
from LCD import LCD

class FactoryLcdAzul(TvAbstractFactory):
    def create_color(self):
        return Azul()

    def create_tv(self):
        return LCD()
