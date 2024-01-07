from ..DesignPatterns.SingletonMeta import singleton

@singleton
class EventRecorderManager:

    def __init__(self):
        self.documentsId= list()
        self.currDocumentId= None

    def AddDocumentId(self, id):

        #Checking if already there
        if(id in self.documentsId):
            return

        self.documentsId.append(id)

    def RemoveDocumentId(self, id):
        if(self.currDocumentId == id):
            self.currDocumentId= None

        self.documentsId.remove(id)

    def SetCurrentEventRecordingDocumentID(self, id):
        self.AddDocumentId(id)
        self.currDocumentId= id

    def GetCurrentEventRecordingDocumentId(self):
        return self.currDocumentId

EventRecorderController= EventRecorderManager()