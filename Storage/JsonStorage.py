import sys
sys.path.append("..")

import json
from Event.EventTypes import EventType
from .Storage import Storage, EVENT_TYPE_KEY, META_KEY

class JsonStorage(Storage):
    def __init__(self, dataSource):
        super().__init__(dataSource)

    def Write(self, event):
        data = convert_event_to_dictionary(event)

        with open(self._data, 'a') as file:
            json.dump(data, file)
            file.write("\n")

    def Read(self):
        pass

def convert_event_to_dictionary(event):
    data = {
        EVENT_TYPE_KEY: int(event.getEventType()),
        META_KEY: get_event_meta(event)
    }
    return data

def get_event_meta(event):
    if is_mouse_event(event):
        return generate_mouse_event_meta_data(event)
    elif is_keyboard_event(event):
        return generate_keyboard_event_meta_data(event)
    return "empty"

def is_mouse_event(event):
    return event.getEventType() in [
        EventType.eMousePressEvent,
        EventType.eMouseReleaseEvent,
        EventType.eMouseMoveEvent,
        EventType.eMousePressedAndMoveEvent
    ]

def is_keyboard_event(event):
    return False  # Not implemented as of now

def generate_mouse_event_meta_data(event):
    meta = {
        'x': int(event.getX()),
        'y': int(event.getY()),
        'waitingtime': int(event.getWaitingTime()),  # in ms
        'button': event.getButton().value[0] if event.getButton() else "None",
        'ispressed': int(event.isPressed()) if event.isPressed() else 0
    }
    return meta

def generate_keyboard_event_meta_data(event):
    return ""
