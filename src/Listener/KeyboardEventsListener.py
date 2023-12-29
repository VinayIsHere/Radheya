import keyboard
from datetime import datetime
from ..DesignPatterns.SingletonMeta import singleton
from ..TimeOffset import TimeOffset
from .EventsListener import EventsListener
from ..Event.EventDispatcher import EventsDispatcher
from ..Event.EventTypes import EventType

WAIT_KEY= 'esc'

@singleton
class KeyboardEventsListener(EventsListener):
    
    def __init__(self, dispatcher):
        EventsListener.__init__(self, dispatcher)
        self.timeOffsetCalculator= TimeOffset(datetime.now())
        
    def start(self):
        keyboard.hook(self.keyEventCallback)
        keyboard.wait(WAIT_KEY) #keyboard event listening will stop when WAIT_KEY is pressed.
        
    def restart():
        pass #not implemented for keyboard.

    def stop():
        keyboard.unhook()
    
    def notify(self, event):
        self._dispatcher.publishEvent(event)
        
    def keyEventCallback(self, event):

        #calculating waiting time
        currtime= datetime.now()
        waiting_time= self.timeOffsetCalculator.calculate_time_offset(currtime)
        self.timeOffsetCalculator.changeReferenceTime(currtime)

        eventtype= None
        #initializing keyboard event
        if(event.event_type == keyboard.KEY_UP):
            eventtype= EventType.eKeyboardUpEvent
        elif(event.event_type == keyboard.KEY_DOWN):
            eventtype= EventType.eKeyboardDownEvent
        
            
        self.notify(event)

#Listener which will capture the Mouse events
KeyboardListenerController=  KeyboardEventsListener(EventsDispatcher)
