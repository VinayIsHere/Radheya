from enum import IntEnum

class EventType(IntEnum):
    eInvalidEvent= -1,
    eStartingEvent= 0,
    eMousePressEvent= 1,
    eMouseReleaseEvent= 2,
    eMouseMoveEvent= 3,
    eMousePressedAndMoveEvent= 4,
    eKeyboardEvent= 5,
    eEndingEvent= 6