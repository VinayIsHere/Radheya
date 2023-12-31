from ..ActionsType import ActionsType
from ..Action import Action
from ..ActionManager import ActionManagerController

class KeyboardUpAction(Action):
    def __init__(self, storage, replayer=None):
        Action.__init__(self)
        self._storage= storage
        self._replayer= replayer

    def handleEvent(self, event):
        if(ActionManagerController.currentAction == ActionsType.eWriteAction):
            self.WriteAction(event)
        elif(ActionManagerController.currentAction == ActionsType.eReadAction):
            self.ReadAction(event)
        elif(ActionManagerController.currentAction == ActionsType.eReplayAction):
            self.replayAction(event)

    def replayAction(self, event):
        self._replayer.replayKeyboardUpEvent(event)

    def WriteAction(self, event):
        self._storage.WriteEvent(event)
    
    def ReadAction(self):
        self._storage.Read()