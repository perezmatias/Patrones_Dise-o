from IAprobador import IAprobador
from EjecutivoDeCuenta import EjecutivoDeCuenta
from LiderTeamEjecutivo import LiderTeamEjecutivo
from Gerente import Gerente
from Director import Director


class Banco(IAprobador):
    def __init__(self):
        self.next = None

    def set_next(self, aprobador):
        self.next = aprobador

    def get_next(self):
        return self.next

    def solicitud_prestamo(self, monto):
        ejecutivo = EjecutivoDeCuenta()
        self.set_next(ejecutivo)
        lider = LiderTeamEjecutivo()
        ejecutivo.set_next(lider)
        gerente = Gerente()
        lider.set_next(gerente)
        director = Director()
        gerente.set_next(director)
        self.next.solicitud_prestamo(monto)
