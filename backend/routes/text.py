from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import ContentInput

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/extract/text")
def extract_text(payload: TextInput, db: Session = Depends(get_db)):
    new_input = ContentInput(
        type="text",
        raw_text=payload.text,
        source_url=None
    )
    db.add(new_input)
    db.commit()
    db.refresh(new_input)
    return {"id": str(new_input.id), "raw_text": new_input.raw_text}
