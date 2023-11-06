from FactoryLcdAzul import FactoryLcdAzul
from FactoryPlasmaAmarillo import FactoryPlasmaAmarillo
from EnsamblajeTv import EnsamblajeTv

def main():
    fabrica1 = FactoryLcdAzul()
    ensamble1 = EnsamblajeTv(fabrica1)

    fabrica2 = FactoryPlasmaAmarillo()
    ensamble2 = EnsamblajeTv(fabrica2)

if __name__ == "__main__":
    main()
