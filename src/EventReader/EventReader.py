class EventReader:
    def __init__(self, storage, eventListener):
        self._storage= storage
        self._eventList= list() #list of events
        self._eventListener= eventListener
        self._stop= False

    def start(self):
        self._eventList= self._storage.Read()
        print(self._eventList)
        self.publishEvent()

    def stop(self):
        self._stop=True

    def restart(self):
        self._stop= False
        self.publishEvent()

    def publishEvent(self):
        if(len(self._eventList)<=0):
            print("Empty Event List")
            return

        while(len(self._eventList)> 0):
            if(self._stop== True):
                break
            
            self._eventListener.publishEvent(self._eventList[0])
            self._eventList.remove(self._eventList[0])
