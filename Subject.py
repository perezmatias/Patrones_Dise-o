from abc import ABC, abstractmethod

class Subjet(ABC):

    @abstractmethod
    def attach(self, observador):
        pass

    @abstractmethod
    def detach(self, observador):
        pass

    @abstractmethod
    def notify_observer(self):
        pass
