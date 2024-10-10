import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [name, setName] = useState<string>('');

  const fetchName = async () => {
    try {
      const response = await axios.get('/api/name');
      setName(response.data.name);
    } catch (error) {
      console.error('Error fetching name:', error);
      setName('Unknown');
    }
  };

  useEffect(() => {
    fetchName();
  }, []);

  return (
    <div className="App">
      <h1>Hello, {name}</h1>
      <button onClick={fetchName}>Reload Name</button>
    </div>
  );
}

export default App;
