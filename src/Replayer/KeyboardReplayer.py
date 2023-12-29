import keyboard
import time

class KeyboardReplayer():
    def __init__(self):
        pass
        
    def replayKeyboardUpEvent(self, event):
        ReplayKeyboardReleaseEvent(event)

    def replayKeyboardDownEvent(self, event):
        ReplayKeyboardPressEvent(event)

def ReplayKeyboardPressEvent(event):
    
    print(f"keyboardPressEvent: event: {event.to_dict()}")

    #delay before performing the action
    time.sleep((event.getWaitingTime()*0.001)) #converting to seconds

    keyboard.press(event.getName())

def ReplayKeyboardReleaseEvent(event):
    print(f"keyboardReleaseEvent: event: {event.to_dict()}")

    #delay before performing the action
    time.sleep((event.getWaitingTime()*0.001)) #converting to seconds

    keyboard.release(event.getName())