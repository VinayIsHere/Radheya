from ..Communicator.Communicator import Communicator
from ..Event.EventTypes import EventType

class AutomationRecorder(Communicator):
    def __init__(self, mouseRecorder, keyboardRecorder):
        Communicator.__init__(self)
        self.MouseEventRecorder= mouseRecorder
        self.KeyboardEventRecorder= keyboardRecorder
    
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

    def isKeyboardEvent(self, eventType):
        if(eventType in [
                EventType.eKeyboardUpEvent,
                EventType.eKeyboardDownEvent
            ]):
            return True

        return False

    def receive(self, event):
        if(self.isMouseEvent(event.eventType)):
            #print("eventttype:", event.eventType)
            self.MouseEventRecorder.receive(event)
        elif(self.isKeyboardEvent(event.eventType)):
            print(f"eventtype: {event.eventType}")
            self.KeyboardEventRecorder.receive(event)