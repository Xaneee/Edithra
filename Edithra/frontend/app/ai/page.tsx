"use client";
import { useEffect, useState } from "react";
import axios from "axios";

export default function AIProcessingStatus() {
  const [status, setStatus] = useState([]);

  useEffect(() => {
    async function fetchStatus() {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_BASE_URL}/ai/status`);
      setStatus(response.data);
    }
    fetchStatus();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold text-center">AI Processing Status</h1>
      <ul className="mt-6 space-y-2">
        {status.map((job: any) => (
          <li key={job.id} className="bg-white p-4 shadow-md rounded">{job.status}</li>
        ))}
      </ul>
    </div>
  );
}


