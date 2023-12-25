import sys
sys.path.append("..")

from Communicator.Communicator import Communicator
from Event.EventDispatcher import MouseEventDispatcher
from Event.EventTypes import EventType

class AutomationRecorder(Communicator):
    def __init__(self, mouseRecorder):
        self.MouseEventRecorder= mouseRecorder
    
    def subscribeEvent(self, eventtype, subcriber):
        print("inside subscrive event")

    def publishEvent(self, event):
        print("inside publish event")

    def isMouseEvent(self, eventType):
        if(eventType == EventType.eMousePressEvent or
           eventType == EventType.eMouseReleaseEvent or
           eventType == EventType.eMouseMoveEvent or
           eventType == EventType.eMousePressedAndMoveEvent):
            return True

        return False

    def receive(self, event):
        if(self.isMouseEvent(event.eventType)):
            #print("eventttype:", event.eventType)
            self.MouseEventRecorder.receive(event)
        else:
            pass