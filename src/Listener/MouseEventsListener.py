from pynput import mouse
from src.Event.Event import Event
from ..Event.MouseEvent.MouseEventEnvelop import MouseEventEnvelop
from ..Event.EventDispatcher import EventsDispatcher
from ..Event.EventTypes import EventType
from .EventsListener import EventsListener
from ..DesignPatterns.SingletonMeta import singleton
from ..TimeOffset import TimeOffsetCalculator
from datetime import datetime
from ..EventRecorder.EventRecorderManager import EventRecorderController

@singleton
class MouseEventsListener(EventsListener):
        
    def __init__(self, dispatcher):
        EventsListener.__init__(self, dispatcher)
        self._listener= mouse.Listener(on_move= self.onMove, on_click= self.onClick)
        self.isMousePressed= False

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

        #calculating waiting time
        currtime=datetime.now()
        waiting_time= TimeOffsetCalculator.calculate_time_offset(currtime)
        TimeOffsetCalculator.changeReferenceTime(currtime)

        #setting global mouse_pressed event
        self.isMousePressed=pressed

        #initializing mouse_event
        eventtype = None
        if(pressed == True):
            eventtype= EventType.eMousePressEvent
        elif(pressed == False):
            eventtype= EventType.eMouseReleaseEvent
    
        #creating event envelop
        uuid= EventRecorderController.GetCurrentEventRecordingDocumentId()
        event= MouseEventEnvelop(uuid, x, y, eventtype, pressed, waiting_time, button)
    
        #print(f"onClick: {event.to_dict()}")
        self.notify(event)

    def onMove(self, x, y):
        #initializing mouse event
        event_type= EventType.eMouseMoveEvent

        #calculating waiting time
        currtime=datetime.now()
        waiting_time= TimeOffsetCalculator.calculate_time_offset(currtime)
        TimeOffsetCalculator.changeReferenceTime(currtime)

        #creating event envelop
        uuid= EventRecorderController.GetCurrentEventRecordingDocumentId() 
        event= MouseEventEnvelop(uuid, x, y, event_type, self.isMousePressed, waiting_time, None)
        
        #print(f"onMove: {event.to_dict()}")
        self.notify(event)

#Listener which will capture the Mouse events
MouseListenerController=  MouseEventsListener(EventsDispatcher)
