from AutoBuilder import AutoBuilder
from Motor import Motor

class MitsubishiBuilder(AutoBuilder):
    def build_marca(self):
        self.auto.set_marca("Mitsubishi")
    
    def build_modelo(self):
        self.auto.set_modelo("Lancer Evolution X")
    
    def build_motor(self):
        motor = Motor()
        motor.set_numero(232323)
        motor.set_potencia("280 hp")
        self.auto.set_motor(motor)
    
    def build_puertas(self):
        self.auto.set_cantidad_de_puertas(2)
