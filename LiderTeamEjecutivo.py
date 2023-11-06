from IAprobador import IAprobador

class LiderTeamEjecutivo(IAprobador):
    def __init__(self):
        self.next = None

    def set_next(self, aprobador):
        self.next = aprobador

    def get_next(self):
        return self.next

    def solicitud_prestamo(self, monto):
        if 10000 < monto <= 50000:
            print("Lo manejo yo el lider!")
        else:
            self.next.solicitud_prestamo(monto)
