**SCREEN ACTIVITY PLAYER**
This application supports recording of Mouse and keyboard actions of the system and then replaying them back in your system. The Aim is to help with do repititive task or doing automation testing and yes for fun too.

**Completed Feature**
* Records Mouse and Keyboard actions.
* Replay the recorded actions.

**Feature Scope**
* Add a UI for this application for the ease of Application use.
* Add Image Detection AI Model, which will take Right output screen after the certain actions and will compare it to the actual screen which came up after replaying the same actions for which the truth image was generated.
* Code Refactoring
* Specifying the SRS for FrontEnd and BackEnd.

**How to Build**
Install Python 3.12 and then install following dependencies.
* flask ```pip install Flask```
* keyboard ```pip install keyboard ```
* pynput ```pip install pynput```
then open the visual studio and set ScreenPlayer.py as Startup project and build it.

**How to Run**
My aim was to make this library accessed through api, so that I can use any web app which supports the defined api for this application can use this project. Right now there are following APIs available and the param they need in their get/post request.

1. **API**:```/api/v1/recordingModes```
   **API Type**: GET
   **PARAM**: nothing
   **RETURNS**: returns the List of supported modes by the application.
   **DESCRIPTION**: This api is a GET request and returns the list of modes supported by the application.

2. **API**:```/api/v1/startRecording```
   **API Type**: POST
   **PARAM**: The body of the api request should contains the following information: {"eventmode": mode_number} e.g {"eventmode": 4} ```4=eKeyboardAndMouseEventRecordMode```
   **RETURNS**: Returns the ```documentId```. This ```documentId``` is the reference for the current recording application. In future when the application supports multiple record or replay operation at the same time. This will help keep track of those. For now it only support only single record or replay operation at a time. but still this ```documentId``` is used to get information about the current ongoing task.
   **DESCRIPTION**: This api is a POST request which takes the ```eventmode``` in the body of the request, This event mode decide which operation to start in the application.

3. **API**:```/api/v1/stopRecording```
   **API Type**: POST
   **PARAM**: The body of the api request should contains the following information: {"documentid": document_id, "filepath": path, "save": 1_or_0} e.g {"documentid": "2e3042eb-c4b1-4137-821f-c15095f7cbb5", "filepath": "V:/vinayPersonal/PythonProjects/Radheya/jsonfiles/myfile.json", "save": 1}. ```documentId``` is the one returned during startRecording API, ```filepath``` is the system path where the recorded actions json file should store, ```save``` is the parameter decides whether to store current action json. If ```save``` is 0, then ```filepath``` can remain empty, but if it is 1, then we should provide a valid ```filepath```.
   **RETURNS**: Returns the status of the operation along with the documentId.
   **DESCRIPTION**: This stops the action recording and store the stored actions into a physical file in the provided ```filepath```.

4. **API**:```/api/v1/startReplay```
   **API Type**: POST
   **PARAM**: The body of the api request should contains the following information: {"documentid": document_id, "filepath": path} e.g {"documentid": "2e3042eb-c4b1-4137-821f-c15095f7cbb5", "filepath": "V:/vinayPersonal/PythonProjects/Radheya/jsonfiles/myfile.json"}. ```documentId```: document Id for the replayed file, ```filepath```: Path of the replay json file.
   **RETURNS**: 200 Status for success
   **DESCRIPTION**: This reads the json file presents in the path and then replay the actions stored in that file.
