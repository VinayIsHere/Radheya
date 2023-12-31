from abc import ABC, abstractmethod

EVENT_SEQUENCE_NO= "EventSequenceNumber"
META_KEY= "meta"

class Storage(ABC):
    def __init__(self, dataSource):
        self._currentActiveStorageFile= None
        self._data= dataSource # _data could be json, xml or .db file
        
    #Write the event into _data.
    @abstractmethod
    def WriteEvent(self, event):
        pass

    #Read Stored Events From the _data.
    @abstractmethod
    def Read(self):
        pass
