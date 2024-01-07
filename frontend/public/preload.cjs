/* eslint-disable no-undef */
const {ipcRenderer, contextBridge} = require('electron');
contextBridge.exposeInMainWorld("ipc",ipcRenderer)

