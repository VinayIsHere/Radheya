import env from "../../config/index.json";
const ApiEndPoints = {
  recordingModes: `${env.baseUrl}/recordingModes`,
  startRecording: `${env.baseUrl}/startrecording`,
};

export default ApiEndPoints;
