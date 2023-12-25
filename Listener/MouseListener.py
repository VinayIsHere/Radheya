import sys
sys.path.append("..")

from pynput import mouse
from Event.MouseEvent.MouseEventEnvelop import MouseEventEnvelop
from Event import EventDispatcher
from Event.EventTypes import EventType

#Global variable to pass information of whether the mouse is pressed or not.
isMousePressed= False

def OnClick(x, y, button, pressed):
    global isMousePressed
    
    #Preparing Event
    event= MouseEventEnvelop()
    event.setX(x)
    event.setY(y)
    event.setPressed(pressed)
    event.setButton(button)

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

    #Sending to dispatcher
    EventDispatcher.MouseEventDispatcher.publishEvent(event)

