from abc import ABC, abstractmethod

class EventsListener(ABC):
    def __init__(self, dispatcher):
        self._dispatcher= dispatcher

    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass

    @abstractmethod
    def restart():
        pass
    
    @abstractmethod
    def notify():
        pass