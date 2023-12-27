from enum import IntEnum

class ApplicationModes(IntEnum):
    eOffMode= 0, #No Activities are currently being performed by Application
    eRecordMode= 8, #Events will be getting recorded
    eMouseEventsRecordMode=1, #Mouse events are getting recorded now.
    eKeyboardEventsRecordMode= 2, #Keyboards Events recording mode
    eKeyboardAndMouseEventRecordMode=4, #Both Mouse and Keyboard Events are getting recorded
    eReplayMode= 128,#Event will be played back from a file
    eMouseEventsReplayMode= 64,
    eKeyboardEventsReplayMode= 32,
    eMouseAndKeyboardReplayMode= 16