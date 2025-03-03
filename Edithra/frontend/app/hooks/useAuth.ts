import { useState, useEffect } from "react";
import axios from "axios";

interface User {
  id: string;
  username: string;
  email: string;
}

export const useAuth = () => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const response = await axios.get("/api/auth/me");
        setUser(response.data);
      } catch (error) {
        setUser(null);
      }
    };

    checkAuth();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      const response = await axios.post("/api/auth/login", { email, password });
      setUser(response.data.user);
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const logout = () => {
    axios.post("/api/auth/logout");
    setUser(null);
  };

  return { user, login, logout };
};


