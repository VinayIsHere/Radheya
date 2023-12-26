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
from ApplicationModes import ApplicationModes

AppMode= ApplicationModes.eOffMode

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

def RecordingEventSetup():

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

def startEventRecording():
    global AppMode

    AppMode= ApplicationModes.eRecordMode | ApplicationModes.eKeyboardAndMouseEventRecordMode
    RecordingEventSetup()
    MouseEventsListener.InitializeMouseEventsListener()
    MouseEventsListener.StartListeningToMouseEvents()
    print("starting MouseListener")
    
def startEventReplaying():
    print("startEventReplaying")
    fileToReplay= "4944dc0b-7518-41e5-ad27-5a1fbd6b8b90.json" #this should come from the UI, for now passing from here.

def stopActivities():
    global AppMode

    if(AppMode == (ApplicationModes.eRecordMode | ApplicationModes.eKeyboardAndMouseEventRecordMode)):
        MouseEventDispatcher.unsubscribeAll()
        MouseEventsListener.StopListeningToMouseEvent()
        print("stopping Listening to MouseEvents")
    
def on_key_event(keyboardEvent):
    if(keyboardEvent.event_type == keyboard.KEY_DOWN):
        if(keyboard.is_pressed("ctrl+s")):
            startEventRecording()
        elif(keyboard.is_pressed("ctrl+r")):
            startEventReplaying()
        elif(keyboard.is_pressed("ctrl+end")):
            stopActivities()

def main():
    keyboard.hook(on_key_event)
    keyboard.wait("esc")

if(__name__ == "__main__"):
    main()