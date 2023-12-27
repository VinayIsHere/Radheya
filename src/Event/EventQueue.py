from threading import Thread, Lock
import threading
import queue

mutex= Lock()
EventQueue= queue.Queue()

def AddEvent(event):
    mutex.acquire()
    EventQueue.put(event)
    mutex.release()
