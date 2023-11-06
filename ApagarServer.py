from Command import Command

class ApagarServer(Command):
    def __init__(self, servidor):
        self.servidor = servidor

    def execute(self):
        self.servidor.conectate()
        self.servidor.verificaConexion()
        self.servidor.guardaLog()
        self.servidor.cerraConexion()
        self.servidor.apagate()