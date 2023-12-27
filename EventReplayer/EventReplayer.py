import sys
sys.path.append("..")

from Communicator.Communicator import Communicator
from Event.EventTypes import EventType

class EventReplayer(Communicator):
    def __init__(self, mouseReplayer):
        Communicator.__init__(self)
        self._mouseReplayer= mouseReplayer

    def subscribeEvent(self, eventtype, subcriber):
        print("event replayer subscribe event")

    def publishEvent(self, event):
        print("replayer publish event")

    def receive(self, event):
        if(self.isMouseEvent(event.getEventType())):
            self._mouseReplayer.receive(event)

    def isMouseEvent(self, eventType):
        if(eventType == EventType.eMousePressEvent or
           eventType == EventType.eMouseReleaseEvent or
           eventType == EventType.eMouseMoveEvent or
           eventType == EventType.eMousePressedAndMoveEvent):
            return True

        return False
