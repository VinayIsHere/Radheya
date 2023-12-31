import json
from ..Event.EventTypes import EventType
from .Storage import Storage, EVENT_SEQUENCE_NO , META_KEY
from ..Event.MouseEvent.MouseEventEnvelop import convertDictToMouseEventEnvelop
from ..Event.KeyboardEvent.KeyboardEventEnvelop import convertDictToKeyboardEventEnvelop
from ..Actions.ActionManager import ActionManagerController

class JsonStorage(Storage):
    def __init__(self, dataSource):
        super().__init__(dataSource)

    def WriteEvent(self, event):
        data= convert_event_to_dictionary(event)
        seq_no=ActionManagerController.GetCurrentEventSequenceNumber(event.getParentUuid())
        self._data[event.getParentUuid()][seq_no]= data
        
    def InternalWrite(self, filename):
        with open(filename, 'a') as file:
            json.dump(self._data, file)
            file.write("\n")

    def Read(self):
        
        totalevents= []

        file= open(self._data)
        eventsJson= json.load(file)

        for uuid in eventsJson.keys():
            eventsDict= eventsJson[uuid]
            
            for seq_no, event in eventsDict.items():
                eventEnvelop= convert_dictionary_to_event(event)
                totalevents.append(eventEnvelop)

        return totalevents

def convert_event_to_dictionary(event):
    data = {
        META_KEY: get_event_meta(event)
    }
    return data

def get_event_meta(event):
    return event.to_dict()

def is_mouse_event(eventType):
    return eventType in [
        EventType.eMousePressEvent,
        EventType.eMouseReleaseEvent,
        EventType.eMouseMoveEvent,
        EventType.eMousePressedAndMoveEvent
    ]

def is_keyboard_event(eventType):
    if(eventType in [ EventType.eKeyboardUpEvent, EventType.eKeyboardDownEvent]):
        return True

    return False

def convert_dictionary_to_event(dictEvent):
    
    eventType = EventType(dictEvent.get("meta").get("eventType"))
    eventEnvelop= None

    if is_mouse_event(eventType):
        eventEnvelop= convertDictToMouseEventEnvelop(dictEvent)
    elif(is_keyboard_event(eventType)):
        eventEnvelop= convertDictToKeyboardEventEnvelop(dictEvent)

    return eventEnvelop