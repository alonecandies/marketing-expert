import React, { useContext, useEffect, useState } from "react";
import { AuthContext } from "../AuthContext";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

async function fetchMe(token) {
  const res = await fetch(`${API_URL}/auth/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

async function topUp(token, amount) {
  const res = await fetch(`${API_URL}/auth/topup`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
    body: JSON.stringify({ amount }),
  });
  if (!res.ok) throw new Error(await res.text());
  return await res.json();
}

export default function UserPage() {
  const { token, logout } = useContext(AuthContext);
  const [user, setUser] = useState(null);
  const [amount, setAmount] = useState(10);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  useEffect(() => {
    if (token) {
      fetchMe(token)
        .then(setUser)
        .catch((err) => setError(err.message));
    }
  }, [token]);

  const handleTopUp = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");
    try {
      const updated = await topUp(token, amount);
      setUser(updated);
      setSuccess("Credits topped up!");
    } catch (err) {
      setError(err.message);
    }
  };

  if (!user) return <div>Loading...</div>;

  return (
    <div className="flex flex-col items-center gap-4 mt-8">
      <div className="bg-white p-4 rounded shadow w-80">
        <h2 className="text-xl font-bold mb-2">User Info</h2>
        <div>Email: {user.email}</div>
        <div>Credits: {user.credits}</div>
        <form onSubmit={handleTopUp} className="flex gap-2 mt-4">
          <input
            type="number"
            min="1"
            value={amount}
            onChange={(e) => setAmount(Number(e.target.value))}
            className="border p-2 rounded w-20"
          />
          <button className="bg-primary text-white px-4 py-2 rounded" type="submit">
            Top Up
          </button>
        </form>
        {success && <div className="text-green-600 text-sm mt-2">{success}</div>}
        {error && <div className="text-red-500 text-sm mt-2">{error}</div>}
        <button className="text-red-500 text-sm mt-4" onClick={logout}>
          Log Out
        </button>
      </div>
    </div>
  );
}
