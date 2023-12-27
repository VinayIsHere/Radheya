import sys
sys.path.append("..")

from Communicator.Communicator import Communicator
from Event.EventTypes import EventType

class MouseEventReplayer(Communicator):
    def __init__(self, mousePressAction, mouseMoveAction, mouseReleaseAction):
        Communicator.__init__(self)
        self._mousePressAction= mousePressAction
        self._mouseMoveAction= mouseMoveAction
        self._mouseReleaseAction= mouseReleaseAction

    def subscribeEvent(self, eventtype, subcriber):
        pass #not implemented now

    def publishEvent(self, event):
        pass #not implemented now

    def receive(self, event):
        if(event.eventType == EventType.eMousePressEvent):
            self._mousePressAction.handleEvent(event)
        elif(event.eventType == EventType.eMouseMoveEvent or event.eventType == EventType.eMousePressedAndMoveEvent):
            self._mouseMoveAction.handleEvent(event)
        elif(event.eventType == EventType.eMouseReleaseEvent):
            self._mouseReleaseAction.handleEvent(event)
        else:
            pass