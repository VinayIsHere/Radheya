from src.ApplicationModes import ApplicationModes
from ScreenAutomation import ScreenRecorderAutomation, ScreenReplayerAutomation
import time

ScreenRecorder = None
ScreenReplayer= None

def StartScreenRecorder():
    global ScreenRecorder
    app_mode= ApplicationModes.eKeyboardAndMouseEventRecordMode
    ScreenRecorder = ScreenRecorderAutomation(app_mode)
    uuid = ScreenRecorder.getUuid()

    ScreenRecorder.start()
    return uuid

def StopRecorder(uuid):
    global ScreenRecorder
    ScreenRecorder.stopEventRecordingAndSave(uuid, "V:/vinayPersonal/PythonProjects/Radheya/jsonfiles/myjson.json", True)
    ScreenRecorder.join()
        
def StartReplayer(uuid, fileToReplay):
    global ScreenReplayer
    ScreenReplayer= ScreenReplayerAutomation(uuid, fileToReplay)
    ScreenReplayer.start()

#uuid=StartScreenRecorder()
#time.sleep(10)
#StopRecorder(uuid)

#StartReplayer("dbd1f073-77c4-4320-bb68-1cbcdb85a6d3", "V:/vinayPersonal/PythonProjects/Radheya/jsonfiles/myjson.json")
#time.sleep(10)