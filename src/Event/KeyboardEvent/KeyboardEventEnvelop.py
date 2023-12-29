from ..Event import Event

class KeyboardEventEnvelop(Event):
    def __init__(self, name, scanCode, waitingtime, time, device, iskeypad, modifiers):
        Event.__init__(self)
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
        return self.waitintTime

    def getDevice(self):
        return self.device

    def to_dict(self):
        attrs = dict(
            (attr, getattr(self, attr)) for attr in ['name', 'scanCode', 'waitingTime', 'time', 'device', 'isKeypad', 'modifiers']
        )
        return attrs