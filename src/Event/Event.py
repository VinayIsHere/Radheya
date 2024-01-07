from abc import ABC, abstractmethod

#An Abstract class which will serve as base class for other Event classes.
class Event(ABC):
    def __init__(self, eventType, uuid):
        self.eventType= eventType
        self.parentuuid= uuid
    
    @abstractmethod
    def getEventType(self):
        pass

    @abstractmethod
    def getParentUuid(self):
        pass