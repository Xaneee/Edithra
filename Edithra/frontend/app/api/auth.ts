import { NextApiRequest, NextApiResponse } from "next";

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === "POST") {
    const { email, password } = req.body;
    if (email === "test@example.com" && password === "password") {
      return res.status(200).json({ user: { id: "1", email } });
    } else {
      return res.status(401).json({ message: "Invalid credentials" });
    }
  }

  return res.status(405).json({ message: "Method not allowed" });
}


