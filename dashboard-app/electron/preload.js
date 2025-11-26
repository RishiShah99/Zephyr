const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods to renderer process
contextBridge.exposeInMainWorld('zephyrAPI', {
  // Communication with Python backend
  sendCommand: async (command) => {
    const response = await fetch('http://localhost:5000/command', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ command })
    });
    return response.json();
  },
  
  getMemory: async () => {
    const response = await fetch('http://localhost:5000/memory');
    return response.json();
  },
  
  getProjects: async () => {
    const response = await fetch('http://localhost:5000/projects');
    return response.json();
  },
});

// Window controls - separate namespace
contextBridge.exposeInMainWorld('electron', {
  minimize: () => ipcRenderer.send('minimize-window'),
  maximize: () => ipcRenderer.send('maximize-window'),
  close: () => ipcRenderer.send('close-window')
});
