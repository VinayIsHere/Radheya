from enum import IntEnum

class ExtendedIntEnum(IntEnum):
    @classmethod
    def dict(cls):
        return {i.name: i.value for i in cls}

class ApplicationModes(ExtendedIntEnum):
    eOffMode= 0, #No Activities are currently being performed by Application
    eRecordMode= 8, #Events will be getting recorded
    eMouseEventsRecordMode=1, #Mouse events are getting recorded now.
    eKeyboardEventsRecordMode= 2, #Keyboards Events recording mode
    eKeyboardAndMouseEventRecordMode=4, #Both Mouse and Keyboard Events are getting recorded
    eReplayMode= 128,#Event will be played back from a file
    eMouseEventsReplayMode= 64,
    eKeyboardEventsReplayMode= 32,
    eMouseAndKeyboardReplayMode= 16