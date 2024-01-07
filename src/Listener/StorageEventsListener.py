from ..DesignPatterns.SingletonMeta import singleton
from .EventsListener import EventsListener

@singleton
class StorageEventsListener(EventsListener):

    def __init__(self, dispatcher):
        EventsListener.__init__(self, dispatcher)        

    def start():
        pass

    def stop():
        pass

    def restart():
        pass
    
    def notify(self, event):
        self._dispatcher.publishEvent(event)

    def onSave(filepath, saveOrNot):
        pass