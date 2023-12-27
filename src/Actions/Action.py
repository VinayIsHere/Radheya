from abc import ABC, abstractmethod

class Action(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def handleEvent(self, event):
        pass

    @abstractmethod
    def replayAction(self, event):
        pass

    @abstractmethod
    def WriteAction(self):
        pass
    
    @abstractmethod
    def ReadAction(self):
        pass