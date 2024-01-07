import React from 'react'
import { Button } from './button'
import { CheckIcon, DeleteIcon } from './icons'

const Modal = ({setOpen,open}) => {

  const curOpen=open??true;
  return (
    <div
    className={`${!curOpen?"hidden":''}`} >
    <div className="bg-white rounded-md p-8">
      <h2 className="text-xl font-bold mb-4">Save Your Progress</h2>
      <p className="mb-6">Are you sure you want to save current progress and exit?</p>
      <div className="flex gap-4">
        <Button className="border p-2 rounded-md bg-red-500 text-white" onClick={()=>{
          window.ipc.send("modelAction",{save:false})
          setOpen?.(false)}}>
          <DeleteIcon className="w-4 h-4 mr-2" />
          Cancel
        </Button>
        <Button className="border p-2 rounded-md bg-green-500 text-white" onClick={()=>{
          window.ipc.send("modelAction",{save:true})
          setOpen?.(false)}}>
          <CheckIcon className="w-4 h-4 mr-2" />
          Confirm
        </Button>
      </div>
    </div>
  </div>
  )
}

export default Modal