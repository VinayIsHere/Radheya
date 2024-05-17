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
#time.sleep(30)
#StopRecorder(uuid)

StartReplayer("769d5e55-c6c1-463f-b3c3-2024bda9ad58", "V:/vinayPersonal/PythonProjects/Radheya/jsonfiles/myjson.json")
time.sleep(60)