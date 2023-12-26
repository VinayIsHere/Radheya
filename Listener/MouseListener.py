import sys
sys.path.append("..")

from pynput import mouse
from Event.MouseEvent.MouseEventEnvelop import MouseEventEnvelop
from Event import EventDispatcher
from Event.EventTypes import EventType
from TimeOffset import TimeOffset
from datetime import datetime

#Global variable to pass information of whether the mouse is pressed or not.
isMousePressed= False
timeOffsetCalc= TimeOffset(datetime.now())

def OnClick(x, y, button, pressed):
    global isMousePressed
    
    #Preparing Event
    event= MouseEventEnvelop()
    event.setX(x)
    event.setY(y)
    event.setPressed(pressed)
    event.setButton(button)

    currtime=datetime.now()
    event.setWaitingTime(timeOffsetCalc.calculate_time_offset(currtime))
    timeOffsetCalc.changeReferenceTime(currtime)

    isMousePressed= pressed

    if(pressed == True):
        event.setEventType(EventType.eMousePressEvent)
    elif(pressed == False):
        event.setEventType(EventType.eMouseReleaseEvent)
        
    #Sending to Dispatcher
    EventDispatcher.MouseEventDispatcher.publishEvent(event)

def OnMove(x, y):
    global isMousePressed

    #Preparing Event
    event= MouseEventEnvelop()
    event.setX(x)
    event.setY(y)
    event.setEventType(EventType.eMouseMoveEvent)
    event.setPressed(isMousePressed)

    currtime=datetime.now()
    event.setWaitingTime(timeOffsetCalc.calculate_time_offset(currtime))
    timeOffsetCalc.changeReferenceTime(currtime)

    #Sending to dispatcher
    EventDispatcher.MouseEventDispatcher.publishEvent(event)

