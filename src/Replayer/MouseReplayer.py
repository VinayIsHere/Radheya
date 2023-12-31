from pynput import mouse
from pynput.mouse import Button, Controller
import time

MouseController= Controller()
LastMouseEventPosition= tuple([0, 0])

class MouseReplayer:
    def __init__(self):
        #will be used to control waiting time of first event, which should be 0.
        self.firstEvent= False

    def replayMoveEvent(self, event):
        
        if(self.firstEvent == False):
            event.setWaitingTime(0)
            self.firstEvent= True

        ReplayMouseMoveEvent(event)

    def replayPressEvent(self, event):
        
        if(self.firstEvent == False):
            event.setWaitingTime(0)
            self.firstEvent= True

        ReplayMousePressEvent(event)

    def replayReleaseEvent(self, event):

        if(self.firstEvent == False):
            event.setWaitingTime(0)
            self.firstEvent= True
            
        ReplayMouseReleaseEvent(event)

def ReplayMousePressEvent(event):
    global LastMouseEventPosition
    global MouseController
    
    print(f"mousePressEvent: eventDetails: {event.to_dict()}")
    
    #delay before performing the action
    time.sleep((event.getWaitingTime()*0.001)) #converting to seconds

    #Set Mouse Position and update Last position
    MouseController.position= (event.getX(), event.getY())
    LastMouseEventPosition= MouseController.position

    #Simulate Press Event
    MouseController.press(event.getButton())
    
def ReplayMouseMoveEvent(event):
    global LastMouseEventPosition
    global MouseController

    #print(f"mouseMoveEvent: eventDetails: {event.to_dict()}")
    
    #delay before performing the action
    time.sleep((event.getWaitingTime()*0.001)) #converting to seconds

    #calculating offset from the last position
    offsetPosition= tuple([event.getX()-LastMouseEventPosition[0], event.getY()-LastMouseEventPosition[1]])
    
    #Simulate Move Event
    MouseController.move(offsetPosition[0], offsetPosition[1])
    LastMouseEventPosition= MouseController.position
    #print(LastMouseEventPosition)
    
def ReplayMouseReleaseEvent(event):
    global MouseController
    global LastMouseEventPosition

    #print(f"mouseReleaseEvent: eventDetails: {event.to_dict()}")
    
    time.sleep((event.getWaitingTime()*0.001)) #converting to seconds

    MouseController.position= (event.getX(), event.getY())
    LastMouseEventPosition= MouseController.position

    MouseController.release(event.getButton())