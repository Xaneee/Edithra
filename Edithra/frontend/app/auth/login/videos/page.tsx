"use client";
import React from "react";
import { useVideos } from "@/hooks/useVideos";

export default function VideosPage() {
  const { videos } = useVideos();

  return (
    <div>
      <h1>Uploaded Videos</h1>
      <ul>
        {videos.map((video) => (
          <li key={video.id}>
            <a href={video.url} target="_blank" rel="noopener noreferrer">
              {video.title}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}


