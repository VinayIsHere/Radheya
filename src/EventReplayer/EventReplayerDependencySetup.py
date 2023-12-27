from ..Storage.StorageManager import StorageManager
from ..Storage.JsonStorage import JsonStorage
from ..Replayer.MouseReplayer import MouseReplayer
from ..Actions.MouseActions.MousePressAction import MousePressAction
from ..Actions.MouseActions.MouseMoveAction import MouseMoveAction
from ..Actions.MouseActions.MouseReleaseAction import MouseReleaseAction
from ..Replayer.MouseEventReplayer import MouseEventReplayer
from ..EventReader.EventReader import EventReader
from ..Event.EventDispatcher import EventsDispatcher
from ..EventReplayer.EventReplayer import EventReplayer

storageManager= StorageManager()
mousePressAction= None
mouseMoveAction= None
mouseReleaseAction= None
storage= None

def GetJsonFileToReplay():
    return "22d8bc05-896e-4640-8fdc-69cac40fdfa7.json" #this should come from the UI, for now passing from here.

def SetupStorage():
    global storageManager
    global storage

    storageManager.ChangeDataSource("jsonfiles/"+GetJsonFileToReplay())
    storage=JsonStorage(storageManager.GetDataSource())

def SetupMouseActions():
    global storage
    global mousePressAction
    global mouseMoveAction
    global mouseReleaseAction

    replayer= MouseReplayer()
    
    mousePressAction= MousePressAction(storage, replayer)
    mouseMoveAction= MouseMoveAction(storage, replayer)
    mouseReleaseAction= MouseReleaseAction(storage, replayer)

def SetupMouseEventReplayer():
    global mousePressAction
    global mouseMoveAction
    global mouseReleaseAction

    return MouseEventReplayer(mousePressAction, mouseMoveAction, mouseReleaseAction)

def SetupEventReaderAndReplayer():
    
    SetupStorage()
    SetupMouseActions()

    return EventReader(storage, EventsDispatcher), EventReplayer(SetupMouseEventReplayer())