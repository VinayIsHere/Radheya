from abc import ABC, abstractmethod

class Communicator(ABC):

    def __init__(self):
        self.subscribers= dict()
    
    @abstractmethod
    def subscribeEvent(self, eventtype, subcriber):
        pass

    @abstractmethod
    def publishEvent(self, event):
        pass

    @abstractmethod
    def receive(self, event):
        pass
