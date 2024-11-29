from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from yt_dlp import YoutubeDL
import os
from pathlib import Path
import re

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoDownloadRequest(BaseModel):
    url: str
    format: str = 'mp4'

    @validator('url')
    def validate_url(cls, v):
        # Basic URL validation
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        if not url_pattern.match(v):
            raise ValueError("Invalid URL format")
        
        return v

@app.post("/download")
async def download_video(request: VideoDownloadRequest):
    # Ensure downloads directory exists
    downloads_path = str(Path.home() / "Downloads" / "video_downloader")
    os.makedirs(downloads_path, exist_ok=True)

    # Configure YoutubeDL options
    ydl_opts = {
        'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best' if request.format == 'mp3' else 'bestvideo+bestaudio/best',
        'nooverwrites': True,
        'no_color': True,
        'progress_hooks': [print],  # Optional: print download progress
    }

    # Add post-processing for MP3 conversion
    if request.format == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.url, download=True)
            filename = ydl.prepare_filename(info)
            
            # Modify filename if needed for MP3
            if request.format == 'mp3':
                filename = filename.rsplit('.', 1)[0] + '.mp3'

            return FileResponse(
                filename, 
                filename=os.path.basename(filename), 
                media_type='audio/mpeg' if request.format == 'mp3' else 'video/mp4'
            )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Video Downloader API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)