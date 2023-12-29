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

storageManager= StorageManager()
storage= None
mousePressAction= None
mouseMoveAction= None
mouseReleaseAction= None
keyboardUpAction= None
keyboardDownAction= None

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

def SetupAutomationEventRecorder():
    
    SetupNewFileForWritingEvents()
    SetupJsonStorage()
    SetupMouseActions()
    SetupKeyboardActions()

    return AutomationRecorder(SetupMouseEventRecorder(), SetupKeyboardEventRecorder())

