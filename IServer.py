from abc import ABC, abstractmethod

class IServer(ABC):
    @abstractmethod
    def apagate(self):
        pass

    @abstractmethod
    def prendete(self):
        pass

    @abstractmethod
    def conectate(self):
        pass

    @abstractmethod
    def verificaConexion(self):
        pass

    @abstractmethod
    def guardaLog(self):
        pass

    @abstractmethod
    def cerraConexion(self):
        pass
