from abc import ABC, abstractmethod

#An Abstract class which will serve as base class for other Event classes.
class Event(ABC):
    def __init__(self, eventType):
        self.eventType= eventType
    
    @abstractmethod
    def getEventType(self):
        pass