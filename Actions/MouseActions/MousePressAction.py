import sys
sys.path.append("..")

from ..ActionsType import ActionsType
from ..Action import Action
from ..ActionManager import ActionManagerController

class MousePressAction(Action):
    
    def __init__(self, storage):
        Action.__init__(self)
        self.storage= storage

    def handleEvent(self, event):
        
        if(ActionManagerController.currentAction == ActionsType.eWriteAction):
            self.WriteAction(event)
        elif(ActionManagerController.currentAction == ActionsType.eReadAction):
            self.ReadAction(event)

    def WriteAction(self, event):
        self.storage.Write(event)

    def ReadAction(self, event):
        self.storage.Read()