import sys
sys.path.append("..")

from pynput import mouse
from Event.MouseEvent.MouseEventEnvelop import MouseEventEnvelop, CreateMouseEventEnvelop
from Event import EventDispatcher
from Event.EventTypes import EventType
from TimeOffset import TimeOffset
from datetime import datetime

#Global variable to pass information of whether the mouse is pressed or not.
isMousePressed= False
timeOffsetCalc= TimeOffset(datetime.now())

def OnClick(x, y, button, pressed):
    global isMousePressed
    
    #calculating waiting time
    currtime=datetime.now()
    waiting_time= timeOffsetCalc.calculate_time_offset(currtime)
    timeOffsetCalc.changeReferenceTime(currtime)

    #setting global mouse_pressed event
    isMousePressed= pressed

    #initializing mouse_event
    eventtype = None
    if(pressed == True):
        eventtype= EventType.eMousePressEvent
    elif(pressed == False):
        eventtype= EventType.eMouseReleaseEvent
    
    #creating event envelop
    event= CreateMouseEventEnvelop(x, y, eventtype, pressed, waiting_time, button)
    
    #Sending to Dispatcher
    EventDispatcher.MouseEventDispatcher.publishEvent(event)

def OnMove(x, y):
    global isMousePressed
    
    #initializing mouse event
    event_type= EventType.eMouseMoveEvent

    #calculating waiting time
    currtime=datetime.now()
    waiting_time=timeOffsetCalc.calculate_time_offset(currtime)
    timeOffsetCalc.changeReferenceTime(currtime)

    #creating event envelop
    event= CreateMouseEventEnvelop(x, y, event_type, isMousePressed, waiting_time, None) 
    
    #Sending to dispatcher
    EventDispatcher.MouseEventDispatcher.publishEvent(event)

