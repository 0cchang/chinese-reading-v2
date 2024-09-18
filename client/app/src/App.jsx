import { useState } from 'react';
import './App.css';

function App() {
  const [chinese_character, setChineseCharacter] = useState("");
  const [id, setId] = useState("");

  const fetchCharacterFromOmega = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/mcq/get-character/?id=${id}`);
      const data = await response.json();
      if (data.character) {
        setChineseCharacter(data.character);
      } else {
        setChineseCharacter('Character not found');
      }
    } catch (error) {
      console.error('Error fetching character:', error);
      setChineseCharacter('Error fetching character');
    }
  };

  return (
    <>
      <h1>MCQ</h1>
      <input 
        type="number" 
        value={id} 
        onChange={(e) => setId(e.target.value)} 
        placeholder="Enter ID (1-5000)" 
      />
      <button onClick={fetchCharacterFromOmega}>Get Character</button>
      <div>
        <p>{chinese_character}</p>
      </div>
    </>
  );
}

export default App;