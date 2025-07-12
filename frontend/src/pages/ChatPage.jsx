import React, { useState, useEffect, useContext } from "react";
import { AuthContext } from "../AuthContext";
import { getToken } from "../api";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

async function startConversation(token) {
  const res = await fetch(`${API_URL}/conversations/start`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

async function sendMessage(conversationId, role, content, token) {
  const res = await fetch(`${API_URL}/conversations/${conversationId}/message`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
    body: JSON.stringify({ role, content }),
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

async function aiChat(conversationId, token) {
  const res = await fetch(`${API_URL}/ai/chat/${conversationId}`, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

async function getHistory(token) {
  const res = await fetch(`${API_URL}/conversations/history`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

export default function ChatPage() {
  const { token } = useContext(AuthContext);
  const [conversationId, setConversationId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (token) {
      startConversation(token)
        .then(({ conversation_id }) => setConversationId(conversation_id))
        .catch((err) => setError(err.message));
    }
  }, [token]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    setLoading(true);
    setError("");
    try {
      await sendMessage(conversationId, "user", input, token);
      setMessages((msgs) => [...msgs, { role: "user", content: input }]);
      setInput("");
      const { response } = await aiChat(conversationId, token);
      setMessages((msgs) => [...msgs, { role: "assistant", content: response }]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center min-h-screen bg-gray-50">
      <div className="w-full max-w-xl mt-8 bg-white rounded shadow p-4">
        <h2 className="text-2xl font-bold mb-4">Marketing Expert Chat</h2>
        <div className="flex flex-col gap-2 mb-4 max-h-96 overflow-y-auto">
          {messages.map((msg, i) => (
            <div key={i} className={msg.role === "user" ? "text-right" : "text-left"}>
              <span
                className={
                  msg.role === "user"
                    ? "bg-blue-100 px-2 py-1 rounded"
                    : "bg-green-100 px-2 py-1 rounded"
                }
              >
                <b>{msg.role === "user" ? "You" : "Expert"}:</b> {msg.content}
              </span>
            </div>
          ))}
        </div>
        <form onSubmit={handleSend} className="flex gap-2">
          <input
            className="flex-1 border p-2 rounded"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={loading}
            placeholder="Ask anything about marketing..."
          />
          <button
            className="bg-primary text-white px-4 py-2 rounded"
            type="submit"
            disabled={loading}
          >
            Send
          </button>
        </form>
        {error && <div className="text-red-500 text-sm mt-2">{error}</div>}
      </div>
    </div>
  );
}
