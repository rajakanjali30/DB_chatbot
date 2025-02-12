import { useState, useEffect } from "react";
import { TextField, Button, Container, Box, Typography } from "@mui/material";
import axios from "axios";

const API_URL = "http://127.0.0.1:5000";  // ✅ Correct API URL

const App = () => {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [isBackendConnected, setIsBackendConnected] = useState(false);

  // ✅ Check if backend is running
  useEffect(() => {
    axios
      .get(`${API_URL}/health`)
      .then(() => setIsBackendConnected(true))
      .catch(() => setIsBackendConnected(false));
  }, []);

const handleSendMessage = async () => {
  if (!message) return;

  try {
    const response = await axios.post(`${API_URL}/chat`, 
      { message },  // ✅ Send message in correct JSON format
      { headers: { "Content-Type": "application/json" } }
    );

    setChatHistory((prev) => [...prev, { sender: "bot", text: response.data.reply }]);
  } catch (error) {
    console.error("Error fetching chatbot response:", error);
    setChatHistory((prev) => [...prev, { sender: "bot", text: "Error: Could not reach the server." }]);
  }
};


  return (
    <Container maxWidth="sm">
      <Box sx={{ display: "flex", flexDirection: "column", height: "80vh" }}>
        <Typography variant="h4" gutterBottom>
          Chatbot
        </Typography>
        <Typography
          variant="subtitle1"
          sx={{ color: isBackendConnected ? "green" : "red", marginBottom: 2 }}
        >
          {isBackendConnected
            ? "✅ Connected to Backend"
            : "❌ Backend Not Reachable"}
        </Typography>

        {/* ✅ Chat Display Box */}
        <Box
          sx={{
            flexGrow: 1,
            overflowY: "auto",
            border: "1px solid #ccc",
            borderRadius: "8px",
            padding: 2,
            marginBottom: 2,
            maxHeight: "60vh",
          }}
        >
          {chatHistory.map((chat, index) => (
            <Box
              key={index}
              sx={{
                display: "flex",
                flexDirection: chat.sender === "user" ? "row-reverse" : "row",
                marginBottom: 1,
              }}
            >
              <Box
                sx={{
                  padding: 1,
                  borderRadius: "8px",
                  backgroundColor:
                    chat.sender === "user" ? "#f0f0f0" : "#e3f2fd",
                }}
              >
                {chat.text}
              </Box>
            </Box>
          ))}
        </Box>

        {/* ✅ Input and Send Button */}
        <Box sx={{ display: "flex" }}>
          <TextField
            label="Type a message"
            variant="outlined"
            fullWidth
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
          <Button
            variant="contained"
            color="primary"
            onClick={handleSendMessage}
            sx={{ marginLeft: 2 }}
          >
            Send
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default App;
