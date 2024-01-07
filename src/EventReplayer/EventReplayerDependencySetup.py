from ..Storage.StorageManager import StorageManager
from ..Storage.JsonStorage import JsonStorage
from ..Replayer.MouseReplayer import MouseReplayer
from ..Replayer.KeyboardReplayer import KeyboardReplayer
from ..Actions.MouseActions.MousePressAction import MousePressAction
from ..Actions.MouseActions.MouseMoveAction import MouseMoveAction
from ..Actions.MouseActions.MouseReleaseAction import MouseReleaseAction
from ..Actions.KeyboardActions.KeyboardUpAction import KeyboardUpAction
from ..Actions.KeyboardActions.KeyboardDownAction import KeyboardDownAction
from ..Replayer.MouseEventReplayer import MouseEventReplayer
from ..Replayer.KeyboardEventReplayer import KeyboardEventReplayer
from ..EventReader.EventReader import EventReader
from ..Event.EventDispatcher import EventsDispatcher
from ..EventReplayer.EventReplayer import EventReplayer

storageManager= StorageManager()
mousePressAction= None
mouseMoveAction= None
keyboardUpAction= None
keyboardDownAction= None
mouseReleaseAction= None
storage= None


def SetupStorage(fileToReplay):
    global storageManager
    global storage

    storageManager.ChangeDataSource(fileToReplay)
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

def SetupKeyboardActions():
    global keyboardUpAction
    global keyboardDownAction

    replayer= KeyboardReplayer()

    keyboardUpAction= KeyboardUpAction(storage, replayer)
    keyboardDownAction= KeyboardDownAction(storage, replayer)

def SetupMouseEventReplayer():
    global mousePressAction
    global mouseMoveAction
    global mouseReleaseAction

    return MouseEventReplayer(mousePressAction, mouseMoveAction, mouseReleaseAction)

def SetupKeyboardEventReplayer():
    global keyboardUpAction
    global keyboardDownAction

    return KeyboardEventReplayer(keyboardUpAction, keyboardDownAction)

def SetupEventReaderAndReplayer(fileToReplay):
    
    SetupStorage(fileToReplay)
    SetupMouseActions()
    SetupKeyboardActions()

    return EventReader(storage, EventsDispatcher), EventReplayer(SetupMouseEventReplayer(), SetupKeyboardEventReplayer())

