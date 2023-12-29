import json
from ..Event.EventTypes import EventType
from .Storage import Storage, EVENT_TYPE_KEY, META_KEY
from ..Event.MouseEvent.MouseEventEnvelop import convertDictToMouseEventEnvelop
from ..Event.KeyboardEvent.KeyboardEventEnvelop import convertDictToKeyboardEventEnvelop

class JsonStorage(Storage):
    def __init__(self, dataSource):
        super().__init__(dataSource)

    def Write(self, event):
        data = convert_event_to_dictionary(event)

        with open(self._data, 'a') as file:
            json.dump(data, file)
            file.write("\n")

    def Read(self):
        events= []

        with open(self._data, 'r') as file:
            for line in file:
                event_data= json.loads(line)
                event= convert_dictionary_to_event(event_data)
                events.append(event)
        return events

def convert_event_to_dictionary(event):
    data = {
        EVENT_TYPE_KEY: int(event.getEventType()),
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
    
    eventType = EventType(dictEvent.get("eventType"))
    eventEnvelop= None

    if is_mouse_event(eventType):
        eventEnvelop= convertDictToMouseEventEnvelop(dictEvent)
    elif(is_keyboard_event(eventType)):
        eventEnvelop= convertDictToKeyboardEventEnvelop(dictEvent)

    return eventEnvelop