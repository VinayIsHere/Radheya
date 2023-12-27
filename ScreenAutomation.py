from src import EnableDPISetting
from src.Listener import MouseEventsListener
from src.Event.EventTypes import EventType
from src.Event.EventDispatcher import EventsDispatcher
import keyboard
from src.ApplicationModes import ApplicationModes
from src.Actions.ActionManager import ActionManagerController
from src.Actions.ActionsType import ActionsType
from src.EventRecorder import EventRecorderDependencySetup
from src.EventReplayer import EventReplayerDependencySetup

#Setting application mode to Off Initially.
AppMode= ApplicationModes.eOffMode

#Enable DPI Awareness for our Application.
EnableDPISetting.EnableWindowsDPIAware()

eventReader= None

def SubscribeMouseEvents(subscriber):
    
    #Subscribing Events
    EventsDispatcher.subscribeEvent(EventType.eMousePressEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eMouseReleaseEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eMouseMoveEvent, subscriber)

def startEventRecording():
    global AppMode

    #Changing Current Action Manager to indicate Write Action is ON.
    ActionManagerController.changeCurrentAction(ActionsType.eWriteAction)

    #Setting App Mode to Record Mode for Keyboard and Mouse Event.
    AppMode= ApplicationModes.eRecordMode | ApplicationModes.eKeyboardAndMouseEventRecordMode

    #Setting up Activity Recorder
    ActivityRecorder= EventRecorderDependencySetup.SetupAutomationEventRecorder()
    
    #Subscriving All Mouse Events for Activity Recorder.
    SubscribeMouseEvents(ActivityRecorder)

    MouseEventsListener.InitializeMouseEventsListener()
    MouseEventsListener.StartListeningToMouseEvents()

    print("started EventRecorder")
    
def startEventReplaying():
    global AppMode
    global eventReader

    AppMode= ApplicationModes.eReplayMode | ApplicationModes.eMouseAndKeyboardReplayMode

    ActionManagerController.changeCurrentAction(ActionsType.eReplayAction)
    
    eventReader, eventReplayer= EventReplayerDependencySetup.SetupEventReaderAndReplayer()
    SubscribeMouseEvents(eventReplayer)

    eventReader.start()
    print("Started Event Replayer")

def stopRecordingOrReplaying():
    global AppMode

    if(AppMode == (ApplicationModes.eRecordMode | ApplicationModes.eKeyboardAndMouseEventRecordMode)):
        EventsDispatcher.unsubscribeAll()
        MouseEventsListener.StopListeningToMouseEvent()
        print("stopping Listening to MouseEvents")
    elif(AppMode == (ApplicationModes.eReplayMode | ApplicationModes.eMouseAndKeyboardReplayMode)):
        eventReader.stop()
        EventsDispatcher.unsubscribeAll()        
        print("stopping event Replaying")
    
def on_key_event(keyboardEvent):
    if(keyboardEvent.event_type == keyboard.KEY_DOWN):
        if(keyboard.is_pressed("ctrl+s")):
            startEventRecording()
        elif(keyboard.is_pressed("ctrl+r")):
            startEventReplaying()
        elif(keyboard.is_pressed("ctrl+end")):
            stopRecordingOrReplaying()

def main():
    keyboard.hook(on_key_event)
    keyboard.wait("esc")

if(__name__ == "__main__"):
    main()