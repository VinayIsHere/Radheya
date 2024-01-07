from ..DesignPatterns.SingletonMeta import singleton

@singleton
class StorageManager:
    def __init__(self, dataSource=None):
        self._currentDataSource= dataSource
        self._storageManager= dict()

    def AddDocumentForStorage(self, documentId, storage):
        self._storageManager[documentId]= storage
    
    def GetStorageForDocument(self, documentId):
        print("__documentId:", documentId)
        return self._storageManager.get(documentId)

    def GetDataSource(self):
        return self._currentDataSource

    def ChangeDataSource(self, datasource):
        self._currentDataSource= datasource

    def SaveIntoStorage(self, documentId, filepath, saveOrNot):
        storage= self.GetStorageForDocument(documentId)
        
        if(saveOrNot == True):
            storage.InternalWrite(filepath)
        
        storage.ClearBuffer()

StorageController= StorageManager()