from pynput import mouse
from ..Event.MouseEvent.MouseEventEnvelop import MouseEventEnvelop
from ..Event.EventDispatcher import EventsDispatcher
from ..Event.EventTypes import EventType
from .EventsListener import EventsListener
from ..DesignPatterns.SingletonMeta import singleton
from ..TimeOffset import TimeOffset
from datetime import datetime

@singleton
class MouseEventsListener(EventsListener):
        
    def __init__(self, dispatcher):
        EventsListener.__init__(self, dispatcher)
        self._listener= mouse.Listener(on_move= self.onMove, on_click= self.onClick)
        self.isMousePressed= False
        self.timeoffsetCalculator= TimeOffset(datetime.now())

    def start(self):
        self._listener.start()

    def stop(self):
        self._listener.stop()

    def restart(self):
        self._listener= mouse.Listener(on_move= self.onMove, on_click= self.onClick)
        self.start()

    def notify(self, event):
        self._dispatcher.publishEvent(event)

    def onClick(self, x, y, button, pressed):
        #print(f"onClick: x:{x}, y:{y}, button:{button}, pressed:{pressed}")

        #calculating waiting time
        currtime=datetime.now()
        waiting_time= self.timeoffsetCalculator.calculate_time_offset(currtime)
        self.timeoffsetCalculator.changeReferenceTime(currtime)

        #setting global mouse_pressed event
        self.isMousePressed=pressed

        #initializing mouse_event
        eventtype = None
        if(pressed == True):
            eventtype= EventType.eMousePressEvent
        elif(pressed == False):
            eventtype= EventType.eMouseReleaseEvent
    
        #creating event envelop
        event= MouseEventEnvelop(x, y, eventtype, pressed, waiting_time, button)
    
        self.notify(event)

    def onMove(self, x, y):
        #print(f"onMove: x:{x}, y:{y}")

        #initializing mouse event
        event_type= EventType.eMouseMoveEvent

        #calculating waiting time
        currtime=datetime.now()
        waiting_time=self.timeoffsetCalculator.calculate_time_offset(currtime)
        self.timeoffsetCalculator.changeReferenceTime(currtime)

        #creating event envelop
        event= MouseEventEnvelop(x, y, event_type, self.isMousePressed, waiting_time, None)
        
        self.notify(event)

#Listener which will capture the Mouse events
MouseListenerController=  MouseEventsListener(EventsDispatcher)
