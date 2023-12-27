from pynput import mouse
from . import MouseListener

#Listener which will capture the Mouse events
MouseEventListener= mouse.Listener()

def InitializeMouseEventsListener():
    global MouseEventListener

    MouseEventListener= mouse.Listener(
    on_move=MouseListener.OnMove,
    on_click=MouseListener.OnClick)

def StartListeningToMouseEvents():
    global MouseEventListener
    MouseEventListener.start()

def StopListeningToMouseEvent():
    global MouseEventListener
    MouseEventListener.stop()
