from fastapi import FastAPI
from backend.routes import extract, text, youtube, summarize

app = FastAPI(title="PRISM Backend")

app.include_router(extract.router)
app.include_router(text.router)
app.include_router(youtube.router)
app.include_router(summarize.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}