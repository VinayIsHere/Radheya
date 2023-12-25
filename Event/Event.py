from abc import ABC, abstractmethod

#An Abstract class which will serve as base class for other Event classes.
class Event(ABC):
    def __init__(self):
        self.eventType= None
    
    @abstractmethod
    def setEventType(self, eventType):
        pass

    @abstractmethod
    def getEventType(self):
        pass