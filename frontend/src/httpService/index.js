import axios from "axios";
import { toast } from "react-toastify";


const httpService = {
  get: axios.get,
  post: axios.post,
  put: axios.put,
};

export default httpService;
