from Command import Command

class PrenderServer(Command):
    def __init__(self, servidor):
        self.servidor = servidor

    def execute(self):
        self.servidor.prendete()
        self.servidor.conectate()
        self.servidor.verificaConexion()
        self.servidor.guardaLog()
        self.servidor.cerraConexion()
