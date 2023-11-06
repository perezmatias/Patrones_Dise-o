from IAprobador import IAprobador

class Director(IAprobador):
    def __init__(self):
        self.next = None

    def set_next(self, aprobador):
        self.next = aprobador

    def get_next(self):
        return self.next

    def solicitud_prestamo(self, monto):
        if monto > 100000:
            print("Lo manejo yo, el director!")
