import { useState, useEffect } from "react";
import axios from "axios";

interface Video {
  id: string;
  title: string;
  url: string;
}

export const useVideos = () => {
  const [videos, setVideos] = useState<Video[]>([]);

  useEffect(() => {
    const fetchVideos = async () => {
      try {
        const response = await axios.get("/api/videos");
        setVideos(response.data);
      } catch (error) {
        console.error("Failed to fetch videos", error);
      }
    };

    fetchVideos();
  }, []);

  return { videos };
};


