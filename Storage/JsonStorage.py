import sys
sys.path.append("..")

import json
from Event.EventTypes import EventType
from .Storage import Storage, EVENT_TYPE_KEY, META_KEY
from pynput.mouse import Button
from Event.MouseEvent.MouseEventEnvelop import CreateMouseEventEnvelop

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
    if is_mouse_event(event.getEventType()):
        return generate_mouse_event_meta_data(event)
    elif is_keyboard_event(event.getEventType()):
        return generate_keyboard_event_meta_data(event)
    return "empty"

def is_mouse_event(eventType):
    return eventType in [
        EventType.eMousePressEvent,
        EventType.eMouseReleaseEvent,
        EventType.eMouseMoveEvent,
        EventType.eMousePressedAndMoveEvent
    ]

def is_keyboard_event(eventType):
    return False  # Not implemented as of now

def generate_mouse_event_meta_data(event):
    meta = {
        'x': int(event.getX()),
        'y': int(event.getY()),
        'waitingtime': int(event.getWaitingTime()),  # in ms
        'button': event.getButton().value if event.getButton() else "None",
        'ispressed': int(event.isPressed()) if event.isPressed() else 0
    }
    return meta

def generate_keyboard_event_meta_data(event):
    return ""

def convert_dictionary_to_event(dictEvent):
    
    eventType = EventType(dictEvent.get("eventtype"))
    eventEnvelop= None

    if is_mouse_event(eventType):
        eventEnvelop= convert_dictionry_to_mouse_event(dictEvent)
    elif(is_keyboard_event(eventType)):
        eventEnvelop= convert_dictionary_to_keyboard_event(dictEvent)

    return eventEnvelop

def convert_dictionry_to_mouse_event(dictEvent):
    eventType= EventType(dictEvent.get("eventtype"))

    meta= dictEvent.get("meta")

    #Parsing Mouse Meta Information
    button= None
    if(meta.get("button") != "None"):
        button= Button(tuple(meta.get("button")))
       
    x= int(meta.get("x"))
    y= int(meta.get("y"))
    ispressed= int(meta.get("ispressed"))
    waitingtime= int(meta.get("waitingtime"))

    mouseEventEnvelop= CreateMouseEventEnvelop(x, y, eventType, ispressed, waitingtime, button)

    return mouseEventEnvelop

def convert_dictionary_to_keyboard_event(dictEvent):
    pass #Feature Not implemented