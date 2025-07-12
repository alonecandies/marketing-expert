import React, { useState, useContext } from "react";
import { signup, login } from "../api";
import { AuthContext } from "../AuthContext";

export default function AuthPage() {
  const [isSignUp, setIsSignUp] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { login: doLogin } = useContext(AuthContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      if (isSignUp) {
        await signup(email, password);
        setIsSignUp(false);
      } else {
        const { access_token } = await login(email, password);
        doLogin(access_token, { email });
      }
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen gap-4">
      <form
        onSubmit={handleSubmit}
        className="flex flex-col gap-2 w-80 p-6 bg-white rounded shadow"
      >
        <h2 className="text-xl font-bold mb-2">{isSignUp ? "Sign Up" : "Sign In"}</h2>
        <input
          className="border p-2 rounded"
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          className="border p-2 rounded"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        {error && <div className="text-red-500 text-sm">{error}</div>}
        <button className="bg-primary text-white py-2 rounded mt-2" type="submit">
          {isSignUp ? "Sign Up" : "Sign In"}
        </button>
        <button
          type="button"
          className="text-blue-500 text-sm mt-2"
          onClick={() => setIsSignUp((s) => !s)}
        >
          {isSignUp ? "Already have an account? Sign In" : "Don't have an account? Sign Up"}
        </button>
      </form>
    </div>
  );
}
