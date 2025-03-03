from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "Edithra/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload/")
def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"message": "Video uploaded successfully", "file_path": file_path}

@router.get("/videos/")
def list_videos():
    videos = os.listdir(UPLOAD_DIR)
    return {"videos": videos}




