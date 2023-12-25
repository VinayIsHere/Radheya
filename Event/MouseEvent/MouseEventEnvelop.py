from ..Event import Event

#Envleop Contains Information about Mouse Event.
class MouseEventEnvelop(Event):
    def __init__(self):
        self.x= None
        self.y= None
        self.button= None
        self.pressed= None
        self.waitingTime= 0
        #self.waitingTime= None
        #self.doubleClick= None
        #self.pressed= None
        #self.released= None
        #self.moving= None

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

    #def setDoubleClickEvent(self, val):
    #    self.doubleClick= val

    #def setPressedEvent(self, val):
    #    self.pressed= val

    #def setReleaseEvent(self, val):
    #    self.release= val

    #def setMovingElement(self, val):
    #    self.moving= val