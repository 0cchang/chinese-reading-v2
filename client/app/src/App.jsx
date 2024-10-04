import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [chineseCharacter, setChineseCharacter] = useState("");
  const [id, setId] = useState("");
  const [chineseText, setChineseText] = useState("");
  const [savedTexts, setSavedTexts] = useState([]);
  const [currentPosition, setCurrentPosition] = useState(0); // Track the current character position
  const [isEndOfText, setIsEndOfText] = useState(false); // Track if the user reached the end

  // Function to fetch character from Omega using an ID
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

  // Function to submit Chinese text and save as a "saved text"
  const handleTextSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/mcq/saveText/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: chineseText }),
      });
      if (response.ok) {
        console.log('Text saved successfully!');
        setChineseText('');
        fetchSavedTexts(); // Refresh the saved texts list
      } else {
        console.error('Failed to save text');
      }
    } catch (error) {
      console.error('Error submitting text:', error);
    }
  };

  // Function to fetch saved texts
  const fetchSavedTexts = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/mcq/savedTexts/');
      const data = await response.json();
      setSavedTexts(data);
    } catch (error) {
      console.error('Error fetching saved texts:', error);
    }
  };

  // Function to delete a saved text
  const deleteSavedText = async (textId) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/mcq/delete-savedtext/${textId}/`, {
        method: 'DELETE',
      });
      if (response.ok) {
        console.log('Saved text deleted successfully');
        fetchSavedTexts(); // Refresh the saved texts list
      } else {
        console.error('Failed to delete saved text');
      }
    } catch (error) {
      console.error('Error deleting saved text:', error);
    }
  };

  // Fetch saved texts when the component mounts
  useEffect(() => {
    fetchSavedTexts();
  }, []);

  const handleKeyDown = async (event) => {
    if (chineseText.length === 0) return;

    if (event.key === 'ArrowLeft') {
      // Save the current character's ID (left arrow pressed)
      const currentCharacter = chineseText[currentPosition];
      const response = await fetch(
        `http://127.0.0.1:8000/mcq/get-character-id/?char=${currentCharacter}`
      );
      const data = await response.json();
      console.log('Character ID saved:', data.unique_id); // Save for later use
    }

    if (event.key === 'ArrowRight') {
      // Move to the next character (right arrow pressed)
      if (currentPosition < chineseText.length - 1) {
        setCurrentPosition(currentPosition + 1);
      } else {
        setIsEndOfText(true); // Reached the end of text
      }
    }
  };

  // Replay the text from the beginning
  const handleReplay = () => {
    setCurrentPosition(0);
    setIsEndOfText(false);
  };

  const renderTextWithHighlight = () => {
    return (
      <div className="pip-window">
        {chineseText.split('').map((char, index) => (
          <div
            key={index}
            className={`char-box ${index === currentPosition ? 'highlight' : ''}`}
          >
            {char}
          </div>
        ))}
      </div>
    );
  };

  return (
    <>
      <h1>MCQ</h1>

      {/* Input to fetch character based on ID */}
      <input 
        type="number" 
        value={id} 
        onChange={(e) => setId(e.target.value)} 
        placeholder="Enter ID (1-5000)" 
      />
      <button onClick={fetchCharacterFromOmega}>Get Character</button>
      <div>
        <p>{chineseCharacter}</p>
      </div>

      {/* Text area for submitting chunks of Chinese text */}
      <h2>Submit Chinese Text</h2>
      <form onSubmit={handleTextSubmit}>
        <textarea
          value={chineseText}
          onChange={(e) => setChineseText(e.target.value)}
          placeholder="Enter Chinese text here..."
          rows="5"
          cols="50"
        />
        <button type="submit">Save Text</button>
      </form>

      {/* Display saved texts with delete option */}
      <h2>Saved Texts</h2>
      <ul>
        {savedTexts.map((text) => (
          <li key={text.id}>
            <button onClick={() => setChineseText(text.text)}>
              Open Saved Text {text.id}
            </button>
          </li>
        ))}
      </ul>

      {/* Display PiP window */}
      {chineseText && (
        <>
          <h2>Reading Mode</h2>
          {renderTextWithHighlight()}
          {isEndOfText && (
            <button onClick={handleReplay}>
              Replay Text
            </button>
          )}
        </>
      )}
    </>
  );
}

export default App;
