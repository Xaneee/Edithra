"use client";
import { useState } from "react";
import axios from "axios";

export default function UploadVideo() {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file first.");
      return;
    }
    const formData = new FormData();
    formData.append("file", file);

    try {
      await axios.post(`${process.env.NEXT_PUBLIC_API_BASE_URL}/videos/upload`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setMessage("Upload successful.");
    } catch (error) {
      setMessage("Upload failed.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <div className="bg-white p-6 shadow-md rounded-lg w-80">
        <h2 className="text-xl font-bold text-center">Upload Video</h2>
        <input type="file" className="w-full p-2 border rounded mt-2" onChange={(e) => setFile(e.target.files ? e.target.files[0] : null)} />
        <button onClick={handleUpload} className="w-full bg-gradient-to-r from-green-500 to-teal-500 hover:scale-105 transition transform duration-300 text-gray-100 p-2 mt-3 rounded">Upload</button>
        {message && <p className="text-blue-500 text-center mt-3">{message}</p>}
      </div>
    </div>
  );
}


