import React, { createContext, useState, useEffect } from "react";
import { getToken, setToken, logout as apiLogout } from "./api";

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setTokenState] = useState(getToken());

  useEffect(() => {
    if (token) setToken(token);
  }, [token]);

  const login = (token, user) => {
    setToken(token);
    setTokenState(token);
    setUser(user);
  };

  const logout = () => {
    apiLogout();
    setTokenState(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>{children}</AuthContext.Provider>
  );
}
