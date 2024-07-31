
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    const uploadResponse = await axios.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    const summarizeResponse = await axios.post('/summarize', {
      filepath: uploadResponse.data.filepath,
    });

    setSummary(summarizeResponse.data.summary);
  };

  return (
    <div className="App">
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload and Summarize</button>
      <div>
        <h3>Summary</h3>
        <p>{summary}</p>
      </div>
    </div>
  );
}

export default App;
