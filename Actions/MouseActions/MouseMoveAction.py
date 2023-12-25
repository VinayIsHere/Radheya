import sys
sys.path.append("..")

from ..ActionsType import ActionsType
from ..Action import Action
from ..ActionManager import ActionManagerController

class MouseMoveAction(Action):
    
    def __init__(self, storage):
        Action.__init__(self)
        self.storage= storage

    def handleEvent(self, event):
        #Only record Move event when mouse is pressed.
        if(event.isPressed() == False or event.isPressed() == None):
            return

        if(ActionManagerController.currentAction == ActionsType.eWriteAction):
            self.WriteAction(event)
        elif(ActionManagerController.currentAction == ActionsType.eReadAction):
            self.ReadAction(event)

    def WriteAction(self, event):
        self.storage.Write(event)

    def ReadAction(self, event):
        self.storage.Read()