from ..Event import Event

#Envleop Contains Information about Mouse Event.
class MouseEventEnvelop(Event):
    def __init__(self):
        self.x= None
        self.y= None
        self.button= None
        self.pressed= None
        self.waitingTime= 0
        
    def setWaitingTime(self, val):

        self.waitingTime= val
    
    def setX(self, val):
        self.x= val
    

    def setY(self, val):
        self.y= val

    def setPressed(self, val):
        self.pressed= val

    def setButton(self, val):
        self.button= val


    def setEventType(self, eventType):
        self.eventType= eventType

    def getEventType(self):
        return self.eventType
    
    def isPressed(self):
        return self.pressed

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWaitingTime(self):
        return self.waitingTime

    def getButton(self):
        return self.button

def CreateMouseEventEnvelop(x, y, eventtype, ispressed, waitingtime, button):
    envelop= MouseEventEnvelop()

    envelop.setX(x)
    envelop.setY(y)
    envelop.setEventType(eventtype)
    envelop.setPressed(ispressed)
    envelop.setButton(button)
    envelop.setWaitingTime(waitingtime)

    return envelop