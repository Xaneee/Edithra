import axios from "axios";
import { useAuthStore } from "@/store/auth";

export function useAuth() {
  const { token, setToken } = useAuthStore();

  const login = async (email: string, password: string) => {
    const response = await axios.post(`${process.env.NEXT_PUBLIC_API_BASE_URL}/auth/login`, { email, password });
    setToken(response.data.token);
  };

  return { token, login };
}


