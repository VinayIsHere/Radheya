from pynput import mouse
from pynput.mouse import Button, Controller
import time

MouseController= Controller()

class MouseReplayer:
    def __init__(self):
        pass

    def replayMoveEvent(self, event):
        ReplayMouseMoveEvent(event)

    def replayPressEvent(self, event):
        ReplayMousePressEvent(event)

    def replayReleaseEvent(self, event):
        ReplayMouseReleaseEvent(event)

def ReplayMousePressEvent(event):
    global MouseController

    time.sleep(event.getWaitingTime())

    MouseController.position(event.getX(), event.getY())
    MouseController.press(event.getButton())
    time.sleep(1)

def ReplayMouseMoveEvent(event):
    print("do mousemove event, ", event.getX(), event.getY())

def ReplayMouseReleaseEvent(event):
    global MouseController

    time.sleep(event.getWaitingTime())

    MouseController.position(event.getX(), event.getY())
    MouseController.release(event.getButton())
    time.sleep(1)