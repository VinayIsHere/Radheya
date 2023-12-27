from enum import IntEnum

class ActionsType(IntEnum):
    eInvalidAction= -1,
    eReadAction=0,
    eWriteAction=1,
    eReplayAction= 2