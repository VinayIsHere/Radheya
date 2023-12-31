from ..Event import Event
from ..EventTypes import EventType
from pynput.mouse import Button

#Envleop Contains Information about Mouse Event.
class MouseEventEnvelop(Event):
    def __init__(self, uuid, x, y, eventtype, pressed, waitingtime, button=None):
        Event.__init__(self, eventtype, uuid)
        self.x= x
        self.y= y
        self.button= button
        self.pressed= pressed
        self.waitingTime= waitingtime
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getButton(self):
        return self.button

    def isPressed(self):
        return self.pressed

    def getCordinate(self):
        return self.x, self.y

    def getWaitingTime(self):
        return self.waitingTime

    def getEventType(self):
        return self.eventType

    def setWaitingTime(self, waitingtime):
        self.waitingTime= waitingtime
    
    def getParentUuid(self):
        return self.parentuuid

    def to_dict(self):
        attrs = dict(
            (attr, getattr(self, attr)) for attr in ['parentuuid', 'x', 'y', 'eventType', 'waitingTime', 'pressed']
        )

        #Button is a special case
        if(self.button != None):
            attrs['button']= self.button.value
        else:
            attrs['button']= "None"

        return attrs

#Helper Functions
def convertDictToMouseEventEnvelop(dictEvent): 
    meta= dictEvent.get("meta")

    uuid= meta["parentuuid"]
    eventType= EventType(meta["eventType"])

    #Parsing Mouse Meta Information
    button= None
    if(meta.get("button") != "None"):
        button= Button(tuple(meta.get("button")))
       
    x= int(meta.get("x"))
    y= int(meta.get("y"))
    ispressed= int(meta.get("pressed"))
    waitingtime= int(meta.get("waitingTime"))

    mouseEventEnvelop= MouseEventEnvelop(uuid, x, y, eventType, ispressed, waitingtime, button)

    return mouseEventEnvelop