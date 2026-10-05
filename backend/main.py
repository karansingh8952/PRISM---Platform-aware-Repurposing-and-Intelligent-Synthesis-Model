from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=True)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import extract, text, youtube, summarize


app = FastAPI(title="PRISM Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(extract.router)
app.include_router(text.router)
app.include_router(youtube.router)
app.include_router(summarize.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}