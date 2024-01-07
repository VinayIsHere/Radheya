const { app, BrowserWindow, ipcMain } = require("electron")
const { dialog } = require('electron');

const saveFile = async () => {
  console.log("here in save");
  try {
    const res = await dialog
      .showSaveDialog({
        defaultPath: "C:/",
        title: "Save File",
        buttonLabel: "Save",
        filters: [
          { name: "json", extensions: ["json"] },
        ],
      })
  
      if (!res.canceled) {
        const filePath = res.filePath;
        console.log("here are we",filePath)
        
      }
    
  } catch (err) {
    console.error(err);
  }
};

async function createWindow() {
  const win = new BrowserWindow({
    width: 450,
    height: 200,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation:true,
      preload: __dirname + '/preload.cjs'
    },

  });

  if (process.env.NODE_ENV!="production") {
    const server = await (await import("vite")).createServer({
      server: { base: './' },
    });

    await server.listen();
    win.loadURL(`http://localhost:${server.config.server.port}`);

    let modalWindow 
    ipcMain.on("hello",(event,...args)=>{
      modalWindow = new BrowserWindow({
        width: 400,
        height: 300,
        parent: win, // Set the parent window if needed
        modal: true,
        webPreferences: {
          nodeIntegration: true,
          contextIsolation: true,
          preload: __dirname + "/preload.cjs",
        },
      });
      modalWindow.loadURL(`http://localhost:${server.config.server.port}/modal`);

    })

    ipcMain.on("modelAction",(event,...args)=>{
      
      console.log(args)
      const data=args[0];

      if(!data?.save){
        console.log("closed")
        modalWindow.close();
      }
      
      
      if(data?.save){
        console.log("saved")
        saveFile()
        modalWindow.close();
      }
      

    })

  } else {
    win.loadFile('dist/index.html'); // Load the production build
    ipcMain.on("hello",(event,...args)=>{
      const modalWindow = new BrowserWindow({
        width: 400,
        height: 300,
        parent: win, // Set the parent window if needed
        modal: true,
        webPreferences: {
          nodeIntegration: true,
        },
      });

      modalWindow.loadURL(`/modal`);

    })
  }

  // Open DevTools (optional)
  win.webContents.openDevTools();
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
