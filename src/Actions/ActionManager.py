from .ActionsType import ActionsType
from ..DesignPatterns.SingletonMeta import singleton

#Manager contains information about All Actions taking place at Global level.
@singleton
class ActionManager:
    def __init__(self, currentAction):
        self.currentAction = currentAction
        self.seqManager= dict()

    def AddSequenceCounterForUuid(self, uuid):
        self.seqManager[uuid]= 0
        
    def RemoveSequenceCounterForUuid(self, uuid):
        self.seqManager.pop(uuid)

    def changeCurrentAction(self, action):
        self.currentAction= action

    def IncrementSequenceNumber(self, uuid):
        self.seqManager[uuid]+=1

    def GetCurrentEventSequenceNumber(self, uuid):
        seq_no= self.seqManager[uuid]
        self.IncrementSequenceNumber(uuid)
        return seq_no


ActionManagerController= ActionManager(ActionsType.eWriteAction)