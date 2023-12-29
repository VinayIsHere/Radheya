import keyboard
from datetime import datetime
from ..DesignPatterns.SingletonMeta import singleton
from ..TimeOffset import TimeOffsetCalculator
from .EventsListener import EventsListener
from ..Event.EventDispatcher import EventsDispatcher
from ..Event.EventTypes import EventType
from ..Event.KeyboardEvent.KeyboardEventEnvelop import KeyboardEventEnvelop

WAIT_KEY= 'esc'

@singleton
class KeyboardEventsListener(EventsListener):
    
    def __init__(self, dispatcher):
        EventsListener.__init__(self, dispatcher)
        
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
        waiting_time= TimeOffsetCalculator.calculate_time_offset(currtime)
        TimeOffsetCalculator.changeReferenceTime(currtime)

        eventtype= None
        #initializing keyboard event
        if(event.event_type == keyboard.KEY_UP):
            eventtype= EventType.eKeyboardUpEvent
        elif(event.event_type == keyboard.KEY_DOWN):
            eventtype= EventType.eKeyboardDownEvent
        
        eventEnvelop= KeyboardEventEnvelop(event.name, eventtype, event.scan_code, waiting_time, event.time, event.device, event.is_keypad, event.modifiers)

        print(f"keyboardevent:", eventEnvelop.to_dict())
        self.notify(eventEnvelop)

#Listener which will capture the Mouse events
KeyboardListenerController=  KeyboardEventsListener(EventsDispatcher)
