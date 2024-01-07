'use client'
import { CardTitle, CardHeader, CardContent, Card } from "./ui/card"
import { Button } from "./ui/button"
import { useEffect, useState } from "react";
import httpService from "@/httpService";
import ApiEndPoints from "@/httpService/apiEndPoints";

export function DashBoard() {
  const [open,setOpen]=useState(false)
  const [modeOptions,setModeOptions]=useState([]);
  const [curMode,setCurMode]=useState("")
  const [documentId,setDocumentId]=useState("")
  
  useEffect(()=>{
    httpService.get(ApiEndPoints.recordingModes).then((res)=>setModeOptions(res.data))
  },[])
  console.log(modeOptions);


  const handleStart=async()=>{

    try {
      
      const res= await httpService.post(ApiEndPoints.startRecording,{eventMode:curMode});

      setDocumentId(res.data?.documentid);

    } catch (error) {
      console.log(error)
    }
  }

  return (
    (<div
      className="relative flex flex-col w-full min-h-screen p-4 md:p-8">
      
      <main className="flex flex-col gap-4 p-0 md:gap-8 md:p-10">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
            <CardTitle className="text-lg font-bold">Dashboard Controls</CardTitle>
          </CardHeader>
          
          <CardContent className="flex flex-row items-center justify-around pt-4">
          <select onChange={(val)=>setCurMode(val)} value={curMode} className="border border-gray-300 rounded-md text-gray-600 h-10 pl-5 pr-10 bg-white hover:border-gray-400 focus:outline-none appearance-none">
                <option value="">Select an mode</option>
                {modeOptions.map(mode=><option value={mode}>{mode.slice(1)}</option>)}
              </select>
            <Button className="border p-2 rounded-md bg-blue-500 text-white" disabled={curMode?false:true} onClick={handleStart}>
              <PlayIcon className="w-4 h-4 mr-2" />
              Start
            </Button>
            <Button className="border p-2 rounded-md bg-red-500 text-white" disabled={curMode?false:true}  onClick={()=>{setOpen(true)
            window.ipc.send("hello","12345")
            }}>
              <MonitorStopIcon className="w-4 h-4 mr-2" />
              Stop & Save
            </Button>
            <Button className="border p-2 rounded-md bg-green-500 text-white">
              <RefreshCwIcon className="w-4 h-4 mr-2" />
              Resume
            </Button>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
            <CardTitle className="text-lg font-bold">Replay Feature</CardTitle>
          </CardHeader>
          <CardContent className="flex flex-row items-center justify-center pt-4">
            <Button className="border p-2 rounded-md bg-purple-500 text-white">
              <RepeatIcon className="w-4 h-4 mr-2" />
              Replay
            </Button>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
            <CardTitle className="text-lg font-bold">Save Pop-up</CardTitle>
          </CardHeader>
          <CardContent className="flex flex-row items-center justify-center pt-4">
            <Button className="border p-2 rounded-md bg-yellow-500 text-white" onClick={()=>setOpen(true)}>
              <SaveIcon className="w-4 h-4 mr-2" />
              Trigger Save Pop-up
            </Button>
          </CardContent>
        </Card>
      </main>
     
    </div>)
  );
}





function PlayIcon(props) {
  return (
    (<svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round">
      <polygon points="5 3 19 12 5 21 5 3" />
    </svg>)
  );
}


function MonitorStopIcon(props) {
  return (
    (<svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round">
      <rect x="9" y="7" width="6" height="6" />
      <rect width="20" height="14" x="2" y="3" rx="2" />
      <path d="M12 17v4" />
      <path d="M8 21h8" />
    </svg>)
  );
}


function RefreshCwIcon(props) {
  return (
    (<svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round">
      <path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8" />
      <path d="M21 3v5h-5" />
      <path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16" />
      <path d="M8 16H3v5" />
    </svg>)
  );
}


function RepeatIcon(props) {
  return (
    (<svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round">
      <path d="m17 2 4 4-4 4" />
      <path d="M3 11v-1a4 4 0 0 1 4-4h14" />
      <path d="m7 22-4-4 4-4" />
      <path d="M21 13v1a4 4 0 0 1-4 4H3" />
    </svg>)
  );
}


function SaveIcon(props) {
  return (
    (<svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round">
      <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z" />
      <polyline points="17 21 17 13 7 13 7 21" />
      <polyline points="7 3 7 8 15 8" />
    </svg>)
  );
}
