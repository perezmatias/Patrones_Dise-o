from IAprobador import IAprobador

class EjecutivoDeCuenta(IAprobador):
    def __init__(self):
        self.next = None

    def set_next(self, aprobador):
        self.next = aprobador

    def get_next(self):
        return self.next

    def solicitud_prestamo(self, monto):
        if monto <= 10000:
            print("Lo manejo yo, el Ejecutivo de Cuentas")
        else:
            self.next.solicitud_prestamo(monto)
