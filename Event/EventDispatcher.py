import sys
sys.path.append("..")

from .EventQueue import EventQueue
from Communicator.Communicator import Communicator

#Shall be Responsible for Storing All the Events during Capturing.
class EventDispatcher(Communicator):
    def __init__(self):
        Communicator.__init__(self)

    def unsubscribeAll(self):
        self.subscribers.clear()

    def unsubscribeEvent(self, subscriber):
        if(len(self.subscribers)== 0):
            return #No subcribers

        if(subscriber in self.subscribers):
            self.subcribers.pop(subscriber)

    def subscribeEvent(self, eventtype, subcriber):
        if(self.subscribers.get(eventtype) == None):
            self.subscribers[eventtype]= list()

        self.subscribers[eventtype].append(subcriber)

    def publishEvent(self, event):
        #EventQueue.AddEvent(event)
        
        if(self.subscribers.get(event.getEventType()) == None):
            return #No Subscribers present for the given type

        for subscriber in self.subscribers[event.getEventType()]:
            subscriber.receive(event)

    def receive(self, event):
        pass
        
EventsDispatcher= EventDispatcher()