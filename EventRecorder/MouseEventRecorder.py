import sys
sys.path.append("..")

from Communicator.Communicator import Communicator
from Event.EventTypes import EventType

class MouseEventRecorder(Communicator):
    def __init__(self, mousePressAction, mouseMoveAction, mouseReleaseAction):
        self._mousePressEventAction= mousePressAction
        self._mouseMoveEventAction= mouseMoveAction
        self._mouseReleaseEventAction= mouseReleaseAction
    
    def subscribeEvent(self, eventtype, subcriber):
        pass #not implemented now

    def publishEvent(self, event):
        pass #not implemented now

    def receive(self, event):
        if(event.eventType == EventType.eMousePressEvent):
            self._mousePressEventAction.handleEvent(event)
        elif(event.eventType == EventType.eMouseMoveEvent or event.eventType == EventType.eMousePressedAndMoveEvent):
            self._mouseMoveEventAction.handleEvent(event)
        elif(event.eventType == EventType.eMouseReleaseEvent):
            self._mouseReleaseEventAction.handleEvent(event)
        else:
            pass