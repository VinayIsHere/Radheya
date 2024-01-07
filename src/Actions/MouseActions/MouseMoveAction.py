from ..ActionsType import ActionsType
from ..Action import Action
from ..ActionManager import ActionManagerController

class MouseMoveAction(Action):
    
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

    def WriteAction(self, event):
        #Only record Move event when mouse is pressed
        if(event.isPressed() == False or event.isPressed() == None):
            return

        self._storage.WriteEvent(event)

    def ReadAction(self):
        self._storage.Read()

    def replayAction(self, event):
        self._replayer.replayMoveEvent(event)