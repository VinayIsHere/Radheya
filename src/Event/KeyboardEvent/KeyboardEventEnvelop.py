from ..Event import Event
from ..EventTypes import EventType

class KeyboardEventEnvelop(Event):
    def __init__(self, name, eventType, scanCode, waitingtime, time, device, iskeypad, modifiers):
        Event.__init__(self, eventType)
        self.name= name
        self.scanCode= scanCode
        self.waitingTime = waitingtime
        self.time= time
        self.device= device
        self.isKeypad= iskeypad
        self.modifiers= modifiers

    def getName(self):
        return self.name

    def getWaitingTime(self):
        return self.waitingTime

    def getDevice(self):
        return self.device

    def getScanCode(self):
        return self.scanCode

    def getTime(self):
        return self.time

    def getIsKeypad(self):
        return self.isKeypad

    def getModifiers(self):
        return self.modifiers

    def getEventType(self):
        return self.eventType

    def to_dict(self):
        attrs = dict(
            (attr, getattr(self, attr)) for attr in ['name', 'eventType' ,'scanCode', 'waitingTime', 'time', 'device', 'isKeypad', 'modifiers']
        )
        return attrs

#Helper functions
def convertDictToKeyboardEventEnvelop(dictEvent):
    eventtype= EventType(dictEvent.get("eventType"))

    meta= dictEvent.get("meta")

    #Parsing mouse meta information
    name= meta["name"]
    scancode= meta["scanCode"]
    waitingtime= meta["waitingTime"]
    time= meta["time"]
    device= meta["device"]
    iskeypad= meta["isKeypad"]
    modifiers= meta["modifiers"]

    #Preparing envelop
    keyboardEventEnvelop= KeyboardEventEnvelop(name, eventtype, scancode, waitingtime, time, device, iskeypad, modifiers)

    return keyboardEventEnvelop