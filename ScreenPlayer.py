from multiprocessing import Event
from src import EnableDPISetting
from src.Listener import MouseEventsListener
from src.Listener import KeyboardEventsListener
from src.Event.EventTypes import EventType
from src.Event.EventDispatcher import EventsDispatcher
from src.ApplicationModes import ApplicationModes
from src.Actions.ActionManager import ActionManagerController
from src.Actions.ActionsType import ActionsType
from src.EventRecorder import EventRecorderDependencySetup
from src.EventReplayer import EventReplayerDependencySetup
from src.Helper.UtilityFunctions import generate_unique_number
import threading
from src.Storage.StorageManager import StorageController

#Enable DPI Awareness for our Application.
EnableDPISetting.EnableWindowsDPIAware()

def SubscribeMouseEvents(subscriber):    
    #Subscribing Events
    EventsDispatcher.subscribeEvent(EventType.eMousePressEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eMouseReleaseEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eMouseMoveEvent, subscriber)

def SubscribeKeyboardEvents(subscriber):
    EventsDispatcher.subscribeEvent(EventType.eKeyboardUpEvent, subscriber)
    EventsDispatcher.subscribeEvent(EventType.eKeyboardDownEvent, subscriber)

def SubscribeStorageEvents(subscriber):
    EventsDispatcher.subscribeEvent(EventType.eSaveIntoStorageEvent, subscriber)

class ScreenRecorderAutomation(threading.Thread):
    
    def __init__(self, appMode):
        super().__init__()
        self.appMode= None
        self.uuid= generate_unique_number()
        self.eventRecorder= None

    def run(self):
        print("start thread")
        self.startEventRecording(ApplicationModes.eKeyboardAndMouseEventRecordMode)
        print("stop thread")

    def getUuid(self):
        return self.uuid

    def startEventRecording(self, appMode):
        #Changing Current Action Manager to indicate Write Action is ON.
        ActionManagerController.changeCurrentAction(ActionsType.eWriteAction)
        self.appMode= appMode
        self.eventRecorder= EventRecorderDependencySetup.SetupAutomationEventRecorder(self.uuid)
    
        SubscribeMouseEvents(self.eventRecorder)
        SubscribeKeyboardEvents(self.eventRecorder)
        SubscribeStorageEvents(self.eventRecorder)

        print("Started EventRecorder")
        MouseEventsListener.MouseListenerController.start()
        KeyboardEventsListener.KeyboardListenerController.start()

    def stopEventRecordingAndSave(self, documentId, filepath, saveOrNot):
        #Saving recording
        self.SaveRecording(documentId, filepath, saveOrNot)

        #unsubscribing subcribers from dispatcher
        EventsDispatcher.unsubscribeAll()

        #stopping listeners.
        MouseEventsListener.MouseListenerController.stop()
        KeyboardEventsListener.KeyboardListenerController.stop()
    
    def SaveRecording(self, docId, filepath, saveOrNot):
        StorageController.SaveIntoStorage(docId, filepath, saveOrNot)

    def notify(self, event):
        EventsDispatcher.publishEvent(event)

class ScreenReplayerAutomation(threading.Thread):
    
    def __init__(self, uuid, fileToReplay):
        super().__init__()
        self.appMode= ApplicationModes.eMouseAndKeyboardReplayMode
        self.uuid= uuid
        self.fileToReplay= fileToReplay
        self.eventReplayer= None

    def run(self):
        self.startEventReplaying(ApplicationModes.eMouseAndKeyboardReplayMode)
    
    def startEventReplaying(self, appMode):
        self.appMode=appMode
        ActionManagerController.changeCurrentAction(ActionsType.eReplayAction)
    
        self.eventReader, self.eventReplayer= EventReplayerDependencySetup.SetupEventReaderAndReplayer(self.fileToReplay)
        SubscribeMouseEvents(self.eventReplayer)
        SubscribeKeyboardEvents(self.eventReplayer)

        print("Started Event Replayer")
        self.eventReader.start()

    def stopEventReplaying(self):
        self.eventReader.stop()
        EventsDispatcher.unsubscribeAll() 
    