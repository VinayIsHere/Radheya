import EnableDPISetting
from Event import EventQueue
from Listener import MouseEventsListener
from EventRecorder.AutomationRecorder import AutomationRecorder
from Event.EventTypes import EventType
from Event.EventDispatcher import MouseEventDispatcher
from EventRecorder.MouseEventRecorder import MouseEventRecorder
from Actions.MouseActions.MousePressAction import MousePressAction
from Actions.MouseActions.MouseMoveAction import MouseMoveAction
from Actions.MouseActions.MouseReleaseAction import MouseReleaseAction
from Storage.JsonStorage import JsonStorage
from Storage.StorageManager import StorageManager
import uuid
import os
import keyboard


#Only for Testing purpose, replace it with taking the file name as input from UI.
def generate_random_filename():
    # Create the "jsonfiles" directory if it doesn't exist
    jsonfiles_directory = "jsonfiles"
    if not os.path.exists(jsonfiles_directory):
        os.makedirs(jsonfiles_directory)

    # Generate a random filename within the "jsonfiles" directory
    random_filename = os.path.join(jsonfiles_directory, str(uuid.uuid4()) + '.json')
    return random_filename

#Enable DPI Awareness for our Application.
EnableDPISetting.EnableWindowsDPIAware()
storageManager= StorageManager()

def main():

    global storageManager

    #ToDo: Create Separate Class for doing Dependendy injection
    FileName= generate_random_filename()
    print("New File Created: {0}".format(FileName))
    storageManager.ChangeDataSource(FileName)

    storage= JsonStorage(storageManager.GetDataSource())

    _mousePressAction= MousePressAction(storage)
    _mouseMoveAction= MouseMoveAction(storage)
    _mouseReleaseAction= MouseReleaseAction(storage)
    _mouseEventRecorder= MouseEventRecorder(_mousePressAction, _mouseMoveAction, _mouseReleaseAction)

    ActivityRecorder= AutomationRecorder(_mouseEventRecorder)

    #Subscribing Events
    MouseEventDispatcher.subscribeEvent(EventType.eMousePressEvent, ActivityRecorder)
    MouseEventDispatcher.subscribeEvent(EventType.eMouseReleaseEvent, ActivityRecorder)
    MouseEventDispatcher.subscribeEvent(EventType.eMouseMoveEvent, ActivityRecorder)
    
    #with mouse.Listener(
    #        on_move=MouseListener.OnMove,
    #        on_click=MouseListener.OnClick,
    #        ) as MouseListener:
    #    MouseListener.join()

def startFunctionality():
    main()
    MouseEventsListener.InitializeMouseEventsListener()
    MouseEventsListener.StartListeningToMouseEvents()
    print("starting MouseListener")
    
def stopFunctionality():
    print("stopping Listening to MouseEvents")
    MouseEventsListener.StopListeningToMouseEvent()

def on_key_event(keyboardEvent):
    if(keyboardEvent.event_type == keyboard.KEY_DOWN):
        if(keyboard.is_pressed("ctrl+s")):
            startFunctionality()
        elif(keyboard.is_pressed("ctrl+end")):
            stopFunctionality()

if(__name__ == "__main__"):
    keyboard.hook(on_key_event)
    keyboard.wait("esc")