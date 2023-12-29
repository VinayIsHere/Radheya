from ..Communicator.Communicator import Communicator
from ..Event.EventTypes import EventType

class KeyboardEventRecorder(Communicator):
    def __init__(self, keyboardUpAction, keyboardDownAction):
        self._keyboardUpAction= keyboardUpAction
        self._keyboardDownAction= keyboardDownAction
    
    def subscribeEvent(self, eventtype, subcriber):
        pass #not implemented now

    def publishEvent(self, event):
        pass #not implemented now

    def receive(self, event):
        if(event.eventType == EventType.eKeyboardUpEvent):
            self._keyboardUpAction.handleEvent(event)
        elif(event.eventType == EventType.eKeyboardDownEvent):
            self._keyboardDownAction.handleEvent(event)
        else:
            pass