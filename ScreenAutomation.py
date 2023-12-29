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

def SubscribeKeyboardEvents(subscriber):

    EventsDispatcher.subscribeEvent(EventType.eKeyboardUpEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eKeyboardDownEvent, subscriber)

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
    SubscribeKeyboardEvents(ActivityRecorder)
    
    print("Started EventRecorder")
    MouseEventsListener.MouseListenerController.start()
    KeyboardEventsListener.KeyboardListenerController.start()
    
    
def startEventReplaying():
    global AppMode
    global eventReader

    AppMode= ApplicationModes.eReplayMode | ApplicationModes.eMouseAndKeyboardReplayMode

    ActionManagerController.changeCurrentAction(ActionsType.eReplayAction)
    
    eventReader, eventReplayer= EventReplayerDependencySetup.SetupEventReaderAndReplayer()
    SubscribeMouseEvents(eventReplayer)
    SubscribeKeyboardEvents(eventReplayer)

    print("Started Event Replayer")
    eventReader.start()
    
def stopRecordingOrReplaying():
    global AppMode

    if(AppMode == (ApplicationModes.eRecordMode | ApplicationModes.eKeyboardAndMouseEventRecordMode)):
        EventsDispatcher.unsubscribeAll()
        MouseEventsListener.MouseListenerController.stop()
        print("stopping Listening to MouseEvents")
    elif(AppMode == (ApplicationModes.eReplayMode | ApplicationModes.eMouseAndKeyboardReplayMode)):
        eventReader.stop()
        EventsDispatcher.unsubscribeAll()        
        print("stopping event Replaying")
    
#def on_key_event(keyboardEvent):
#    if(keyboardEvent.event_type == keyboard.KEY_DOWN):
#        if(keyboard.is_pressed("f5")):
#            startEventRecording()
#        elif(keyboard.is_pressed("ctrl+r")):
#            startEventReplaying()
#        elif(keyboard.is_pressed("end")):
#            stopRecordingOrReplaying()

def main():
    #startEventRecording()
    startEventReplaying()
   
if(__name__ == "__main__"):
    main()