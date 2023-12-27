import json
import EnableDPISetting
from Event import EventQueue
from Listener import MouseEventsListener
from EventRecorder.AutomationRecorder import AutomationRecorder
from Event.EventTypes import EventType
from Event.EventDispatcher import EventsDispatcher
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
from EventReader.EventReader import EventReader
from EventReplayer.EventReplayer import EventReplayer
from Actions.ActionManager import ActionManagerController
from Actions.ActionsType import ActionsType
from Replayer.MouseReplayer import MouseReplayer
from Replayer.MouseEventReplayer import MouseEventReplayer

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
    EventsDispatcher.subscribeEvent(EventType.eMousePressEvent, ActivityRecorder)
    EventsDispatcher.subscribeEvent(EventType.eMouseReleaseEvent, ActivityRecorder)
    EventsDispatcher.subscribeEvent(EventType.eMouseMoveEvent, ActivityRecorder)

def startEventRecording():
    global AppMode

    ActionManagerController.changeCurrentAction(ActionsType.eWriteAction)

    AppMode= ApplicationModes.eRecordMode | ApplicationModes.eKeyboardAndMouseEventRecordMode
    RecordingEventSetup()
    MouseEventsListener.InitializeMouseEventsListener()
    MouseEventsListener.StartListeningToMouseEvents()
    print("starting MouseListener")
    
def startEventReplaying():
    global storageManager
    print("startEventReplaying")

    replayer= MouseReplayer()

    ActionManagerController.changeCurrentAction(ActionsType.eReplayAction)

    fileToReplay= "8be51c7e-ad34-4dbf-93ac-d11915ab0017.json" #this should come from the UI, for now passing from here.
    storageManager.ChangeDataSource("jsonfiles/"+fileToReplay)

    storage= JsonStorage(storageManager.GetDataSource())

    _mousePressAction= MousePressAction(storage, replayer)
    _mouseMoveAction= MouseMoveAction(storage, replayer)
    _mouseReleaseAction= MouseReleaseAction(storage, replayer)
    
    mouseReplayer= MouseEventReplayer(_mousePressAction, _mouseMoveAction, _mouseReleaseAction)

    eventReader= EventReader(storage, EventsDispatcher)
    eventReplayer= EventReplayer(mouseReplayer)

    #Subscribing Events
    EventsDispatcher.subscribeEvent(EventType.eMousePressEvent, eventReplayer)
    EventsDispatcher.subscribeEvent(EventType.eMouseReleaseEvent, eventReplayer)
    EventsDispatcher.subscribeEvent(EventType.eMouseMoveEvent, eventReplayer)
    
    eventReader.start()

def stopActivities():
    global AppMode

    if(AppMode == (ApplicationModes.eRecordMode | ApplicationModes.eKeyboardAndMouseEventRecordMode)):
        EventsDispatcher.unsubscribeAll()
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