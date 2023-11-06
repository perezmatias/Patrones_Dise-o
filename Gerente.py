from IAprobador import IAprobador

class Gerente(IAprobador):
    def __init__(self):
        self.next = None

    def set_next(self, aprobador):
        self.next = aprobador

    def get_next(self):
        return self.next

    def solicitud_prestamo(self, monto):
        if 50000 < monto <= 100000:
            print("Lo manejo yo, el gerente!")
        else:
            self.next.solicitud_prestamo(monto)