from .ActionsType import ActionsType
from ..DesignPatterns.SingletonMeta import singleton

#Manager contains information about All Actions taking place at Global level.
@singleton
class ActionManager:
    def __init__(self, currentAction):
        self.currentAction = currentAction

    def changeCurrentAction(self, action):
        self.currentAction= action

ActionManagerController= ActionManager(ActionsType.eWriteAction)