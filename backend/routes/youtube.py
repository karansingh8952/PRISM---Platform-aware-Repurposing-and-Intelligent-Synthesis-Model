from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from youtube_transcript_api import YouTubeTranscriptApi
from backend.database import get_db
from backend.models import ContentInput

router = APIRouter()

class YoutubeInput(BaseModel):
    url: str

@router.post("/extract/youtube")
def extract_youtube(payload: YoutubeInput, db: Session = Depends(get_db)):
    video_id = payload.url.split("v=")[-1].split("&")[0]

    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)
    text = " ".join([snippet.text for snippet in transcript])  
    text = text.replace("\n", " ").replace("♪", "").strip()

    new_input = ContentInput(
        type="youtube",
        raw_text=text,
        source_url=payload.url
    )
    db.add(new_input)
    db.commit()
    db.refresh(new_input)
    return {"id": str(new_input.id), "raw_text": text}