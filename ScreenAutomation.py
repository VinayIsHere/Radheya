from src import EnableDPISetting
from src.Listener import MouseEventsListener
from src.Listener import KeyboardEventsListener
from src.Event.EventTypes import EventType
from src.Event.EventDispatcher import EventsDispatcher
import keyboard
from src.ApplicationModes import ApplicationModes
from src.Actions.ActionManager import ActionManagerController
from src.Actions.ActionsType import ActionsType
from src.EventRecorder import EventRecorderDependencySetup
from src.EventReplayer import EventReplayerDependencySetup
from src.Helper.UtilityFunctions import generate_unique_number

#Setting application mode to Off Initially.
AppMode= ApplicationModes.eOffMode

#Enable DPI Awareness for our Application.
EnableDPISetting.EnableWindowsDPIAware()

eventReader= None
CurrentRecordingUUID= None

def SubscribeMouseEvents(subscriber):
    
    #Subscribing Events
    EventsDispatcher.subscribeEvent(EventType.eMousePressEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eMouseReleaseEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eMouseMoveEvent, subscriber)

def SubscribeKeyboardEvents(subscriber):

    EventsDispatcher.subscribeEvent(EventType.eKeyboardUpEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eKeyboardDownEvent, subscriber)

def startEventRecording(appMode):
    global AppMode
    global CurrentRecordingUUID

    #Changing Current Action Manager to indicate Write Action is ON.
    ActionManagerController.changeCurrentAction(ActionsType.eWriteAction)
    AppMode= appMode

    CurrentRecordingUUID= generate_unique_number()

    #Setting up Activity Recorder
    ActivityRecorder= EventRecorderDependencySetup.SetupAutomationEventRecorder(CurrentRecordingUUID)
    
    #Subscriving All Mouse Events for Activity Recorder.
    SubscribeMouseEvents(ActivityRecorder)
    SubscribeKeyboardEvents(ActivityRecorder)
    
    print("Started EventRecorder")
    MouseEventsListener.MouseListenerController.start()
    KeyboardEventsListener.KeyboardListenerController.start()
    
def startEventReplaying(appMode):
    global AppMode
    global eventReader

    AppMode=appMode
    ActionManagerController.changeCurrentAction(ActionsType.eReplayAction)
    
    eventReader, eventReplayer= EventReplayerDependencySetup.SetupEventReaderAndReplayer()
    SubscribeMouseEvents(eventReplayer)
    SubscribeKeyboardEvents(eventReplayer)

    print("Started Event Replayer")
    eventReader.start()
    
def stopRecordingOrReplaying():
    global AppMode

    if(AppMode == (ApplicationModes.eKeyboardAndMouseEventRecordMode)):
        EventsDispatcher.unsubscribeAll()
        MouseEventsListener.MouseListenerController.stop()
        print("stopping Listening to MouseEvents")
    elif(AppMode == (ApplicationModes.eMouseAndKeyboardReplayMode)):
        eventReader.stop()
        EventsDispatcher.unsubscribeAll()        
        print("stopping event Replaying")

