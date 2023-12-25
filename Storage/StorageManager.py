import sys
sys.path.append("..")

from DesignPatterns.SingletonMeta import singleton

@singleton
class StorageManager:
    def __init__(self, dataSource=None):
        self._currentDataSource= dataSource
        
    def GetDataSource(self):
        return self._currentDataSource

    def ChangeDataSource(self, datasource):
        self._currentDataSource= datasource