import sys
sys.path.append("..")

from ..ActionsType import ActionsType
from ..Action import Action
from ..ActionManager import ActionManagerController

class MouseReleaseAction(Action):
    
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
        print("release action write")
        self.storage.Write(event)

    def ReadAction(self, event):
        print("release action read")
        self.storage.Read()

    def replayAction(self, event):
        self._replayer.replayReleaseEvent(event)