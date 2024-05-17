from flask import Flask, request, jsonify
from src.ApplicationModes import ApplicationModes
from ScreenAutomation import ScreenRecorderAutomation, ScreenReplayerAutomation
import time
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

ScreenRecorder= None
ScreenReplayer= None

@app.route("/api/v1/recordingModes", methods=['GET'])
def get_recording_modes():
    """
    Endpoint to retrieve available recording modes.

    Returns:
        JSON: Recording modes
    """
    try:
        # Retrieve recording modes from the ApplicationModes class
        recording_modes = ApplicationModes.dict()

        # Return a JSON response with recording modes and a 200 status code
        return jsonify(recording_modes), 200

    except Exception as e:
        # Handle exceptions with a 500 status code
        return jsonify({"error": str(e)}), 500

"""
    Endpoint to start event recording.

    Returns:
        JSON: {"documentid": <document_id>}
"""
@app.route("/api/v1/startRecording", methods=['GET', 'POST'])
def start_event_recording():
    if(request.method == 'POST'):
        try:
            global ScreenRecorder
            # Extract the application mode from the JSON data
            json_data = request.get_json()
            
            print(json_data)

            app_mode = ApplicationModes(json_data["eventmode"])

            # Log the application mode
            print("app_mode:", app_mode)
            
            ScreenRecorder=None
            ScreenRecorder=ScreenRecorderAutomation(app_mode)

            uuid= ScreenRecorder.getUuid()
            
            ScreenRecorder.start()
            time.sleep(3) #Delay for the initialization of ScreenRecorder.

            return jsonify({"documentid": uuid}), 200

        except KeyError as e:
            # Handle missing or incorrect key in the JSON data with a 400 status code
            return jsonify({"error": "Invalid or missing key: {}".format(str(e))}), 400

        except Exception as e:
            # Handle other exceptions with a 500 status code
            return jsonify({"error": str(e)}), 500

@app.route("/api/v1/stopRecording/", methods=['POST'])
def stop_recording():
    try:
        global ScreenRecorder

        json_data = request.get_json()
        documentId = json_data["documentid"]
        filepath= json_data["filepath"]
        saveOrNot= json_data["save"]

        # Call the function to stop recording or replaying
        ScreenRecorder.stopEventRecordingAndSave(documentId, filepath, bool(saveOrNot))
        ScreenRecorder=None
        
        # Return a 200 status code along with the document ID in the response
        response_data = {"status": "success", "documentId": documentId}
        return jsonify(response_data), 200
    except Exception as e:
        # Return an error status code and message in case of an exception
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/v1/startReplay", methods= ["POST"])
def start_replay():
    if(request.method == "POST"):
        try:
            global ScreenReplayer
            json_data = request.get_json()

            uuid= json_data["documentid"]
            fileToReplay= json_data["filepath"]
            
            ScreenReplayer = ScreenReplayerAutomation(uuid, fileToReplay)
            ScreenReplayer.start()

            # Return a 200 status code along with the document ID in the response
            response_data = {"status": "success", "documentId": uuid}
            return jsonify(response_data), 200

        except Exception as e:
            # Handle other exceptions with a 500 status code
            return jsonify({"error": str(e)}), 500


@app.route("/", methods=['GET'])
def Hello():
    return "Hello World"