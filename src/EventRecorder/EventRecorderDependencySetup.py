import os
from ..Storage.StorageManager import StorageController
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
    StorageController.ChangeDataSource(random_filename)

def SetupStorageManagerProperties(uuid):
    global currRecordingDict
    currRecordingDict[uuid]= dict()
    StorageController.ChangeDataSource(currRecordingDict)

def SetupJsonStorage():
    global storage
    storage= JsonStorage(StorageController.GetDataSource())
    
def SetupMouseActions(uuid):
    global mousePressAction
    global mouseMoveAction
    global mouseReleaseAction
    global storage

    mousePressAction= MousePressAction(StorageController.GetStorageForDocument(uuid))
    mouseMoveAction= MouseMoveAction(StorageController.GetStorageForDocument(uuid))
    mouseReleaseAction= MouseReleaseAction(StorageController.GetStorageForDocument(uuid))
 
def SetupKeyboardActions(uuid):
    global keyboardUpAction
    global keyboardDownAction

    keyboardUpAction= KeyboardUpAction(StorageController.GetStorageForDocument(uuid))
    keyboardDownAction= KeyboardDownAction(StorageController.GetStorageForDocument(uuid))

def SetupMouseEventRecorder():
    global mousePressAction
    global mouseMoveAction
    global mouseReleaseAction

    return MouseEventRecorder(mousePressAction, mouseMoveAction, mouseReleaseAction)

def SetupKeyboardEventRecorder():
    global keyboardUpAction
    global keyboardDownAction

    return KeyboardEventRecorder(keyboardUpAction, keyboardDownAction)

def SetupAutomationEventRecorder(uuid):
 
    #SetupNewFileForWritingEvents()
    
    EventRecorderController.SetCurrentEventRecordingDocumentID(uuid)
    SetupStorageManagerProperties(uuid)
    ActionManagerController.AddSequenceCounterForUuid(uuid)
    
    SetupJsonStorage()
    StorageController.AddDocumentForStorage(uuid, storage)

    SetupMouseActions(uuid)
    SetupKeyboardActions(uuid)

    return AutomationRecorder(SetupMouseEventRecorder(), SetupKeyboardEventRecorder())
