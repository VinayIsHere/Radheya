from flask import Flask, request, jsonify
from src.ApplicationModes import ApplicationModes
from ScreenAutomation import startEventRecording, startEventReplaying, stopRecordingOrReplaying

app= Flask(__name__)

@app.route("/api/v1/recordingModes", methods=['GET'])
def GetRecordingModes():
    return jsonify(ApplicationModes.dict())

@app.route("/api/v1/startrecording", methods=['POST'])
def StartEventRecording():
    json_data= request.get_json()
    appMode= json_data["eventmode"]

    print("appMode:", appMode)
    docId=startEventRecording(appMode)

    #create a file and return it's uuid.
    return jsonify({"documentid": docId})
