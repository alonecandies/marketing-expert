import React, { useContext, useState } from "react";
import { AuthProvider, AuthContext } from "./AuthContext";
import AuthPage from "./pages/AuthPage";
import ChatPage from "./pages/ChatPage";
import UserPage from "./pages/UserPage";

function AppRoutes() {
  const { token } = useContext(AuthContext);
  const [page, setPage] = useState("chat");
  if (!token) return <AuthPage />;
  return (
    <>
      <nav className="flex gap-4 p-4 bg-gray-100">
        <button onClick={() => setPage("chat")} className="text-blue-600">
          Chat
        </button>
        <button onClick={() => setPage("user")} className="text-blue-600">
          User
        </button>
      </nav>
      {page === "chat" ? <ChatPage /> : <UserPage />}
    </>
  );
}

function App() {
  return (
    <AuthProvider>
      <AppRoutes />
    </AuthProvider>
  );
}

export default App;
