import Versions from './components/Versions'
import electronLogo from './assets/electron.svg'
import { useState } from 'react';

function App(): JSX.Element {
  const ipcHandle = (): void => window.electron.ipcRenderer.send('ping');

  const [rustResult, setRustResult] = useState<string | null>(null);
  const [tensorflowResult, setTensorflowResult] = useState<string | null>(null)

  const callRustApi = async (): Promise<void> => {
    const response = await fetch("http://127.0.0.1:8000/api/rust-process/")
    const data = await response.text() // Assuming a simple string response
    setRustResult(data)
  };

  const callTensorflowApi = async (): Promise<void> => {
    const response = await fetch("http://127.0.0.1:8000/api/tensorflow-process/");
    const data = await response.text() // Assuming a simple string response
    setTensorflowResult(data)
  };


  return (
    <>
      <img alt="logo" className="logo" src={electronLogo} />
      <div className="creator">Powered by electron-vite</div>
      <div className="text">
        Build an Electron app with <span className="react">React</span>
        &nbsp;and <span className="ts">TypeScript</span>
      </div>
      <p className="tip">
        Please try pressing <code>F12</code> to open the devTool
      </p>
      <div className="actions">
        <div className="action">
          <a href="https://electron-vite.org/" target="_blank" rel="noreferrer">
            Documentation
          </a>
        </div>
        <div className="action">
          <a target="_blank" rel="noreferrer" onClick={ipcHandle}>
            Send IPC
          </a>
        </div>
      </div>
      <Versions></Versions>
      <div style={{ padding: "20px" }}>
      <button onClick={callRustApi}>Call Rust API</button>
      <p>Rust Result: {rustResult}</p>

      <button onClick={callTensorflowApi}>Call TensorFlow API</button>
      <p>TensorFlow Result: {tensorflowResult}</p>
    </div>
    </>
  )
}

export default App
