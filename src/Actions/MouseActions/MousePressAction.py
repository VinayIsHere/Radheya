from ..ActionsType import ActionsType
from ..Action import Action
from ..ActionManager import ActionManagerController

class MousePressAction(Action):
    
    def __init__(self, storage, replayer=None):
        Action.__init__(self)
        self.storage= storage
        self._replayer= replayer

    def handleEvent(self, event):
        if(ActionManagerController.currentAction == ActionsType.eWriteAction):
            self.WriteAction(event)
        elif(ActionManagerController.currentAction == ActionsType.eReadAction):
            self.ReadAction(event)
        elif(ActionManagerController.currentAction == ActionsType.eReplayAction):
            self.replayAction(event)

    def WriteAction(self, event):
        self.storage.WriteEvent(event)

    def ReadAction(self, event):
        self.storage.Read()

    def replayAction(self, event):
        self._replayer.replayPressEvent(event)