from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text as sql
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import ContentInput
from ai_llm.llm_service import generate_content

router = APIRouter()

@router.post("/summarize/{content_id}")
def summarize(content_id: str, db: Session = Depends(get_db)):
    content = db.query(ContentInput).filter(ContentInput.id == content_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")

    result = generate_content(
        f"Summarize this in 3-5 key points: {content.raw_text}"
    )
    if result.get("error"):
        raise HTTPException(status_code=502, detail=result["error"])

    db.execute(
        sql("insert into content_dna (input_id, top_insights) values (:i, :t)"),
        {"i": content.id, "t": result["response"]},
    )
    db.commit()
    return {"id": content_id, "summary": result["response"]}