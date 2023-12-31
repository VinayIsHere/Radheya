import os
from ..Storage.StorageManager import StorageManager
from ..Helper.UtilityFunctions import generate_unique_number
from ..Storage.JsonStorage import JsonStorage
from ..Actions.MouseActions.MousePressAction import MousePressAction
from ..Actions.MouseActions.MouseMoveAction import MouseMoveAction
from ..Actions.MouseActions.MouseReleaseAction import MouseReleaseAction
from ..Actions.KeyboardActions.KeyboardUpAction import KeyboardUpAction
from ..Actions.KeyboardActions.KeyboardDownAction import KeyboardDownAction
from ..EventRecorder.AutomationRecorder import AutomationRecorder
from ..EventRecorder.MouseEventRecorder import MouseEventRecorder
from ..EventRecorder.KeyboardEventRecorder import KeyboardEventRecorder
from ..Actions.ActionManager import ActionManagerController
from ..EventRecorder.EventRecorderManager import EventRecorderController

storageManager= StorageManager()
storage= None
mousePressAction= None
mouseMoveAction= None
mouseReleaseAction= None
keyboardUpAction= None
keyboardDownAction= None
currRecordingDict= dict()

def generate_random_json_filename():
    return generate_unique_number()+'.json'

def SetupNewFileForWritingEvents():
    jsonfiles_directory = "jsonfiles"

    if not os.path.exists(jsonfiles_directory):
        os.makedirs(jsonfiles_directory)
        
    fileName= generate_random_json_filename()
    random_filename = os.path.join(jsonfiles_directory, fileName)
    
    print("New File Created: {0}".format(random_filename))
    storageManager.ChangeDataSource(random_filename)

def SetupStorageManagerProperties(uuid):
    global currRecordingDict
    currRecordingDict[uuid]= dict()
    storageManager.ChangeDataSource(currRecordingDict)

def SetupJsonStorage():
    global storage
    storage= JsonStorage(storageManager.GetDataSource())
    
def SetupMouseActions():
    global mousePressAction
    global mouseMoveAction
    global mouseReleaseAction
    global storage

    mousePressAction= MousePressAction(storage)
    mouseMoveAction= MouseMoveAction(storage)
    mouseReleaseAction= MouseReleaseAction(storage)
 
def SetupKeyboardActions():
    global keyboardUpAction
    global keyboardDownAction

    keyboardUpAction= KeyboardUpAction(storage)
    keyboardDownAction= KeyboardDownAction(storage)

def SetupMouseEventRecorder():
    global mousePressAction
    global mouseMoveAction
    global mouseReleaseAction

    return MouseEventRecorder(mousePressAction, mouseMoveAction, mouseReleaseAction)

def SetupKeyboardEventRecorder():
    global keyboardUpAction
    global keyboardDownAction

    return KeyboardEventRecorder(keyboardUpAction, keyboardDownAction)


def saveFile():
    global storage
    storage.InternalWrite("abc.json")

def SetupAutomationEventRecorder(uuid):
    
    #SetupNewFileForWritingEvents()
    
    EventRecorderController.SetCurrentEventRecordingDocumentID(uuid)
    SetupStorageManagerProperties(uuid)
    ActionManagerController.AddSequenceCounterForUuid(uuid)
    SetupJsonStorage()
    SetupMouseActions()
    SetupKeyboardActions()

    return AutomationRecorder(SetupMouseEventRecorder(), SetupKeyboardEventRecorder())
